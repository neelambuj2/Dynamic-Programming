s = input()
str2 = s[::-1]
l1 = len(s)
l2 = len(str2)
t = [[0 for j in range(l2+1)] for i in range(l1 + 1)]
max_len = 0
x = 0
y = 0
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s[i - 1] == str2[j - 1]:
            t[i][j] = t[i-1][j-1] + 1
            if t[i][j] > max_len:
                max_len = t[i][j]
                y = i
                x = j

while t[y][x] != 0:
    print(s[y - 1], end='')
    x=x-1
    y=y-1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        str2 = s[::-1]
        l1 = len(s)
        l2 = len(str2)
        t = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        max_len = 0
        x = 0
        y = 0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s[i - 1] == str2[j - 1]:
                    t[i][j] = t[i - 1][j - 1] + 1
                    if t[i][j] > max_len:
                        max_len = t[i][j]
                        y = i
                        x = j
        res = ""
        while t[y][x] != 0:
            if s[y-1] == str2[x-1]:
                res = res + s[y - 1]
            x = x - 1
            y = y - 1
        return res

