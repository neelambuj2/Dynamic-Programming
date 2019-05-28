def binary_search(arr, start ,end, ele):
    while start<=end:
        mid = int((start + end)/2)
        if arr[mid] == ele:
            return mid
        if arr[mid]<ele:
            start = mid+1
        if arr[mid]>ele:
            end = mid-1
    return -1

def infinite_search(arr, ele):
    end=1
    start = 0
    while arr[end]<ele:
        start = end
        end = end *2
    pos = binary_search(arr, start, end, ele)
    return pos

arr = [int(i) for i in input().rstrip().split(', ')]
x = int(input())
print("pos: ", infinite_search(arr,x))
