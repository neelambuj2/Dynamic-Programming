import math
import sys
class Solution:
    cache = dict()
    def integerBreak(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]

        max_prod = 1
        for i in range(2,n):
            prod = max(i*(n-i), i * self.integerBreak(n-i))
            max_prod = max(max_prod, prod)
            Solution.cache[n] = max_prod

        return max_prod


temp = Solution().integerBreak(4)
print(temp)