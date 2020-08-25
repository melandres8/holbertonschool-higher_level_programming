#!/usr/bin/python3
""" Headers with requests """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    header = requests.get(url).headers['X-Request-Id']
    print(header)
