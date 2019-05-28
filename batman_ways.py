from collections import defaultdict
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        ways = 0

        def dfs_ways(i,dist,cache):
            if dist == A-1:
                return 1
            if i in cache and dist in cache[i]:
                  return cache[i][dist]
            next_ways = 0
            for num in range(1, B + 1):
                if co_prime(num, i):
                    if i in cache and dist in cache[i]:
                        next_ways = next_ways + cache[i][dist]
                    else:
                        next_ways = next_ways + dfs_ways(i, dist+1, cache)
            cache[dist][i] = next_ways
            return next_ways

        def co_prime(num, i):
            min_range = min(num, i)
            for k in range(2, min_range + 1):
                if num % k == 0 and i % k == 0:
                    return False
            else:
                return True

        for num in range(1, B + 1):
            cache = defaultdict(dict)
            ways = ways + dfs_ways(num,0,cache)

        return ways % 1000000007

print(Solution().solve(6,96))