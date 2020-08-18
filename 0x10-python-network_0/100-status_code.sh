#!/bin/bash
# Displays only the status code of the response.
curl -so /dev/null -Iw "%{http_code}" "$1"
