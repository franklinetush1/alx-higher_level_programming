#!/usr/bin/python3
"""Python script that uses the GitHub API to show user id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    APIurl = 'https://api.github.com/user'
    auth = HTTPBasicAuth(user, password)
    response = requests.get(APIurl, auth=auth)
    print(response.json().get('id'))
