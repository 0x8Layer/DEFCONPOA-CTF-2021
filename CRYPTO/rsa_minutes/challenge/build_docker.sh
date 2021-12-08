#!/bin/bash

docker rm -f rsa_minutes
docker build -t rsa_minutes .
docker run -it rsa_minutes
