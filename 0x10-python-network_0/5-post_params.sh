#!/bin/bash
# Sends a POST request to a URL with variables
curl -sX POST -d "email=5-post_params.sh&subject=I will always be here for PLD" $1
