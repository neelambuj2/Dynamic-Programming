
def cost1(B):
    l = len(B)
    diff = [[0,0] for i in range(l)]
    last1 = 1
    last2 = B[0]
    for i in range(1,l):
        diff1 = abs(B[i]-last1)
        diff2 = abs(1-last1)
        diff3 = abs(B[i] - last2)
        diff4 = abs(1 - last2)

        if diff1>=diff2:
            last1 = B[i]
            diff[i][0] = diff[i-1][0] + diff1
        else:
            last1 = 1
            diff[i][0] = diff[i-1][0] + diff2
        if diff3 >= diff4:
            last2 = B[i]
            diff[i][1] = diff[i - 1][1] + diff3
        else:
            last2 = 1
            diff[i][1] = diff[i - 1][1] + diff4

    return max(diff[l-1][0], diff[l-1][1])









if __name__ == '__main__':

    t = int(input())
    while(t> 0):
         n = int(input())
         B = list(map(int, input().rstrip().split(" ")))
         result = cost1(B)
         print(result)
         t=t-1
