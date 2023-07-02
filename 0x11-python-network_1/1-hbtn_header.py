#!/usr/bin/python3
import urllib.request
import sys
"""Displays the value of the X-Request-Id variable"""

if __name__ == '__main__':
	url = sys.argv[1]
	with urllib.request.urlopen(url) as response:
        inf = response.info()
        print(inf.get('X-Request-Id'))
