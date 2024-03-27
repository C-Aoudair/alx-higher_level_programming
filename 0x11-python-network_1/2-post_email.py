#!/usr/bin/python3
""" sends a POST request to the passed URL with the email
as a parameter, and displays the body of"""

from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode('utf-8'))
