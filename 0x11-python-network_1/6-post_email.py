#!/usr/bin/python3
""" sends a POST request to the passed URL with the email
as a parameter, and displays the body of"""

import requests
import sys


if __name__ == "__main__":
    r = request.post(sys.argv[1], data={'email': sys.argv[2])
    print(r.text)
