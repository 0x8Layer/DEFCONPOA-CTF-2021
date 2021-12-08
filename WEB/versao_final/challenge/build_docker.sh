#!/bin/bash

docker rm -f versao_final
docker build -t versao_final .
docker run -it versao_final
