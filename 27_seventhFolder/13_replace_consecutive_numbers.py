# https://www.geeksforgeeks.org/make-all-array-elements-equal-by-replacing-consecutive-occurrences-of-a-number-repeatedly/
# Question : Given an array arr[] of size N, the task is to find the minimum number of operations
# required to make all the array elements equal by following operation:
# Pick any number between 1 to N.
# Choose an element from the array,
# Replace all the consecutive equal elements with the picked number.
#
# Example : Input: arr[] = {1, 2, 5, 2, 1}, N = 5
# Output: 2
# Explanation: Following are the operations required to make all the elements in arr[] equal.
# {1, 2, 2, 2, 1}, pick 2 and replace it with all consecutive 5s.
# {1, 1, 1, 1, 1}, pick 1 and replace it with all consecutive 2s.
# Therefore, Number of operations required = 2, which is minimum possible.
#
# Question Type : Odd One
# Used : Remove all consecutive duplicates in the initial array. Using the above idea, make dp[l][r] — how many
#        steps are needed to delete all elements within the range [l, r]. Then, the answer is (dp[0][n-1] – 1)
#        in zero-based indexing, just delete the whole array minus one step.
#        Base of dp[][] is dp[i][i] = 1.
#        for l < r, dp[l][r] initially set to dp[l][r-1] + 1.
#        for each element at position i with same color as element at position r, update dp[l][r] if dp[l][i-1]
#        + dp[i, r] is better.
# Complexity : O(N^3)



def minOperations(arr, N):
    p = [-1] * (N + 1)
    j = 0
    for i in range(1, N):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    N = j + 1
    arr = arr[:N]

    dp = []
    for _ in range(N):
        dp.append([0] * N)

    b = [-1] * N

    for j in range(0, N):
        dp[j][j] = 1

        b[j] = p[arr[j]]
        p[arr[j]] = j

        for i in range(j - 1, -1, -1):
            d = dp[i][j - 1] + 1

            k = b[j]
            while k > i:
                d = min(d, dp[i][k - 1] + dp[k][j])
                k = b[k]

            if arr[i] == arr[j]:
                d = min(d, dp[i + 1][j])

            dp[i][j] = d

    return dp[0][N - 1] - 1


if __name__ == "__main__":
    arr = [1, 2, 5, 2, 1]
    N = len(arr)

    print(minOperations(arr, N))
