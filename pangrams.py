#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    alpha = string.ascii_lowercase
    for e in alpha:
        if e not in s:
            return "not pangram"
    return "pangram"                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
