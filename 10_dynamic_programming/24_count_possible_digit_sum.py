# https://www.geeksforgeeks.org/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/
# Question : Given two integers 'n' and 'sum', find count of all n digit numbers with sum of
# digits as 'sum'. Leading 0's are not counted as digits.
#
# Input:  n = 2, sum = 2
# Output: 2
# Explanation: Numbers are 11 and 20
#
# Question Type : Generic
# Used : Maintain a table dp of size: digitCount * targetSum and set all values as -1.
#        Call a recursive function countRec(digitCount, targetSum, dp, firstCall).
#        if digitCount == 0:
#           if targetSum == 0: return 1 else: return 0
#        Check if for given digitCount and targetSum, possible count is already calculate.
#        if dp[digitCount][targetSum] != -1: return dp[digitCount][targetSum]
#        If this func is called first time start from 1 else 0.
#        Run a loop by taking all possible digits from i : (0 or 1) to 9 and
#        call recursive function again on each.
#           if targetSum - i >= 0:
#               possibleCount += countRec(digitCount - 1, targetSum - i, dp, false)
#        After the loop set dp[digitCount][targetSum] = possibleCount and return it.
# Complexity : O(n * m) where n is digitCount and m is targetSum


def countRec(digitCount, targetSum, dp, firstCall):
    if digitCount == 0:
        if targetSum == 0:
            return 1
        else:
            return 0

    if dp[digitCount][targetSum] != -1:
        return dp[digitCount][targetSum]

    start = 0
    if firstCall:
        start = 1   # First digit must be from 1 to 9

    possibleCount = 0
    for i in range(start, 10):
        if targetSum - i >= 0:
            possibleCount += countRec(digitCount - 1, targetSum - i, dp, False)

    dp[digitCount][targetSum] = possibleCount
    return possibleCount


def finalCount(digitCount, targetSum):
    dp = []
    for i in range(digitCount + 1):
        dp.append([-1] * (targetSum + 1))

    return countRec(digitCount, targetSum, dp, True)


if __name__ == "__main__":
    digitCount = 3
    targetSum = 5
    print(finalCount(digitCount, targetSum))
