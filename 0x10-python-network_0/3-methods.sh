#!/bin/bash
# Displays all http methods the server will accept
curl -sI $1 | grep Allow | cut -d " " -f2
