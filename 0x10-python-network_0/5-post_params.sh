#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -s -F "email=test@gmail.com" -F "subject=I will always be here for PLD" $1
