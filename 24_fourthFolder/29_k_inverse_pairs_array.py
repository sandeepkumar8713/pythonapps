# https://leetcode.com/problems/k-inverse-pairs-array/solution/
# Question : Given two integers n and k, find how many different arrays consist of numbers from 1 to n such
# that there are exactly k inverse pairs. We define an inverse pair as following: For ith and jth element in the
# array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not. Since the answer may be very large,
# the answer should be modulo 109 + 7.
#
# Example : Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
#
# Question Type : ShouldSee
# Used : count(n,k) = summation 0 : min(k, n-1) of count(n-1,k-i)
#        Logic :
#        dp[][] = [0]
#        for i in range(1, n + 1):
#           for j in range(0, k + 1):
#               if j == 0: dp[i][j] = 1
#               else:
#                   for p in range(0, min(j, i-1) + 1):
#                       dp[i][j] = (dp[i][j] + dp[i-1][j-p]) % 1000000007
#        return dp[n][k]
# Complexity : O(n * k * k)


def kInversePairs(n, k):
    dp = []
    for i in range(n + 1):
        dp.append([0] * (k + 1))

    for i in range(1, n + 1):
        for j in range(0, k + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                for p in range(0, min(j, i-1) + 1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-p]) % 1000000007

    return dp[n][k]


# O(n * k)
def kInversePairEfficient(n, k):
    dp = [0] * (k + 1)
    M = 1000000007
    for i in range(1, n+1):
        temp = [0] * (k+1)
        temp[0] = 1
        for j in range(1, k+1):
            if M - (j - i) >= 0:
                imt = dp[j-i]
            else:
                imt = 0
            val = (dp[j] + imt) % M
            temp[j] = (temp[j-1] + val) % M
        dp = temp

    if k > 0:
        imt = dp[k-1]
    else:
        imt = 0

    return (dp[k] + M - imt) % M


if __name__ == "__main__":
    n = 3
    k = 0

    n = 3
    k = 1
    print(kInversePairs(n, k))
