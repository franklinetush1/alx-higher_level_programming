#!/usr/bin/python3
"""Fetches an URL with requests package"""
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    txt = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(txt), txt))
