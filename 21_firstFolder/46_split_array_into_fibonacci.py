# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/discuss/134428/DFS-%2B-Backtracking-C%2B%2B-Solution
# Question : Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence
# [123, 456, 579]. Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if
# the piece is the number 0 itself. Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
#
#
# Example : Input: "123456579"
# Output: [123,456,579]

# Example 2: Input: "11235813"
# Output: [1,1,2,3,5,8,13]
#
# Question Type : Generic
# Used : DFS and backtracking. We make a recursive function. It takes a substring and calls it self again to check if
#        remaining strings fulfill the condition of fibonacci.
#        Logic : def helper(inp, ans, beg=0):
#        if len(inp) == beg:
#           if len(ans) > 2: return True
#           else: return False
#        if inp[beg] == '0': numLen = 1
#        else: numLen = 10
#        i = 0, N = len(inp)
#        while i < numLen and beg + i < N:
#           curr = long(inp[beg: beg + i + 1])
#           if curr > sys.maxint:
#               return False
#           sz = len(ans)
#           if sz < 2 or (sz > 1 and ans[sz-2] + ans[sz-1] == int(curr)):
#               ans.append(int(curr))
#               if helper(inp, ans, beg+i+1):
#                   return True
#               ans.pop()
#           i += 1
#        return False
# Complexity : O(n^2)

import sys


def splitIntoFibonacci(inp):
    ans = []
    if helper(inp, ans):
        return ans
    else:
        return []


def helper(inp, ans, beg=0):
    if len(inp) == beg:
        if len(ans) > 2:
            return True
        else:
            return False

    if inp[beg] == '0':
        numLen = 1
    else:
        numLen = 10

    i = 0
    N = len(inp)
    while i < numLen and beg + i < N:
        curr = int(inp[beg: beg + i + 1])
        if curr > sys.maxsize:
            return False
        sz = len(ans)
        if sz < 2 or (sz > 1 and ans[sz-2] + ans[sz-1] == int(curr)):
            ans.append(int(curr))
            if helper(inp, ans, beg+i+1):
                return True
            ans.pop()
        i += 1

    return False


if __name__ == "__main__":
    inp = "123456579"
    print(splitIntoFibonacci(inp))

    inp = "11235813"
    print(splitIntoFibonacci(inp))
