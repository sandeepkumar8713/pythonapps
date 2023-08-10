# https://leetcode.com/problems/longest-valid-parentheses/
# https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
# Question : Given a string containing just the characters '(' and ')',
# return the length of the longest valid (well-formed) parentheses substring.
#
# Question Type : Generic
# Used : Run a loop from left to right, while doing so keep count of left and right parentheses.
#        If left and right count are equal update maxlength.
#        If right is more than left, reset left and right to 0.
#        Repeat the above process from right to left. Only difference is :
#        If left is more than right, reset left and right to 0.
# Logic: left = right = 0
#        for i in range(n):
#           if s[i] == '(': left += 1
#           else: right += 1
#           if left == right:
#               maxlength = max(maxlength, 2 * right)
#           elif right > left:
#               left = right = 0
#        left = right = 0
#        for i in range(n - 1, -1, -1):
#           if s[i] == '(': left += 1
#           else: right += 1
#           if left == right:
#               maxlength = max(maxlength, 2 * right)
#            elif left > right:
#               left = right = 0
#        return maxlength
# Complexity : O(n)

def solve(s):
    n = len(s)
    maxlength = 0

    left = right = 0
    for i in range(n):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            maxlength = max(maxlength, 2 * right)

        # Resetting the counters when the subsequence becomes invalid
        elif right > left:
            left = right = 0

    left = right = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            maxlength = max(maxlength, 2 * left)

        # Resetting the counters when the subsequence becomes invalid
        elif left > right:
            left = right = 0

    return maxlength


if __name__ == "__main__":
    print (solve("((()()()()(((())"))

    print(solve(")()())"))
