# https://www.geeksforgeeks.org/minimum-number-of-sub-strings-of-a-string-such-that-all-are-power-of-5/
# Question : Given a binary string str. The task is to find the smallest positive integer C such that the binary
# string can be cut into C pieces (sub-strings) and each sub-string should be a power of 5 with no leading zeros.
#
# Used : Iterate from i = 1 and for every str[j...i] where j = 0 & j < i, we check if the number formed from str[j..i]
#        is a power of 5 then we update the dp[] array with the value of the lowest possible cut size value.
#        After confirming that the number formed from str[j..i] in decimal is a power of 5 we calculate
#        dp[i] = min(dp[i], dp[j] + 1).
# Complexity : O(n^2)


def ispower(n):
    if n < 125:
        return n == 1 or n == 5 or n == 25
    if n % 125 != 0:
        return 0
    else:
        return ispower(n // 125)


def number(s, i, j):
    ans = 0
    for x in range(i, j):
        ans = ans * 2 + (ord(s[x]) - ord('0'))
    return ans


def minCuts(inpStr):
    n = len(inpStr)
    dp = [n+1] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        if inpStr[i - 1] == '0':
            continue
        for j in range(i):
            if inpStr[j] == '0':
                continue
            num = number(inpStr, j, i)
            if not ispower(num):
                continue
            dp[i] = min(dp[i], dp[j] + 1)

    if dp[n] < n + 1:
        return dp[n]
    else:
        return -1


if __name__ == "__main__":
    inpStr = "101101101"
    print(minCuts(inpStr))
