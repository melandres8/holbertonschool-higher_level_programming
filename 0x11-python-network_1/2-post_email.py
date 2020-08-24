#!/usr/bin/python3
""" Post an email """
import urllib.parse
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    values = {
        'email': email,
    }

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        response_data = response.read()
    print(response_data.decode('utf-8'))
