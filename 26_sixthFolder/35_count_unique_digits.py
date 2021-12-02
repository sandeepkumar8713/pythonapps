# https://leetcode.com/problems/count-numbers-with-unique-digits/
# Question : Given an integer n, return the count of all numbers with unique digits, x,
# where 0 <= x < 10n.
#
# Question Type : ShouldSee
# Used : if n=3 then for "exact three digits unique number" is 9x9x8=648 and we need to add the
#        unique number of two digits (including one digit) n=3 ans=9x9x8+res[2]
#        So we will use dp and build our ans 1 by 1.
#        Logic :
#        dp = [0] * (n+1)
#        dp[0] = 0, dp[1] = 9
#        res = 10
#        for i in range(2, n+1):
#           dp[i] = dp[i-1] * (10-i+1)
#           res += dp[i]
#        return res
# Complexity : O(n)

def countUnique(n):
    if n == 0:
        return 1

    if n == 1:
        return 10

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 9

    res = 10

    for i in range(2, n+1):
        dp[i] = dp[i-1] * (10-i+1)
        res += dp[i]

    return res


if __name__ == "__main__":
    print(countUnique(3))
