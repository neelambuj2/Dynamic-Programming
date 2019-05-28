str1 = input()
str2 = str1[::-1]
l1 = len(str1)
l2 = len(str2)
t= [[None for i in range(l1+1)] for j in range(l2+1)]


for i in range(l2+1):
    for j in range(l1+1):
        if i == 0 or j == 0:
            t[i][j] = 0
        elif str1[j-1] == str2[i-1]:
            t[i][j] = t[i-1][j-1] + 1
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])

for r in t:
    print(r)

i = l2
j = l1
lcs = ''
while i > 0 and j > 0:
    if str2[i-1] == str1[j-1]:
        lcs = lcs + str2[i-1]
        i = i-1
        j = j-1
    elif t[i-1][j]>t[i][j-1]:
        i = i-1
    else:
        j = j-1

print(lcs)

