#!/usr/bin/env python3.4

### Author: Alex Dunker
### ECN: adunker
### HW: 4
### Filename: hw05.py
### Due Date: 02/15/2016

import BitVector

class RC4:
    S = [i for i in range(256)]

    def __init__(self, key):
        self.key = key
        j = 0
        for i in range(256):
            j = (j + self.S[i] + ord(key[i % len(key)])) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def encrypt(self, image):
        img = []
        with open(image, 'r') as f:
            data = f.readlines()
            for i in range(3, len(data)):
                for j in range(len(data[i])):
                    img.append(ord(data[i][j]))

        encryptS = self.S[:]

        i = 0
        j = 0
        byte = 0
        encrypt = []

        while True:
            i = (i + 1) % 256
            j = (j + encryptS[i]) % 256
            encryptS[i], encryptS[j] = encryptS[j], encryptS[i]
            k = (encryptS[i] + encryptS[j]) % 256
            encrypt.append(encryptS[k] ^ img[byte])
            byte += 1
            if byte == len(img):
                break

        with open("encrypted_"+image, 'wba') as out:
            for x in data[0:3]:
                out.write(x)
            out.write(bytearray(encrypt))
        out.close()
        return encrypt

    def decrypt(self, image):
        return self.encrypt(image)
