#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    openlist = ["{","(","["]
    closelist =["}",")","]"]
    eid =[]
    for e in s:
        if e in openlist:
            eid.append(openlist.index(e))
        elif e in closelist:
            if closelist.index(e)== eid[-1]:
                eid.pop()
            else:
                return "NO"
    if len(eid)==0:
        return "YES"
    return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
