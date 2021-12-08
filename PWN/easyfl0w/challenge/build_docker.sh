#!/bin/bash

docker rm -r easyflow
docker build -t easyflow .
docker run -it easyflow
