#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the body of the response"""

from urllib import request
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decoded('utf-8'))

    except request.error.HTTPError as error:
        print(f"Error code: {error.code}")
