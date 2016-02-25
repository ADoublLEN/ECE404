#!/usr/bin/env python3.4

### Author: Alex Dunker
### ECN: adunker
### HW: 6
### Filename: Dunker_breakRSA_hw06.py
### Due Date: 02/25/2016

from BitVector import *
from solve_pRoot import *
from Dunker_RSA_hw06 import *

def main():

    ## Generate 3 sets of public and private keys
    pub1, priv1, p1, q1, e = createKeys(3)
    pub2, priv2, p2, q2, e = createKeys(3)
    pub3, priv3, p3, q3, e = createKeys(3)

    ## Encrypt 1 file 3 times with each of the different public keys
    encrypted1 = encrypt("message.txt", pub1)
    encrypted2 = encrypt("message.txt", pub2)
    encrypted3 = encrypt("message.txt", pub3)

    ## Write these files out
    writeFile(encrypted1, "enc1.txt", True)
    writeFile(encrypted2, "enc2.txt", True)
    writeFile(encrypted3, "enc3.txt", True)

    ## Calculate N the product of all the values of n
    N = pub1[1] * pub2[1] * pub3[1]

    ## Caluclate Ni = N / ni
    N1 = N / pub1[1]
    N2 = N / pub2[1]
    N3 = N / pub3[1]

    ## Get BitVector representations of Ni and ni for use in BitVector multiplicative inverse
    bvM1 = BitVector(intVal = pub1[1])
    bvM2 = BitVector(intVal = pub2[1])
    bvM3 = BitVector(intVal = pub3[1])
    bv1 = BitVector(intVal = N1)
    bv2 = BitVector(intVal = N2)
    bv3 = BitVector(intVal = N3)

    ## Caluclate the multiplicative inverse of each Ni modulo ni
    C1 = int(bv1.multiplicative_inverse(bvM1))
    C2 = int(bv2.multiplicative_inverse(bvM2))
    C3 = int(bv3.multiplicative_inverse(bvM3))

    crackedBV = BitVector(size = 0)

    ## By CRT recover M^3 by the below equation
    for z in range(len(encrypted1)):
        x = (encrypted1[z] * N1 * C1 + encrypted2[z] * N2 * C2 + encrypted3[z] * N3 * C3) % N
        ## Recover M
        cINT = solve_pRoot(3, x)
        crackedBV += BitVector(intVal = cINT, size = 128)

    ## Write out the recovered file
    out = open("cracked.txt", 'wa')
    out.write(crackedBV.get_text_from_bitvector())

if __name__ == "__main__":
    main()