row = int(input())
col = int(input())
mat = []
for i in range(row):
    temp = [int(j) for j in input().split(" ")]
    mat.append(temp)

def get_connected(mat, r, c):
    if r < 0 or c < 0 or r>=row or c>=col:
        return 0

    if mat[r][c] == 0:
        return 0
    mat[r][c]=0
    size=1
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if i!=r or j!=c:
                size = size+get_connected(mat, i, j)
    return size




size=0
for r in range(row):
    for c in range(col):
        if mat[r][c]==1:
            size = max(size, get_connected(mat,r,c))

print(size)


