#!/bin/bash

docker rm -f simple_request
docker build -t simple_request .
docker run -it simple_request
