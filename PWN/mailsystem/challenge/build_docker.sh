#!/bin/bash

docker rm -r mailsystem
docker build -t mailsystem .
docker run -it mailsystem
