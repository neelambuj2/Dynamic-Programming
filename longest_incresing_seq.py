l = []
l =[int(i) for i in input().split(" ")]
t= [1 for i in range(len(l))]
d= [1 for i in range(len(l))]
print(t)
for i in range(1, len(l)):
    for j in range(0, i):
        if l[j]<l[i]:
            t[i] = max(t[i], t[j]+1)

print(t)


for i in range(1, len(l)):
    for j in range(0, i):
        if l[j]>l[i]:
            d[i] = max(d[i], d[j]+1)

print(d)