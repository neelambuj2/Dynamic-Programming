
def printNGE():
    arr = [int(i) for i in input().split(' ')]
    nge = list()
    s=[]

    for i in range(len(arr)-1,-1,-1):
        print(s, arr[i])
        if bool(s)==True:
            while(bool(s) and s[len(s)-1]<=arr[i]):
                s.pop()

        nge.insert(0,s[len(s)-1] if bool(s) else -1)
        s.append(arr[i])


    for i in range(0,len(arr)):
        print(arr[i],"->",nge[i])


printNGE()
