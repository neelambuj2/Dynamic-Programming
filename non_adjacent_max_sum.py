n = int(input())
arr = [int(i) for i in input().split(" ")]
excl = 0
incl = arr[0]
for i in range(1,n):
    temp = incl
    if excl>=0:
        incl = max(excl+arr[i],incl)
    else:
        incl = max(arr[i],incl)
    excl = temp


print(max(incl,excl))
#negative number are handled