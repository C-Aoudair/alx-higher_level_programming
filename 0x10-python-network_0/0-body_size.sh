#!/usr/bin/bash
# Dispays the size of the body of the response get from server via URL
curl -sI "http://$1" | grep 'Content-Length.*' | sed 's/Content-Length: //'
