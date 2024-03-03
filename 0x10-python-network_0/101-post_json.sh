#!/bin/bash
# Sends a JSON request with the contents of a file.
curl -sX POST -d @"$2" $1
