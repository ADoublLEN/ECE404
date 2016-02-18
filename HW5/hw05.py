#!/usr/bin/env python3.4

### Author: Alex Dunker
### ECN: adunker
### HW: 4
### Filename: hw05.py
### Due Date: 02/15/2016

import BitVector

class RC4:
    ## Initiali
    S = [i for i in range(256)]

    def __init__(self, key):
        self.key = key
        j = 0
        for i in range(256):
            j = (j + self.S[i] + ord(key[i % len(key)])) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def RC4(self,image):
        img = []
        if type(image[0]) is str:
            for char in image:
                img.append(ord(char))
        else:
            img = image

        tempS = self.S[:]

        i = 0
        j = 0
        byte = 0
        encrypt = []

        while True:
            i = (i + 1) % 256
            j = (j + tempS[i]) % 256
            tempS[i], tempS[j] = tempS[j], tempS[i]
            k = (tempS[i] + tempS[j]) % 256
            encrypt.append(tempS[k] ^ img[byte])
            byte += 1
            if byte == len(img):
                break

        return encrypt

    def encrypt(self, f):
        ## Handles the file objects and reads them and then passes them to the RC4 algorithm
        ## Then outputs the file to an "encryptedImage.ppm"
        data = f.read()
        encrypted = self.RC4(data)
        f = open("encryptedImage.ppm", 'w+b')
        f.write(bytearray(encrypted))
        return f

    def decrypt(self, f):
        ## Handles the file objects and reads them and then passes them to the RC4 algorithm
        ## Then outputs the file to an "decryptedImage.ppm"
        data = f.read()
        decrypted = self.RC4(data)
        f = open("decryptedImage.ppm", 'wba')
        f.write(bytearray(decrypted))
        return f

def main():

    ## Personal testing for HW 5. Outputs the images with their headers so you can view them
    rc4Cipher = RC4('keystring')
    image = "winterTown.ppm"
    with open(image, 'r') as f:
        data = f.readlines()
        header = data[0:3]
        img = data[3:]
    originalImage = "".join(img)
    encryptedImage = rc4Cipher.RC4(originalImage)

    with open("encrypted_"+image, 'wba') as out:
        for x in header[0:3]:
            out.write(x)
        out.write(bytearray(encryptedImage))

    decryptedImage = rc4Cipher.RC4(encryptedImage)
    with open("decrypted_"+image, 'wba') as out:
        for x in header[0:3]:
            out.write(x)
        out.write(bytearray(decryptedImage))



if __name__ == "__main__":
    main()
