class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = A[0]
        max_here = A[0]

        for i in A:
            max_here = max(max_here + i, i,
                           max_so_far=max(max_so_far, max_here)

        return max_so_far

