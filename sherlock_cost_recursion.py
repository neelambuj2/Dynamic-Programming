from copy import deepcopy

def cost1(B,i, l,lookup):
    if i==l:
        max_diff = 0
        for j in range(1, l):
            max_diff = max_diff + abs(B[j] - B[j - 1])
        return max_diff

    replace1 = deepcopy(B)
    replace1[i] = 1
    if str(replace1) in lookup:
        diff1 = lookup[str(replace1)]
    else:

        diff1 = cost1(replace1,i+1,l, lookup)
        lookup[str(replace1)] = diff1

    replacei = deepcopy(B)
    replacei[i] = B[i]
    if str(replacei) in lookup:
        diff2 = lookup[str(replacei)]
    else:
        diff2 = cost1(replacei, i + 1, l, lookup)
        lookup[str(replacei)] = diff2


    return max(diff1, diff2)











if __name__ == '__main__':

    t = int(input())
    while(t> 0):
     n = int(input())
     B = list(map(int, input().rstrip().split(" ")))
     result = cost1(B, 0, len(B),{})
     print(result)
     t=t-1
