#!/bin/bash
# Displays only the status code of the response.
curl -sI "$1" | awk '/1.0/{print $2}'
