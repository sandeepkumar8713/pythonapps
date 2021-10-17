# https://leetcode.com/problems/magical-string/
# Question : A magical string s consists of only '1' and '2' and obeys the following rules:
# The string s is magical because concatenating the number of contiguous occurrences of characters
# '1' and '2' generates the string s itself. The first few elements of s is s = "1221121221221121122……".
# If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and
# the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see
# that the occurrence sequence is s itself. Given an integer n, return the number of 1's in the
# first n number in the magical string s.
#
# Example : Input: n = 6
# Output: 3
# Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
#
# Question Type : ShouldSee
# Used : Follow the pattern. one 1 and two 2, then repeat
#        We try to construct the pattern till length
#        While keep count of 1's
#        Logic :
#        magStr = "122"
#        lastDigit = 2, strCount = 3
#        while strCount <= n:
#           if lastDigit == 2:
#               strCount += 1
#               ones += 1
#               lastDigit = 1
#           else:
#               strCount += 2
#               lastDigit = 2
#        return ones
# Complexity : O(n)


def countOnes(n):
    magStr = "122"
    ones = 1
    if n == 0:
        return 0

    if n <= 3:
        return ones

    lastDigit = 2
    strCount = 3
    while strCount <= n:
        if lastDigit == 2:
            strCount += 1
            ones += 1
            lastDigit = 1
        else:
            strCount += 2
            lastDigit = 2

    return ones


if __name__ == "__main__":
    n = 6
    print(countOnes(n))

    n = 1
    print(countOnes(n))
