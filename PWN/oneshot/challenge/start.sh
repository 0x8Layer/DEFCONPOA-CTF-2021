#!/bin/sh

socat TCP-LISTEN:7001,reuseaddr,fork EXEC:"./oneshot",su=root,pty,ctty,echo=0
