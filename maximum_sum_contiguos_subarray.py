

class Solution:
    def maxset(self, A):
        n = len(A)
        ans = 0
        sum = 0
        start = []
        end = []
        diff = []
        for i in range(n):
            sum = 0
            for j in range(n):
                if i+j>=n:
                    break
                sum = sum + A[i+j]
                if sum>ans:
                    start.append(i)
                    end.append(i+j)
                    diff.append(sum)
                    ans = sum
        max_diff = diff[-1]
        length = end[-1]-start[-1]+1
        final_start = start[-1]
        final_end = end[-1]
        for i in range(len(start)-2, -1, -1):
            if diff[i]<max_diff:
                break

            if end[i] - start[i]>length:
                final_start = start[i]
                final_end = end[i]
                length = end[i] - start[i] +1

            elif end[i] - start[i] == length:
                if start[i]<final_start:
                    final_start = start[i]
                    final_end = end[i]
        print(A[final_start:final_end+1])





A = [ -1, -1, -1, -1, -1 ]
Solution().maxset(A)
