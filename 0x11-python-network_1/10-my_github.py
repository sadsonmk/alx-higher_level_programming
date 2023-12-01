#!/usr/bin/python3
"""this module takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    authenticate = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=authenticate)
    result = response.json()
    print(result.get('id'))
