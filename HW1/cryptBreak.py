#!/usr/bin/env python

### Author: Alex Dunker
### ECN: adunker
### HW: 1
### Filename: cryptBreak.py	
### Due Date: 01/21/2016

import sys
import itertools
import string
from BitVector import *

if len(sys.argv) is not 2:
    sys.exit('''Needs one command line argument for the encrypted input''')

def decrypt(encrypted_bv, key):
    PassPhrase = "Hopes and dreams of a million years"
    BLOCKSIZE = 16
    numbytes = BLOCKSIZE // 8
    # Reduce the passphrase to a bit array of size BLOCKSIZE:
    bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)
    for i in range(0,len(PassPhrase) // numbytes):
        textstr = PassPhrase[i*numbytes:(i+1)*numbytes]
        bv_iv ^= BitVector( textstring = textstr )
    # Reduce the key to a bit array of size BLOCKSIZE:
    key_bv = BitVector(bitlist = [0]*BLOCKSIZE)
    key_bv  = BitVector(bitstring = key)
    # Create a bitvector for storing the decrypted plaintext bit array:
    msg_decrypted_bv = BitVector( size = 0 )
    # Carry out differential XORing of bit blocks and decryption:
    previous_decrypted_block = bv_iv
    for i in range(0, len(encrypted_bv) // BLOCKSIZE):
        bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
        temp = bv.deep_copy()
        bv ^=  previous_decrypted_block
        previous_decrypted_block = temp
        bv ^=  key_bv
        msg_decrypted_bv += bv
    # Extract plaintext from the decrypted bitvector:    
    return msg_decrypted_bv.get_text_from_bitvector()

def iterations(charset, maxlength):
    #returns all permutations of inputted charset all length 16
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=16)
        for i in range(1, maxlength + 1)))
    
def main():
    print "BEGIN"
    # Create a bitvector from the ciphertext hex string:
    FILEIN = open(sys.argv[1])
    # Read in the input file (encrypted.txt)
    encrypted_bv = BitVector( hexstring = FILEIN.read() )
    # Loop through all the combinations in the keyspace
    for i, attempt in enumerate(iterations("01", 16)):
        # Decrypt with the attempt
        out =  decrypt(encrypted_bv, attempt)
        # Check if attempt works
        if(out.find("funerals") != -1):
            print "Decrypted text: ",out
            print "Key: ",attempt
            break
    print "COMPLETE"
 
main()
