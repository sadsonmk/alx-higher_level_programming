#!/usr/bin/python3
"""a module that fetches https://alx-intranet.hbtn.io/status using requests
"""


import requests
if __name__ == '__main__':
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(result.text)}")
    print(f"\t- content: {result.content.decode('utf-8')}")
