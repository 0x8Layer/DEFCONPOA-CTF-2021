#!/bin/sh

socat TCP-LISTEN:6000,reuseaddr,fork EXEC:"python3 app.py",su=root,pty,echo=0
