
import math
import sys
class Solution:
    def numSquares(self, n: int, cache = {0: 0, 1: 1}) -> int:
        if n in cache:
            return cache[n]
        length = n
        limit = int(math.sqrt(n))
        for j in range(2, limit+1):
            rem = n - (j*j)
            count = self.numSquares(rem, cache)+1
            length = min(length, count)
        cache[n] = length
        return length

# class Solution(object):
#
#     def numSquares(self, n, n_sqs={0: 0, 1: 1}):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n in n_sqs:
#             return n_sqs[n]
#
#         sqrt_n = int(n ** .5)
#         min_count = n
#         for i in range(2, sqrt_n + 1):
#             count = self.numSquares(n - i * i, n_sqs) + 1
#             min_count = min(count, min_count)
#
#         n_sqs[n] = min_count
#         return min_count

print(Solution().numSquares(6))