#!/bin/bash

docker rm -f preview
docker build -t preview .
docker run -it preview
