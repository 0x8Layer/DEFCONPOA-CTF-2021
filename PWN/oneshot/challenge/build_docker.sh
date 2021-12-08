#!/bin/bash

docker rm -f oneshot
docker build -t oneshot .
docker run -it oneshot
