# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    mini = sys.maxsize
    flag = False
    for i in A:
        if i > 0:
            flag = True
        mini = min(mini, i)

    if flag:
        while mini in A:
            mini += 1
        return mini
    else:
        return 1


print(solution([1, 3, 6, 4, 1, 2]))