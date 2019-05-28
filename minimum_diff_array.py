#o(n2) approach
import sys
def maxm_diffrence(arr, n):
    diff = [sys.maxsize for i in range(n)]
    for i in range(n):
        for j in range(i):
            d = abs(arr[i]-arr[j])
            if d<diff[i]:
                diff[i] = min(d, diff[i])
    print(min(diff))

n = int(input())
arr = [int(i) for i in input().split(" ")]
maxm_diffrence(arr, n)

def maximum_difference(arr, n):
    arr.sort()
    diff = sys.maxsize
    for i in range(n-1):
        diff = min(abs(arr[i]-arr[i+1]), diff)

    print(diff)

