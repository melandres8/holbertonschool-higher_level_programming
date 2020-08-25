#!/usr/bin/python3
""" Script that takes in a letter and sends
    a POST request to url with the letter as
    a parameter. """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ''
    url = 'http://0.0.0.0:5000/search_user'
    data {
        'q': q,
    }
    req = requests.post(url, data=data)
    try:
        data = req.json()
        if not data:
            print('Not result')
        else:
            print('[{}] {}'.format(data['id'], data['name']))
    except Exception:
        print('Not a valid JSON')
