def substrings(n):
    MOD = 1000000007
    sum = 0
    sumMemo = {}
    prev = 0
    for i in range(len(n)):
        sum *= 10
        prev += int(n[i])*(i+1)
        sum += prev
    return sum


a = substrings('123')
print(a)


