#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the body of the response"""

from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))

    except error.HTTPError as error:
        print(f"Error code: {error.code}")
