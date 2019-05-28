from functools import reduce
string = str(input())
length = len(string)

# for l in range(1,length+1):
#     for i in range(l):
#         temp = string[i:l]
#         if temp:
#             sum = sum + int(temp)
#
# print(sum%1000000007)
#
#
arr = list(string)
l = len(arr)
sum = 0
# sum = reduce(lambda x, y: int(x)+int(y), arr)

for i in range(0,l):
    mul = pow(10,i)
    for j in range(i):
        sum = sum+arr[]




