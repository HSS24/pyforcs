#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By 

import base64

def encode_data(pl_txt):
    pl_txt = pl_txt.encode()
    cphr_txt = base64.b64encode(pl_txt)
    cphr_txt = cphr_txt.decode()
    return cphr_txt
def decode_data(cphr_txt):
    pl_txt = base64.b64decode(cphr_txt)
    pl_txt = pl_txt.decode()
    return pl_txt

method = input("do you wish to encode or decode (e/d)? ").lower()
msg = input("what is the message? ")

if method[0] == "e":
    print(encode_data(msg))
elif method[0] == "d":
    print(decode_data(msg))
else:
    print("wrong method selected. choose e/d")   