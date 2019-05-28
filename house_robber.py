class Solution:
    def rob(self, nums) -> int:
        l = len(nums)
        cache = dict()
        cache2 = dict()
        if l==1:
            return nums[0]
        def loot1(i: int):
            if i>=l:
                return 0
            if i in cache:
                return cache[i]
            if i==l-1:
                return nums[i]
            current_money = loot1(i+1)
            adjacent_money = nums[i] + loot1(i+2)
            cache[i] = max(current_money,adjacent_money)
            return max(current_money, adjacent_money)

        def loot2(i: int):
            if i >=l-1:
                return 0
            if i in cache2:
                return cache2[i]
            if i == l - 2:
                return nums[i]
            current_money = loot2(i + 1)
            adjacent_money = nums[i] + loot2(i + 2)
            cache2[i] = max(current_money, adjacent_money)
            return max(current_money, adjacent_money)

        return max(loot1(1),loot2(0))
print(Solution().rob([1]))