
t = int(input())





def restore(n,p):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if len(p)==0:
        return -1

    if max(p)>26:
        return -1
    if p[0] != 1:
        return -1
    for i in range(1,n):
        if p[i]-p[i-1] not in[0,1]:
            return -1
    string='a'
    for i in range(1, n):
        string = string + chars[p[i]-1]
    return string

while t > 0:
    n = int(input())
    p = [int(i) for i in input().split(" ")]
    print(restore(n,p))
    t = t - 1