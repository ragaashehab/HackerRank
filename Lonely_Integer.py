#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    temp = {}
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j) and (a[i]==a[j]):
                temp[i] = a[i]
                temp[j] = a[j]
    for i in range(len(a)):
        if temp.get(i) is None:
            return a[i]
    
        
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
