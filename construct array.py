#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countArray function below.
def countArray(n, k, x):
    a = [0 for i in range(n+1)]
    b = [0 for i in range(n+1)]
    a[0] = 1 if x == 1 else 0
    b[0] = 0 if x == 1 else 1


    for i in range(1, n):
        print('*')
        a[i] = b[i - 1]%(1000000007)
        b[i] = (a[i - 1] * (k - 1) + b[i - 1] * (k - 2))%(1000000007)
        print(a)
        print(b)

    return a[n - 1]

    # Return the number of ways to fill in the array.


if __name__ == '__main__':
    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)
    print(answer)

