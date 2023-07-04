#!/usr/bin/python3
"""Fetches an URL with requests package"""
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    txt = response.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
