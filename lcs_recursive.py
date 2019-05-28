


def lcs(seq, i, j):
    if i==j:
        return 1
    if seq[i]==seq[j] and i+1==j:
        return 2
    if seq[i]==seq[j]:
        return 2+lcs(seq,i+1,j-1)

    return max(lcs(seq,i+1,j),lcs(seq,i,j-1))

def lcs_dp(seq, n):
    t=[[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        t[i][i]=1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if seq[i]==seq[j] and l ==2:
                t[i][j] = 2
            elif seq[i]==seq[j]:
                t[i][j] = 2+t[i+1][j-1]
            else:
                t[i][j] = max(t[i+1][j], t[i][j-1])
    print(t)
    print(t[0][n-1])
if __name__=="__main__":
    seq = input()
    n = len(seq)
    #print(lcs(seq,0,n-1))
    lcs_dp(seq,n)
