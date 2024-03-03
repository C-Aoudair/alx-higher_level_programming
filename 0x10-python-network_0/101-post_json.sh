#!/bin/bash
# Sends a JSON request with the contents of a file.
curl -sX POST -d @"$2" -H "Content-Type: application/json" $1
