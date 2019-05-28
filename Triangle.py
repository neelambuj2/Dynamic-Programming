from collections import defaultdict
class Solution:
    def minimumTotal(self, triangle: list) -> int:
        l = len(triangle)
        cache = defaultdict(dict)
        def path(d,i):
            if d==l-1:
                return triangle[l-1][i]

            if d in cache and i in cache[d]:
                return cache[d][i]
            cache[d][i] = min(path(d+1,i), path(d+1,i+1)) + triangle[d][i]
            return cache[d][i]

        return path(0,0)


print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))