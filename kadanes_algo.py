
def maxSubArray(A):
    max_so_far = 0
    max_here = 0
    flag = False
    subseq_sum = 0

    for i in A:
        if i > 0:
            subseq_sum+=i
            flag = True
        if max_here + i > 0:
            max_here = max_here + i
        else:
            max_here = 0
        max_so_far = max(max_so_far, max_here)

    if flag:
        return max_so_far, subseq_sum
    else:
        max_ele = max(A)
        return max_ele, max_ele


t = int(input())

while t > 0:
    n = int(input())
    A = list(map(int, input().rstrip().split(' ')))
    subarray_sum, sub_sequence_sum = maxSubArray(A)
    print(subarray_sum, sub_sequence_sum)
    t=t-1