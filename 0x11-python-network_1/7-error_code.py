#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    status = r.status_code
    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(r.text)
