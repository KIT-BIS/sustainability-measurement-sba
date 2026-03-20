#!/usr/bin/env python3
"""
Newcomer Active/Leaving Classification using OpenSearch enriched data

Definition:
  - Newcomer: any user whose first patchset was made between a configured
    start date and now.
  - Active newcomer: last contribution was within the last `threshold_days`.
  - Leaving newcomer: last contribution was more than `threshold_days` ago.
"""

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from opensearchpy import OpenSearch

# OpenSearch Connection
client = OpenSearch(
    hosts=[{"host": "mini-pc", "port": 9200}],
    http_auth=("admin", "GrimoireLab.1"),
    # Port 9200 on this cluster is HTTPS/TLS (plain HTTP will yield "empty reply")
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)


def get_user_first_and_last_contribution(index="sba-issue_raw"):
    """
    For every user in the index, return their first and last contribution date.
    """

    """
    FIlter out all Bot user as well as codecentric maintainer
    """
    query = {
        "size": 0,
        "query": {
            "bool": {
                "must_not": [
                    {"term": {"data.user.type": "Bot"}},
                    {
                        "terms": {
                            "data.user.login": [
                                "SteKoe",
                                "ulischulte",
                                "erikpetzold",
                                "mirogaudi",
                                "hzpz",
                            ]
                        }
                    },
                ]
            }
        },
        "aggs": {
            "users": {
                "terms": {"field": "data.user.login", "size": 10000},
                "aggs": {
                    "first_contribution": {"min": {"field": "data.created_at"}},
                    "last_contribution": {"max": {"field": "data.created_at"}},
                },
            }
        },
    }

    result = client.search(index=index, body=query)

    user_data = {}
    for bucket in result["aggregations"]["users"]["buckets"]:
        user = bucket["key"]
        first_ts = bucket["first_contribution"]["value"]
        last_ts = bucket["last_contribution"]["value"]
        user_data[user] = {
            "first": date.fromtimestamp(first_ts / 1000),
            "last": date.fromtimestamp(last_ts / 1000),
        }

    return user_data


def classify_newcomers(index="sba-issue_raw", threshold_days=90, since=None, now=None):
    """
    Classify newcomers as Active or Leaving.

    Parameters
    ----------
    index : str
        OpenSearch index to query.
    threshold_days : int
        A newcomer is considered *leaving* when their last contribution was
        more than this many days ago.  Default: 90.
    since : date, optional
        Drop any user whose last contribution is older than this date.
        Defaults to 2014-01-01.
    now : date, optional
        Reference point for "today".  Defaults to today's date.
    """

    # Resolve "now"
    if now is None:
        now = date.today()

    # Resolve "since"
    if since is None:
        since = date(2014, 1, 1)

    leaving_threshold = now - timedelta(days=threshold_days)

    print(
        f"Since            : {since} (users with last contribution before this date are dropped)"
    )
    print(
        f"Leaving threshold: last contribution before {leaving_threshold} ({threshold_days} days ago)"
    )

    # Fetch data
    user_data = get_user_first_and_last_contribution(index)

    # Classify
    active = []
    leaving = []

    for user, dates in user_data.items():
        last = dates["last"]

        # Drop users whose last contribution is older than the since window
        if last < since:
            continue

        if last >= leaving_threshold:
            active.append(user)
        else:
            leaving.append(user)

    newcomers = active + leaving
    total = len(newcomers)
    active_count = len(active)
    leaving_count = len(leaving)

    # Output
    print(f"\n{'=' * 60}")
    print(f"NEWCOMER CLASSIFICATION")
    print(f"{'=' * 60}")
    active_pct = round(active_count / total * 100) if total > 0 else 0
    leaving_pct = round(leaving_count / total * 100) if total > 0 else 0

    print(f"Total newcomers : {total}")
    print(f"Active          : {active_count} ({active_pct}%)")
    print(f"Leaving         : {leaving_count} ({leaving_pct}%)")

    print(f"\nNewcomers:")
    active_set = set(active)
    for user in sorted(
        newcomers,
        key=lambda u: (u not in active_set, -user_data[u]["last"].toordinal()),
    ):
        first = user_data[user]["first"]
        last = user_data[user]["last"]
        status = "ACTIVE" if user in active_set else "LEAVING"
        print(f"  {user:30} | First: {first} | Last: {last} | {status}")

    return {
        "total_newcomers": total,
        "active": active_count,
        "leaving": leaving_count,
        "active_users": active,
        "leaving_users": leaving,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Classify newcomers as Active or Leaving."
    )
    parser.add_argument(
        "--index",
        default="sba-pull_raw",
        help="OpenSearch index to query (default: sba-pull_raw)",
    )
    parser.add_argument(
        "--since-months",
        type=int,
        default=None,
        metavar="N",
        help="Calculate 'since' as N months before today (overrides --since)",
    )
    parser.add_argument(
        "--since",
        default=None,
        metavar="YYYY-MM-DD",
        help="Drop users whose last contribution is before this date (default: 2014-01-01)",
    )
    parser.add_argument(
        "--threshold-days",
        type=int,
        default=90,
        help="Days before which a newcomer is considered leaving (default: 90)",
    )
    args = parser.parse_args()

    if args.since_months is not None:
        since = date.today() - relativedelta(months=args.since_months)
    elif args.since:
        since = date.fromisoformat(args.since)
    else:
        since = None

    try:
        classify_newcomers(args.index, threshold_days=args.threshold_days, since=since)
    except BrokenPipeError:
        # Allow piping to tools like `head` without stack traces.
        pass
