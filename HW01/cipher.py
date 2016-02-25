#!/usr/bin/env python

"""
Author:        Alex Dunker
ECN:           adunker
Title:         HW1
Filename:      cipher.py
Description:   Reads an input from a file called 'input.txt' and writes to
               a file called 'output.txt'. Reads an encryption file called key
               'key.txt'. 
Date Created:  01/15/2016
"""


def encrypt(key, message):
    out = ""
    x = 0
    for symbol in message:
        out += chr(((ord(symbol)+ord(key[x])) % 26) + ord('A'))
        x += 1
        if x == len(key):
            x = 0
    return out

def letters(input):
    return ''.join(filter(str.isalpha, input))

def main():
    f = open('input.txt', 'r')
    inp = letters(f.read().upper())
    f = open('key.txt', 'r')
    key = f.read().strip().upper()
    out = encrypt(key, inp)
    f = open('output.txt', 'w')
    f.write(out)
    f.close()


main()
