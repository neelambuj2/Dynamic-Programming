price = [int(i) for i in input().split(" ")]
n= len(price)
l = int(input())
t= [[0 for i in range(l+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,l+1):
        if j<i:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = max(price[i-1]+t[i][j-i],t[i-1][j])
print(t[n][l])