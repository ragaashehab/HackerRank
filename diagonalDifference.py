#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    rows = len(arr)
    columns = len(arr[0])
    d1= 0
    d2= 0
    for j in range(columns):
        for i in range(rows):
            if i == j:
                d1 += arr[i][j]
                
    for i in range(rows):
        for j in range(columns):        
            if (i+j == columns-1) :
                d2+= arr[i][j]
    
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()