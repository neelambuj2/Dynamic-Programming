from copy import  deepcopy
arr = [int(i) for i in input().split(" ")]
wt = int(input())

total = sum(arr)
i=0
def get_subset(arr,so_far, rem, wt, i, path ):



    if so_far > wt:
        return 'leave'
    elif so_far+rem < wt:
        return False
    elif so_far==wt:
        return True
    elif rem == 0:
        return False
    elif get_subset(arr, so_far+arr[i], rem - arr[i], wt, i+1, path) is True:
        path.append(arr[i])
        return True
    elif get_subset(arr, so_far, rem - arr[i], wt, i+1, path) is True:
        return True
    return False

path =[]

print(get_subset(arr,0,total,wt,0,path))
print(path)