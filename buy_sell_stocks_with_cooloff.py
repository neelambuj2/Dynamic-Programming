from collections import defaultdict
class Solution:
    def maxProfit(self, prices: list) -> int:
        l = len(prices)
        cache = defaultdict(dict)
        cache2 = defaultdict(dict)
        def transaction(n, k, bflag):

            if n >= l:
                return 0
            if k >=1:
                return 0
            if n in cache and bflag in cache[n]:
                return cache[n][bflag]
            if bflag:
                sell = transaction(n+1, k+1, False) + prices[n]
                not_sell = transaction(n+1,k,bflag)
                cache[n][bflag] = max(sell, not_sell)
                return max(sell, not_sell)
            else:
                buy = transaction(n+1,k, True) - prices[n]
                not_buy = transaction(n+1,k, False)
                cache[n][bflag] = max(buy, not_buy)
                return max(buy, not_buy)

        def transaction2(n, k, bflag):

            if n >= l:
                return 0
            if k >= 2:
                return 0
            if n in cache2 and bflag in cache2[n]:
                return cache2[n][bflag]
            if bflag:
                sell = transaction(n + 1, k + 1, False) + prices[n]
                not_sell = transaction(n + 1, k, bflag)
                cache2[n][bflag] = max(sell, not_sell)
                return max(sell, not_sell)
            else:
                buy = transaction(n + 1, k, True) - prices[n]
                not_buy = transaction(n + 1, k, False)
                cache2[n][bflag] = max(buy, not_buy)
                return max(buy, not_buy)

        return max(transaction(0, 0,  False), transaction2(0,0,False))

print(Solution().maxProfit([7,1,5,3,6,4]))



