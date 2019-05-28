n = int(input("Enter the number of transactions"))
price = [int(i) for i in input().split(" ")]
print(price)
t = [[0 for i in range(len(price))] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, len(price)):
        print("*",i, j)
        temp = 0
        for m in range(0, j):
            print(j, m)
            temp = max((price[j] - price[m])+t[i-1][m], temp)
            print(temp)
        t[i][j] = max(t[i][j-1], temp)






for x in t:
    print(x)
