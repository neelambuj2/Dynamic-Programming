import copy
q = int(input())


for i in range(q):
    hash1 = copy.deepcopy(dict())
    hash2 = copy.deepcopy(dict())

    str1 = input()
    str2 = input()
    for c in str1:
        if c not in hash1:
            hash1[c]=1
        else:
            count = hash1[c]
            hash1[c] = count+1

    for c in str2:
        if c not in hash2:
            hash2[c] = 1
        else:
            count = hash2[(c)]
            hash2[c] = count + 1
    flag = True
    for key in hash2.keys():

        if hash1.get(key.lower(),0)+hash1.get(key.upper(),0)<hash2[key]:
            print("NO")
            flag = False
            break

    for key in hash1.keys():
        if flag ==False:
            break

        if key.isupper and key in hash2:
            if hash1[key]>(hash2.get(key.lower(),0)+hash2.get(key.upper(),0)):
                flag = False
                print("NO")
                break
        if key.isupper and key in hash2:
            if hash1[key] > hash2.get(key.upper(), 0):
                flag = False
                print("NO")
                break
        if key.isupper() and key not in hash2:
            flag = False
            print("NO")
            break

    if flag:
        print("YES")