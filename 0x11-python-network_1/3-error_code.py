#!/usr/bin/python3
""" Error code, display body of the response """
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as r:
            r_data = r.read()
        print(r_data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
