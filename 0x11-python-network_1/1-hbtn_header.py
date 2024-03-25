#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displaysthe value
of the X-Request-Id variable found in the headerof the response."""

from urllib import request
import sys

with request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
