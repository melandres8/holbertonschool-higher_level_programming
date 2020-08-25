#!/usr/bin/python3
""" Error code """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print(req.status_code)
    else:
        print(req.text)
