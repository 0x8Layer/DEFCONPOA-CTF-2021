import json
import logging
import socketserver
import threading
import datetime
import time
import sys
from Crypto.Util.number import bytes_to_long, getPrime

old = {}
p = 0
flag = "DC5551{b4by_r$4_4fun}"

def encodeRSA(p):
    q = getPrime(1024)
    n = p*q
    e = 65537

    c = pow(int(flag.encode("utf-8").hex(), 16), e, n)
    return json.loads('{"c":'+str(c)+', "e":'+str(e)+', "n":'+str(n)+' }')

def isPrime(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def chall():
    minute = datetime.datetime.now().minute
    
    if isPrime(minute):
        p = minute
        old = encodeRSA(p)
        return old, p
    else:
        return False, False

def main():
    minute_previous = 0
    challenge_previous = {}
    while True:
        challenge, minute = chall()
        if challenge is False or minute == minute_previous:
            continue
        print(challenge)
        minute_previous = minute
        challenge_previous = challenge


if __name__ == "__main__":
    main()
