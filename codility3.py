def solution(A):
    # write your code in Python 3.6
    res = mincost(A);
    res = min(25, res)
    return res


def mincost(A):
    n = len(A)
    dl = [0 for i in range(n)]
    dl[0] = 0

    for i in range(1, n):
        od = 2 + dl[i - 1]
        bef = i - 1
        while bef >= 0 and A[bef] >= A[i] - 6:
            bef = bef - 1
        sd = 7
        if bef >= 0:
            sd = sd + dl[bef]

        dl[i] = min(od, sd)

    return dl[n - 1]

print(solution([1, 2, 4, 5, 7, 29, 30]))