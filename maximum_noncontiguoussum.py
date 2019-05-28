l=[]
l=[int(i) for i in input().split(" ")]

excl = 0
incl = l[0]
for i in range(1,len(l)):
    temp = incl
    incl = max(excl+l[i],incl)
    excl = temp

print(max(incl, excl))



