#!/usr/bin/python3
"""a module that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys
if __name__ == '__main__':
    length = len(sys.argv)
    if length > 1:
        letter = sys.argv[1]
    else:
        letter = ''
    my_json = {"q": letter}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=my_json)
    try:
        result = response.json()
        if result == {}:
            print('No result')
        else:
            print(f"{[result.get('id')]} {result.get('name')}")
    except ValueError:
        print("Not a valid JSON")
