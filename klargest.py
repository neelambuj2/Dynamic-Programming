t = (input())
while (t):
    n, k = input().split(" ")
    # n = int(n)
    # k = int(k)
    # t = int(t)
    l1 = [i for i in input().split(' ')]
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    l1.sort()
    temp = len(l1)
    res = l1[temp-k:]

    for x in range(len(res)):
        print(res[x], end=" ")
    print("\n")
    t = t - 1