#!/bin/bash
# Displays only the status conde of the response got from a get request.
curl -s -o /dev/null -w "%{http_code}" $1
