#!/usr/bin/python3
"""This a module which uses the urllib module to fetch data from the web"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        result = resp.read()
        print("Body response:")
        print(f"\t- type: {type(result)}")
        print(f"\t- content: {result}")
        print(f"\t- utf8 content: {result.decode('utf-8')}")
