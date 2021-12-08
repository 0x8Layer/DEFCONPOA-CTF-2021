#!/bin/bash

docker rm -f another_xss
docker build -t another_xss .
docker run -it another_xss
