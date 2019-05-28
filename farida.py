
t = input("")
t=int(t)
for k in range(t):
    n = input("")
    n = int(n)
    arr = [int(i) for i in input().rstrip().split(" ")]
    l = len(arr)
    even_sum = 0
    odd_sum = 0
    for i in range(0,l, 2):
        even_sum = even_sum + arr[i]
    for j in range(1,l,2):
        odd_sum = odd_sum+arr[j]

    print("Case ", k+1, ":", max(even_sum,odd_sum))
