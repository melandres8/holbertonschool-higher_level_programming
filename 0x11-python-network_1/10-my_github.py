#!/usr/bin/python3
""" My github """
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(username, password))
    print(req.json().get('id'))
