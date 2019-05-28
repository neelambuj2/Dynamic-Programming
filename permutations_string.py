string = input()
a=list(string)
n=len(string)



def permutation(arr, s, e):
    if s==e:
        print(''.join(arr))
    else:
        for i in range(s, e+1):
            arr[i], arr[s] = arr[s], arr[i]
            permutation(arr, s+1, e)
            arr[i], arr[s] = arr[s], arr[i]


permutation(a,0,n-1)
