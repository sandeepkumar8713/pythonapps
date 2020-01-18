# CTCI : Q17_16_The_Masseuse
# https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
# Question : There are n houses build in a line, each of which contains some value in it. A thief is going to
# steal the maximal value of these houses, but he can't steal in two adjacent houses because owner of the
# stolen houses will tell his two neighbour left and right side. What is the maximum stolen value.
#
# Examples:
# Input  : hval[] = {6, 7, 1, 3, 8, 2, 4}
# Output : 19
# Thief will steal 6, 1, 8 and 4 from house.
#
# Used : Dynamic programming
#        dp[i] = max(inp[i]+dp[i-2],dp[i])
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
    # inpArr = [30, 15, 60, 75, 45, 15, 15, 45]
    n = len(inpArr)
    print (maximizeLoot(inpArr, n))
