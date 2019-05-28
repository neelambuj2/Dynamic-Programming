def combinations(array, sum_sofar ,sum):
    if sum_sofar>sum:
        return 0
    if sum_sofar == sum:
        return 1
    ways = 0
    for i in array:
        ways = ways + combinations(array,sum_sofar+i,sum)

    return ways

def combinationSum4(nums: list, target: int) -> int:
    memo = dict()

    def dfs(target):
        res = 0
        if target<0:
            return 0
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        for num in nums:
            res += dfs(target - num)
        memo[target] = res
        return res

    return dfs(target)


class Solution:
    cache = dict()

    def combinationSum4(self, nums: list, target: int) -> int:
        if target == 0:
            return 1
        if target in Solution.cache:
            return Solution.cache[target]
        ways = 0
        for i in nums:
            if target >= i:
                ways = ways + self.combinationSum4(nums, target - i)
        Solution.cache[target] = ways
        return Solution.cache[target]


array = [int(i) for i in input().rstrip().split()]
# #print(combinations(array, 0, 4))
# print(combinationSum4(array, 1))
print(Solution().combinationSum4(array,1))
