#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    args = {'email': sys.argv[2]}
    data = parse.urlencode(args).encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
