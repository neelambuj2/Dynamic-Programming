import math
from collections import defaultdict
class Solution:
    def numSquares(self, n: int) -> int:
        nSqrt = int(math.sqrt(n))
        level = 0
        visited = [False for i in range(n)]
        psquares = [j*j for j in range(1,nSqrt+1)]
        queue = list()
        queue.append(n)
        while queue:
            level+=1
            for i in range(len(queue)):
                num = queue.pop(0)
                for psqr in psquares:
                    remain = num - psqr
                    if remain == 0:
                        return level
                    elif remain>0 and visited[remain-1] is False:
                        visited[remain-1] = True
                        queue.append(remain)
                    elif remain<0:
                        break
        return 0
