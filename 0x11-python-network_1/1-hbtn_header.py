#!/usr/bin/python3
""" displays the value of the X-Request-Id
    variable found in the header of the response. """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
    print(header)
