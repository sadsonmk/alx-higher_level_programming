#!/usr/bin/python3
"""This a module which uses the urllib module to fetch data from the web"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        result = resp.read()
        print('Body reponse:')
        print('\t- type: {}'.format(type(result)))
        print('\t- content: {}'.format(result))
        print('\t- utf8 content: {}'.format(result.decode('utf-8')))
