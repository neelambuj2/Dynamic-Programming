
def lcs(str1, str2, i , j):
    if i == len(str1) or j == len(str2):
        return 0

    if str1[i] == str2[j]:
        print(str1[i])
        return 1 + lcs(str1, str2, i+1, j+1)

    left = lcs(str1, str2, i+1 ,j)
    right = lcs(str1, str2, i, j+1)
    return max(left, right)

str1 = input()
str2 = input()
resp = lcs(str1, str2, 0, 0)
print(resp)