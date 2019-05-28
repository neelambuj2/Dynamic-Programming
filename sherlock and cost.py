 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    l = len(B)
    diff = [0 for i in range(l)]
    i=1
    max_value2 = B[i]
    max_value1 = B[i-1]
    diff1 = abs(1- max_value2)
    diff2 = abs(max_value1-1)
    if diff1>=diff2:
        diff[i-1] = 1
        diff[i] = max_value2
    else:
        diff[i-1] = max_value1
        diff[i] = 1

    for i in range(2,l):
        temp1 = abs(B[i]-diff[i-1])
        temp2 = abs(1-diff[i-1])
        if temp1>=temp2:
            diff[i] = B[i]
        else:
            diff[i] = 1


    max_diff = 0
    print(diff)
    for i in range(1,l):
        max_diff = max_diff + abs(diff[i]-diff[i-1])
    return max_diff

def cost1(B):
    l = len(B)
    max_diff_so_far = 0
    diff = list()
    for i in range(1,l):
        diff1 = abs(B[i]-1)
        diff2 = abs(B[i-1] -1)
        diff3 = abs(B[i]-B[i-1])

        if diff1 >= diff2 and diff1 >= diff3:
            diff.append()



if __name__ == '__main__':

    t = int(input())
    while(t> 0):
     n = int(input())
     B = list(map(int, input().rstrip().split(" ")))
     result = cost1(B)
     print(result)
     t=t-1
