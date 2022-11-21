#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sort = 3
    while sort != 0:
        for row in range(n):
            prevrow = ((row -1) if row > 0 else 0)
            for column in range(m):
                if column == k:
                    #print(arr[prevrow][column], "    ",arr[row][column])
                    if arr[prevrow][column] > arr[row][column]:
                        ele = arr[prevrow]
                        arr[prevrow] = arr[row]
                        arr[row] = ele
                        break
        sort -=1
    for row in range(n):
        for column in range(m):
            print(arr[row][column], end = ' ')
        print()