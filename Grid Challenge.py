#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    rows = len(grid)
    columns = len(grid[0])
    
    for i in range(rows):
        templst = []
        newgrid = [[0]*5 for i in range(5)]
        for j in range(columns):
            templst.append(grid[i][j])
            templst = sorted(templst)
        for j1 in range(columns):
            newgrid[i][j1] = templst[j1]
    for j2 in range(columns):
        templst = []
        for i2 in range(rows):
            templst.append(grid[i2][j2])
        if (templst != sorted(templst)):
            return "NO"
    return "YES"
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
