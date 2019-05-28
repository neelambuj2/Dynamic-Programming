str1 = input()
str2 = input()


def lcs(str1, str2, i, j):
    if i == len(str1) or j==len(str2):
        return 0
    if str1[i]!=str2[j]:
        left = lcs(str1, str2,i+1,j)
        right = lcs(str1, str2,i,j+1)
        return max(left, right)
    if str1[i]==str2[j]:
        res = lcs(str1,str2,i+1, j+1)
        return 1+res

print(lcs(str1,str2,0,0))