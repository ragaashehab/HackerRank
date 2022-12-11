#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr= sorted(arr)
    minsum= sum(arr)- arr[len(arr)-1]
    maxsum= sum(arr)-arr[0]
    return print(minsum , maxsum)
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
