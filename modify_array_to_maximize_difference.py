def maximumDifferenceSum(arr, N):
    # Initialize dp[][] with 0 values.
    dp = [[0, 0] for i in range(N)]
    for i in range(N):
        dp[i][0] = dp[i][1] = 0

    for i in range(N - 1):
        # for [i+1][0] (i.e. current modified
        # value is 1), choose maximum from
        # dp[i][0] + abs(1 - 1) = dp[i][0]
        # and dp[i][1] + abs(1 - arr[i])
        dp[i + 1][0] = max(dp[i][0], dp[i][1] +
                           abs(1 - arr[i]))

        # for [i+1][1] (i.e. current modified value
        # is arr[i+1]), choose maximum from
        # dp[i][0] + abs(arr[i+1] - 1) and
        # dp[i][1] + abs(arr[i+1] - arr[i])
        dp[i + 1][1] = max(dp[i][0] + abs(arr[i + 1] - 1),
                           dp[i][1] + abs(arr[i + 1] - arr[i]))

    return max(dp[N - 1][0], dp[N - 1][1])


# Driver Code
if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5]
    N = len(arr)
    print(maximumDifferenceSum(arr, N))