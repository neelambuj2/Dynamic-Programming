from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = defaultdict(dict)
        def paths(i, j):

            if i in cache and j in cache[i]:
                return cache[i][j]

            if j>=m or i>=n:
                return 0

            if j==m-1 and i==n-1:
                return 1

            cache[i][j] =  paths(i+1, j) + paths(i, j+1)
            return cache[i][j]

        return paths(0, 0)

print(Solution().uniquePaths(23,12))