#!/bin/sh

socat TCP-LISTEN:7000,reuseaddr,fork EXEC:"./easyfl0w",su=root,pty,ctty,echo=0
