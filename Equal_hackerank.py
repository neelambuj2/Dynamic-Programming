#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    minm_oper = sys.maxsize
    minm_choc = min(arr)
    for i in range(minm_choc,minm_choc-5,-1):
        oper = 0
        for choc in arr:
            x = choc - i
            oper = oper + int(x / 5) + int((x % 5)/2) + (x % 5) % 2
        if oper < minm_oper:
            minm_oper = oper

    return minm_oper


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)
        print(result)

