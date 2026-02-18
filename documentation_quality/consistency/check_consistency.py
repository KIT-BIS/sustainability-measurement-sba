import subprocess
import shutil
import os
import json
from pathlib import Path


def aggregate_results(json_dic):

    total_words = 0
    total_issues = 0

    for key, value in json_dic.items():

        # Skipping no results
        if value == "{}\n":
            continue

        res = json.loads(key)
        metrics = json.loads(value)
        for filename, issues in res.items():
            total_issues += len(issues)

        total_words += int(metrics["words"])


    return total_issues / total_words


def print_results(json_dic):
    working_dir = os.getcwd()

    file_path = os.path.join(working_dir, "consistency\\results.md")

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n")

        for key, value in json_dic.items():
            if value == "{}\n":
                 continue

            res = json.loads(key)
            for filename, issues in res.items():
                f.write("\n")
                f.write(filename)
                f.write("\n")
                for issue in issues:
                    f.write("  Check:" + issue["Check"])
                    f.write("  Message:" + issue["Message"])
                    f.write("  Severity:" + issue["Severity"])
                    f.write("  Line:" + str(issue["Line"]))
                    f.write("  Match:" + issue["Match"])
                    f.write("  Span:" + str(issue["Span"]))
                    f.write("\n")
    return 0



def check_consistency(temp_dir):
    working_dir = os.getcwd()
    prepare(temp_dir)
    doc_dir = os.path.join(temp_dir, "spring-boot-admin-docs\src\site\docs")

    json_list = []
    json_dic = {}

    for root, dirs, files in os.walk(doc_dir):
        for file in files:

            full_path = os.path.join(root, file)

            if Path(full_path).suffix in [".md", ".mdx"]:
                result = subprocess.run(
                     ["vale", "--output=JSON", full_path],
                     capture_output=True,
                     text=True)

                json_output = result.stdout
                json_list.append(json_output)

                result = subprocess.run(
                ["vale", "ls-metrics", full_path],
                capture_output=True,
                text=True)

                ls_metrics = result.stdout
                json_dic[json_output] = ls_metrics

    os.chdir(working_dir)
    score = aggregate_results(json_dic)
   #print_results(json_dic)
    return score


def prepare(temp_dir):
    source_vale_ini = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".vale-microsoft.ini")
    target_vale_ini = os.path.join(temp_dir, ".vale.ini")
    shutil.copyfile(source_vale_ini, target_vale_ini)

    styles_dir = os.path.join(temp_dir, "styles")
    os.makedirs(styles_dir, exist_ok=True)

    os.chdir(temp_dir)

    result = subprocess.run(
        ["vale", "sync"],
        capture_output=True,
        text=True
    )




