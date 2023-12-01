#!/usr/bin/python3
"""This a module which uses the urllib module to fetch data from the web"""


from urllib import request
if __name__ == '__main__':
    resp = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(resp) as response:
        result = response.read()
    print('Body reponse:')
    print(f'\t- type: {type(result)}')
    print(f'\t- content: {result}')
    print(f'\t- utf8 content: {result.decode("utf-8")}')
