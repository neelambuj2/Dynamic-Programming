#!/bin/python3

import math
import os
import random
import re
import sys
import copy
# Complete the countArray function below.
def countArray(i,n, k, x, d, path):
    path.append(i)
    if i==x and d==n:
        print(path)
        return 1
    if d==n and i!=x:
        return 0
    count = 0
    for j in range(1,k +1 ):
        if j!=i:
            count = count +countArray(j,n,k,x,d+1,copy.deepcopy(path))
    return count

    # Return the number of ways to fill in the array.

if __name__ == '__main__':

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(1, n, k, x,1,[])
    print(answer%(1000000007))

