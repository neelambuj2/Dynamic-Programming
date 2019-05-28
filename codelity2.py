def solution(T):
    n = len(T)
    for i in range(0, n):
        if i == T[i]:
            cap = i
    dl = [0 for i in range(n-1)]
    for i in range(n):
        if i==cap:
            continue
        j=i
        dist = 0
        while(T[j]!=cap):
            k=T[j]
            dist = dist+1
            j=k
        dl[dist] = dl[dist]+1
    return dl
print(solution([1, 1]))