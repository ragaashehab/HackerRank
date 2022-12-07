#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    out = ""
    for e in s:
        if e.isalpha():
            if e.isupper() and (ord(e) + k) > ord('Z'):
                out+= chr((ord(e) + k)% ord('Z'))
            elif e.islower() and ((ord(e) + k) > ord("z")):
                out+= chr((ord(e) + k) % ord('z'))
            else:  
                out += chr(ord(e)+ k)
        else:
            out += e
    return out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
