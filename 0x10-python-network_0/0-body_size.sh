#!/bin/bash

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  exit 1
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2 
