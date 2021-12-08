#!/bin/bash

docker rm -f por_via_das_duvidas
docker build -t por_via_das_duvidas .
docker run -it por_via_das_duvidas
