#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""

import requests
import sys


if __name__ == "__main__":

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url, params={'per_page': 10})

    if r.status_code == 200:
        commits = r.json()
        for commit in commits:
            commit_sha = commit['sha']
            authorName = commit['commit']['author']['name']
            print(f"{commit_sha}: {authorName}")
