class Solution:
    def wordBreak(self, s: str, wordDict: list, ans) -> bool:
        ans[0] = True
        for i in range(len(s)):
            if ans[i]:
                for word in word_dict:
                    l = len(word)
                    if s[i:i+l] == word:
                        ans[i+l] = True
        return ans[-1]


s = input()
ans = [False for i in range(len(s)+1)]
word_dict = list(input().rstrip().split())
x = Solution().wordBreak(s, word_dict, ans)
print(x)
