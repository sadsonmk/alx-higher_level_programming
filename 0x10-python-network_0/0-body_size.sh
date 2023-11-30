#!/bin/bash
# displays the size of the body of the response from a URL
curl -Is $1 | grep Content-Length | cut  -d ':' -f 2- | sed 's/ //g'
