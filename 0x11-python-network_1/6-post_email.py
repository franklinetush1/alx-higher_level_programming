#!/usr/bin/python3
"""sends a POST request to the passed URL with the email"""
import requests
import sys


if __name__ == "__main__":
    arg = sys.argv[2]
    response = requests.post(sys.argv[1], data={'email': arg})
    print(response.text)
