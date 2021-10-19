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
    l = 0
    k = 0
    n = len(arr)
    m = n-1
    for i in range(n):
        print(i, 'i', arr[i][i])
        print(m, 'm', arr[i][m-i])
        l += arr[i][i]
        k += arr[i][m-i]
    
    a = k-l
    return a
        

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
