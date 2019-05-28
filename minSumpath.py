from collections import defaultdict
import sys
class Solution:
    def minPathSum(self, grid: list) -> int:
        cache = defaultdict(dict)
        n = len(grid)
        m = len(grid[0])
        def paths(i, j):
            if j >= m or i >= n:
                return sys.maxsize
            if i in cache and j in cache[i]:
                return cache[i][j]
            if j==m-1 and i ==n-1:
                return grid[i][j]
            if cache[i].get(j) is None:
                cache[i][j] = min( paths(i+1,j), paths(i,j+1))+grid[i][j]
                return cache[i][j]


        return paths(0, 0)

print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))