#!/usr/bin/env python

### Author: Alex Dunker
### ECN: adunker
### HW: 2
### Filename: DES_dunker.py	
### Due Date: 01/28/2015

import sys
import string
from BitVector import *

message = "0123456789ABCDEF"
key = "133457799BBCDFF1"

key_permutation_1 = [56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,
50,42,34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3]

key_permutation = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

key_shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] 

def create_keys(kBV):
    subkeys = []
    sBV = kBV.permute(key_permutation_1)
    for i in range(16):
        [left, right] = sBV.divide_into_two()
        left << key_shifts[i]
        right << key_shifts[i]
        
        

if __name__ == "__main__":
    mBV = BitVector( hexstring = message)
    kBV = BitVector( hexstring = key)
    print(mBV)
    print(kBV)
    create_keys(kBV)
