from collections import defaultdict
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list)-> int:
        cache = defaultdict(dict)
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        def paths(i, j):
            if j >= m or i >= n:
                return 0
            if obstacleGrid[i][j] ==1:
                return 0

            if i in cache and j in cache[i]:
                return cache[i][j]

            if j==m-1 and i==n-1:
                return 1

            cache[i][j] =  paths(i+1, j) + paths(i, j+1)
            return cache[i][j]

        return paths(0, 0)

print(Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))