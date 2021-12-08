#!/bin/bash
docker rm -f sql2
docker build -t sql2 . && \
docker run --name=sql2 --rm -p 5007:5007 -p 3306:3306 --detach -it sql2
