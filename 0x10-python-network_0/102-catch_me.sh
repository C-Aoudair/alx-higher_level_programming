#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sL -X PUT -d "name=no-name" -H "Origin: alx-se" 0.0.0.0:5000/catch_me
