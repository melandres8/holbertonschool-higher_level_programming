#!/usr/bin/python3
""" Post an email """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    req = requests.post(url, data = {'email': email})
    print(req.text)
