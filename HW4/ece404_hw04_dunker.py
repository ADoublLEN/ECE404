#!/usr/bin/env python3

### Author: Alex Dunker
### ECN: adunker
### HW: 4
### Filename: ece404_hw04_dunker.py
### Due Date: 02/05/2016

message = "plaintext.txt"
encout = "encryptedtext.txt"
decout = "decryptedtext.txt"

KEY = "howtogettosesame"

from BitVector import *

def roundKeys(key):
    tmp = BitVector(textstring = key)
    RK = BitVector(textstring = key)
    #for i in range(10):
    #    temp = RoundKey(

def AES_enc(key, message, fileout):
    keys = roundKeys(key)
    return True

def AES_dec(key, message, fileout):
    return True

def main():
    kBV = BitVector( textstring = KEY )
    mBV = BitVector( filename = message )
    ENCOUT = open(encout, 'wb')
    DECOUT = open(decout, 'wb')

    while(mBV.more_to_read):
        bitvec = mBV.read_bits_from_file(128)


if __name__ == "__main__":
    main()