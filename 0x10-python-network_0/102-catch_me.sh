#!/bin/bash
# Script that makes a request to illicit a given response
curl -s -L -X PUT -d user_id=98 0.0.0.0:5000/catch_me
