#!/usr/bin/env python3

### Author: Alex Dunker
### ECN: adunker
### HW: 3
### Filename: Dunker_Field.py	
### Due Date: 02/04/2016

import sys
import math

######################################################
# Function to check wheter a number is primte or not #
######################################################

def isPrime(num):
    # Check if number is two, return it is prime
    if (num == 2): return True
    #C heck if number is less than one, or divisible by two, return not prime
    if (num % 2 == 0) or (num <= 1): return False
    # Calculate the sqrt + 1 of the number to get the upper limit we have to check
    sqr = int(math.sqrt(num)) + 1
    # Move through and check all the numbers
    for div in range(3, sqr, 2):
        if num % div == 0: return False
    # If none found, it's prime
    return True


#################
# Main Function #
#################

def main():
    num = None

    # Take input for the number
    if sys.version_info[0] == 3:
        num = input("\nEnter number: ")
    else:
        num = raw_input("\nEnter number: ")
    num = int(num.strip())

    # Open the output file
    FILE = open("output.txt", 'w')

    # Check if it's prime, and output field or wring
    if isPrime(num):
        print("field")
        FILE.write("field")
    else:
        print("ring")
        FILE.write("ring")

    # Close output file
    FILE.close()

if __name__ == "__main__":
    main()
