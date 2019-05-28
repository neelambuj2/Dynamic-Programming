from collections import defaultdict
string = input()
hash = defaultdict(lambda :0)

for i in string:
    hash[i] = hash[i]+1

for i in string:
    if hash[i]==1:
        print(i)
        break

