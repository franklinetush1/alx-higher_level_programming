#!/bin/bash
# Check if the URL is provided as an argument
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f2
