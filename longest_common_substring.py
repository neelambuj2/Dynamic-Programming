from copy import deepcopy
str1 = input()
str2 = input()

l1 = len(str1)
l2 = len(str2)

ans = 0
row = None
col = None
t= [[0 for i in range(l2+1)] for j in range(l1+1)]
for r in range(1,l1+1):
    for c in range(1,l2+1):
        if str1[r-1]==str2[c-1]:
            temp = ans
            ans = max(t[r-1][c-1]+1, ans)
            if temp!=ans:
                row = r
                col = c
            t[r][c] = t[r-1][c-1]+1
        else:
            t[r][c] = 0

while t[row][col]!=0:
    print(str1[row-1], end=" ")
    row-=1
    col-=1
