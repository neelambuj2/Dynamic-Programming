
class count:
    c=0
v= count()


def combs(string,  i,  l):
    if i>=l-1:
        v.c+=1
        return
    temp1 = string[i:i+1]
    b=i
    if i+1<l:
        if int(string[i+1])==0:
            b=i+1
    if int(temp1)<=26 and int(temp1)!=0:
        combs(string, b+1, l)
    temp2 =string[i:i+2]
    if i+1<l:
        if int(string[i+1])==0:
            return
    if int(temp2) <= 26 and int(temp2) != 0:
        combs(string, i+2,  l)








combs('2263',0,4)
print(v.c)