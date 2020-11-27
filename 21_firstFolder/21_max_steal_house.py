# CTCI : Q17_16_The_Masseuse
# https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
# Question : There are n houses build in a line, each of which contains some value in it. A thief is going to
# steal the maximal value of these houses, but he can't steal in two adjacent houses because owner of the
# stolen houses will tell his two neighbour left and right side. What is the maximum stolen value.
#
# Examples:
# Input  : hval[] = {6, 7, 1, 3, 8, 2, 4}
# Output : 19
# Thief will steal 6, 1, 8 and 4 from house.
#
# Question Type : Generic
# Used : Dynamic programming
#        dp[0] = inp[0]
#        dp[1] = max(inp[0], inp[1])
#        dp[i] = max(inp[i]+dp[i-2], dp[i-1])
# Complexity : O(n)


def maximizeLoot(inpArr, n):
    if n == 0:
        return 0
    if n == 1:
        return inpArr[0]
    if n == 2:
        return max(inpArr[0], inpArr[1])

    dp = [0] * n
    dp[0] = inpArr[0]
    dp[1] = max(inpArr[0], inpArr[1])

    for i in range(2, n):
        dp[i] = max(inpArr[i] + dp[i - 2], dp[i - 1])

    return dp[-1]


if __name__ == "__main__":
    inpArr = [6, 7, 1, 3, 8, 2, 4]
    print(maximizeLoot(inpArr, len(inpArr)))

    inpArr = [30, 15, 60, 75, 45, 15, 15, 45]
    print(maximizeLoot(inpArr, len(inpArr)))

    inpArr = [5, 5, 10, 100, 10, 5]
    print(maximizeLoot(inpArr, len(inpArr)))
