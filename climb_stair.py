class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()

        def unique_ways(n):
            if n<0:
                return 0
            if n in cache:
                return cache[n]

            if n ==0:
                return 1
            cache[n] = unique_ways(n-1)+ unique_ways(n-2)
            return cache[n]

        return unique_ways(n)

print(Solution().climbStairs(3))