import sys
from copy import deepcopy

def find_max_min(arr):
    min = sys.maxsize
    max = -sys.maxsize
    minp = None
    maxp = None
    count = -1
    for i in arr:
        count=count+1
        if min>i[-1]:
            min = i[-1]
            minp = count
        if max <i[-1]:
            max = i[-1]
            maxp=count

    return max,min,maxp

def find_max_least(arr,key):
    temp=-1
    pos = None
    l=None
    count = -1
    for i in arr:
        count=count+1
        if i[-1]<key and i[-1]>temp:
            temp = i[-1]
            pos = count
            l=len(i)


    return pos,l

def run(arr,tt,n):
    for i in range(1,n):
        maxi,min, maxp = find_max_min(tt)
        if arr[i]<tt[0][0]:
            tt.insert(0,[arr[i]])

        elif arr[i]>maxi:
            temp = deepcopy(tt[maxp])
            temp.append(arr[i])
            tt.append(temp)

        else:
            pos,l = find_max_least(tt,arr[i])
            temp = deepcopy(tt[pos])
            temp.append(arr[i])
            tt.append(temp)
            count = -1
            for k in tt:
                count=count+1
                if len(k)==l+1:
                    del(tt[count])
                    break
    tplen = 0
    print(tt)
    for p in tt:
        print(len(p))
        tplen = max(tplen,len(p))

    print(tplen)

n = int(input())
#arr = [int(i) for i in input().split(" ")]
arr=[]
for g in range(n):
    arr.append(int(input()))
tt=[]
tt.append([arr[0]])
run(arr,tt,n)
