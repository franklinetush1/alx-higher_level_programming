#!/bin/bash
# Script that sends a request to a URL 
curl -so /dev/null -w "%{http_code}" "$1"
