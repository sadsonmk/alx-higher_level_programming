#!/bin/bash
# sends a JSON POST request to a URL passed as arg and displays the response.
curl -s -X POST $1 -H "Content-Type: application/json" -d @$2
