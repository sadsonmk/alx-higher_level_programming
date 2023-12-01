#!/usr/bin/python3
"""this is a module that takes 2 arguments and returns commits"""


import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/"
    response = requests.get(url)

    res = response.json()
    i = 0
    while i < 10:
        print("{}: {}".format(res.get('sha'),
                              res.get('commit').get('author').get('name')))
        i = i + 1
