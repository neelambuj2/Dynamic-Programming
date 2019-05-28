seq = [int(i) for i in input().split(' ')]
l=len(seq)
for i in range(l):
    nge = -1
    for j in range(i+1,l):
        if seq[j]>seq[i]:
            nge = seq[j]
            break
    print(seq[i], ":", nge)
