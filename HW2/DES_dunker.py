#!/usr/bin/env python

### Author: Alex Dunker
### ECN: adunker
### HW: 2
### Filename: DES_dunker.py	
### Due Date: 01/28/2015

import sys
import string
from BitVector import *

# Expansion permutation (See Section 3.3.1):
expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 
9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 
20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

# P-Box permutation (the last step of the Feistel function in Figure 4):
p_box_permutation = [15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,
1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]

# Initial permutation of the key (See Section 3.3.6):
key_permutation_1 = [56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,
50,42,34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3]

# Contraction permutation of the key (See Section 3.3.7):
key_permutation_2 = [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,
7,15,6,26,19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,
33,52,45,41,49,35,28,31]

key_shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] 

###################################   S-boxes  ##################################

# Now create your s-boxes as an array of arrays by reading the contents
# of the file s-box-tables.txt:
arr = []
s_box = []
with open('s-box-tables.txt') as f:
    for line in f:
        if len(line) > 5:
            arr.append(line.split())
    for i in range(0,32, 4):
        s_box.append([arr[k] for k in range(i, i+4)])
f.close()

################################# Generate round keys  ########################

def create_keys(kBV):
    subkeys = []
    sBV = kBV.permute(key_permutation_1)
    for i in range(16):
        [left, right] = sBV.divide_into_two()
        left << key_shifts[i]
        right << key_shifts[i]
        tBV = left + right
        tBV = tBV.permute(key_permutation_2)
        subkeys.append(tBV)        
    return subkeys

########################### Encryption / Decryption ###########################

def des(encrypt_or_decrypt, input_file, output_file, key ):
    ## Get the key
    kBV = BitVector( filename = key )
    kBV = kBV.read_bits_from_file(64)
    ## Get the round keys
    rKeys = create_keys(kBV)
    ## Create the bitvector for readint in the file
    bv = BitVector( filename = input_file )
    ## Prepare output file
    FILEOUT = open( output_file, 'wb' )
    ## Use the more_to_read function to travers whole file
    while(bv.more_to_read):
        ## Read 64 bit block
        bitvec = bv.read_bits_from_file(64)
        ## Ensure that length is 64, if not pad
        if((bitvec.length() % 64) != 0):
            bitvec.pad_from_right(64-(bitvec.length() % 64))
        ## Use bitvector fucntion to split it into two
        [LE, RE] = bitvec.divide_into_two()
        ## Perform the 16 rounds of feistel
        for i in range(16):
            ## Place right in temp as it'll be the next left
            TEMP = RE
            ## Perform the expansion permutation
            RE = RE.permute(expansion_permutation)
            ## check if we're encrypting or decrypting
            if encrypt_or_decrypt == 0:
                RE = RE ^ rKeys[i] ## XOR with the roundkey
            elif encrypt_or_decrypt == 1:
                RE = RE ^ rKeys[15-i] ## reverse direction for decrypting
            ## Initialize a bit vector to use
            sBV = BitVector(size=0)
            ## Perform the s-box functions for all 8
            for j in range(8):
                r = 2*RE[6*j] + 1*RE[5+6*j]
                c = 8*RE[1+6*j] + 4*RE[2+6*j] + 2*RE[3+6*j] + 1*RE[4+6*j]
                sBV += BitVector(intVal = int(s_box[j][r][c]), size=4)
            ## Perform the p-permutation
            pBV = sBV.permute(p_box_permutation)
            ## Calculate the new right based of the left, and our f(RE,k)
            RE = LE ^ pBV
            ## Make the right the new left
            LE = TEMP
        ## Reverse the two and write it to the file
        bitvec = RE + LE
        FILEOUT.write(bitvec.get_text_from_bitvector())
        return(bitvec.get_text_from_bitvector())
    FILEOUT.close()

########################### MAIN ##############################################

if __name__ == "__main__":
    print("Encrypt / Decrypt function starting")
    des(0, "message.txt", "encrypted.txt", "key.txt")
    des(1, "encrypted.txt", "decrypted.txt", "key.txt")
    print("Complete.")
    
