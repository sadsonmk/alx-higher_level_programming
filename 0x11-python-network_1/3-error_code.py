#!/usr/bin/python3
"""a module that takes in a URL, sends a request to
    the URL and displays the body of the response (decoded in utf-8).
"""


import urllib
from urllib import request
import sys
if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            result = response.read().decode()
            print(result)
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
