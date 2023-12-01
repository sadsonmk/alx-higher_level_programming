#!/usr/bin/python3
"""this module takes in a URL and an email, sends a
    POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""


from urllib import request, parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    data = parse.urlencode(payload).encode()
    req = request.Request(url, data, method='POST')
    with request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(result)
