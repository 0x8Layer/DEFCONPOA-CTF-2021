#!/bin/sh

socat TCP-LISTEN:7002,reuseaddr,fork EXEC:"./mailsystem",su=root,pty,ctty,echo=0
