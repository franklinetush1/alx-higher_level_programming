#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
		arg = sys.argv[1]
        with request.urlopen(arg) as resp:
            body = resp.read()
            print(body.decode('utf-8'))
    except error.HTTPError as exc:
        print('Error code: {}'.format(exc.code))
