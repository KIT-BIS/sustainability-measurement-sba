#!/usr/bin/env python3
"""
GitHub Retention Metric using OpenSearch enriched data
"""

from opensearchpy import OpenSearch
from datetime import datetime, timedelta, timezone
from collections import defaultdict
# OpenSearch Connection
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'GrimoireLab.1'),
    # Port 9200 on this cluster is HTTPS/TLS (plain HTTP will yield "empty reply")
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False
)

def get_user_first_contribution(index='sba-issue_raw'):
    """Get first contribution date for each user"""

    query = {
        "size": 0,
        "aggs": {
            "users": {
                "terms": {
                    "field": "data.user.login",
                    "size": 10000
                },
                "aggs": {
                    "first_contribution": {
                        "min": {
                            "field": "data.created_at"
                        }
                    }
                }
            }
        }
    }

    result = client.search(index=index, body=query)

    user_first_contrib = {}
    for bucket in result['aggregations']['users']['buckets']:
        user = bucket['key']
        first_date = bucket['first_contribution']['value']
        user_first_contrib[user] = datetime.fromtimestamp(first_date / 1000, tz=timezone.utc)

    return user_first_contrib

def get_user_activities(index='sba-issue_raw', since_date=None):
    """Get all user activities since a date"""

    created_at_field = "data.created_at"

    query = {
        "size": 10000,
        "_source": ["data.user.login", "data.created_at", "data.state", "data.merged"],
        "query": {
            "range": {
                created_at_field: {
                    "gte": since_date.isoformat() if since_date else "now-180d"
                }
            }
        },
        "sort": [{created_at_field: "asc"}]
    }

    activities = []
    result = client.search(index=index, body=query, scroll='2m')
    scroll_id = result['_scroll_id']

    while len(result['hits']['hits']) > 0:
        for hit in result['hits']['hits']:
            source = hit['_source']
            data = source.get('data') or {}
            user_obj = data.get('user') or {}
            user_login = user_obj.get('login')
            created_at = data.get('created_at')
            if not user_login or not created_at:
                continue

            activities.append({
                'user': user_login,
                'date': datetime.fromisoformat(created_at.replace('Z', '+00:00')),
                'type': 'pr_created',
                'merged': data.get('merged', False)
            })

        result = client.scroll(scroll_id=scroll_id, scroll='2m')
        scroll_id = result.get('_scroll_id', scroll_id)

    client.clear_scroll(scroll_id=scroll_id)
    return activities

def calculate_retention(index='sba-issue_raw', period_days=90, now=None):
    """Calculate retention metric"""

    # Define periods
    # Allow callers to inject a fixed "now" for reproducible runs.
    # If a naive datetime is provided, assume it's UTC.
    if now is None:
        # Default "now" is rounded down to midnight UTC for stable day-to-day runs.
        now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    current_period_start = now - timedelta(days=period_days)
    previous_period_start = now - timedelta(days=period_days * 2)

    print(f"Previous period: {previous_period_start.date()} to {current_period_start.date()}")
    print(f"Current period: {current_period_start.date()} to {now.date()}")

    # Get data
    print("\nFetching user first contributions...")
    user_first_contrib = get_user_first_contribution(index)

    print(f"Fetching activities since {previous_period_start.date()}...")
    activities = get_user_activities(index, since_date=previous_period_start)

    # Categorize activities by period
    user_activities = defaultdict(lambda: {'previous': [], 'current': []})

    for activity in activities:
        user = activity['user']
        date = activity['date']

        if date >= current_period_start:
            user_activities[user]['current'].append(activity)
        elif date >= previous_period_start:
            user_activities[user]['previous'].append(activity)

    # Identify newcomers
    newcomers = []
    for user, first_date in user_first_contrib.items():
        if previous_period_start <= first_date < current_period_start:
            newcomers.append(user)

    # Check retention
    retained = []
    for user in newcomers:
        if len(user_activities[user]['current']) > 0:
            retained.append(user)

    # Results
    total_newcomers = len(newcomers)
    retained_count = len(retained)
    retention_rate = (retained_count / total_newcomers * 100) if total_newcomers > 0 else 0

    print(f"\n{'='*60}")
    print(f"RETENTION OF NEWCOMERS")
    print(f"{'='*60}")
    print(f"Total newcomers: {total_newcomers}")
    print(f"Retained: {retained_count}")
    print(f"Retention rate: {retention_rate:.1f}%")
    print(f"\nNewcomers:")
    for user in newcomers:
        first = user_first_contrib[user].date()
        current_acts = len(user_activities[user]['current'])
        all_acts = user_activities[user]['previous'] + user_activities[user]['current']
        latest = max((a['date'] for a in all_acts), default=None)
        latest_str = latest.date().isoformat() if latest else "-"
        status = "✅ RETAINED" if user in retained else "❌ Not retained"
        print(f"  {user:20} | First: {first} | Latest: {latest_str} | Current activities: {current_acts:2} | {status}")

    return {
        'total_newcomers': total_newcomers,
        'retained': retained_count,
        'retention_rate': retention_rate,
        'newcomers': newcomers,
        'retained_users': retained
    }

if __name__ == '__main__':
    try:
        result = calculate_retention('sba-issue_raw', period_days=365*2)
    except BrokenPipeError:
        # Allow piping to tools like `head` without stack traces.
        pass
