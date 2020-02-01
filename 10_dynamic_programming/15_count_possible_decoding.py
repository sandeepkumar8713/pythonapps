# Question : Let 1 represent 'A', 2 represents 'B', etc. Given a digit sequence, count the number of possible
# decodings of the given digit sequence.
#
# Input:  digits[] = "121"
# Output: 3
# The possible decodings are "ABA", "AU", "LA"
#
# Question Type : Generic
# Used : If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
#        If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add
#           the result to total count.
#        Maintain DP of size n+1: where dp[n] represents possible count for digits[n-1]. set dp[0] = 1, dp[1] = 1
#        Run a loop from 2 to n over digits. If  if digits[i-1] > '0': dp[i] = dp[i-1]
#           If digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7'): dp[i] += dp[i - 2]
#           If we get 2 digits add its dp[i-2] value to current dp[i]
#        return dp[n]
# Complexity : O(n)


def countDecodingDP(digits, n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        if digits[i-1] > '0':
            dp[i] = dp[i-1]

        if digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7'):
            dp[i] += dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    digits = "1234"
    n = len(digits)
    print(countDecodingDP(digits, n))
