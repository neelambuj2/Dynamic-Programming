n = int(input())
arr=[]
arr = [int(i) for i in input().split(" ")]

for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)


table = [1 for i in range(n)]
for i in range(1,n):
    if arr[i]>arr[i-1]:
        table[i]=table[i-1]+1

table2 = [1 for i in range(n)]
for i in range(n-2,-1,-1):
    if arr[i]>arr[i+1]:
        table2[i]=table2[i+1]+1



table3=[]

for i in range(0,n):
    table3.append(max(table2[i],table[i]))

# print(table2)
# print(table3)
print(sum(table3))