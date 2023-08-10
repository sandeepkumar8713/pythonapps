# https://leetcode.com/problems/student-attendance-record-ii/
# Question : n attendance record for a student can be represented as a string where each character
# signifies whether the student was absent, late, or present on that day. The record only contains
# the following three characters: 'A': Absent, 'L': Late and 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a
# student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
#
# Example : Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
#
# Question Type : ShouldSee
# Used : We should do DFS with DP. The sub solution is sum of n-1 with all 3 possibilities (P, A, L).
#        For each day we have 3 possibilities.
#        put 'P', late count resets, absent count continues
#        put 'L', late count increases, absent count continues
#        put 'A', late count resets, absent count increases
#        While doing DFS, save the sub solution in dp.
# Logic: def dfs(dp, n, lateCnt, absntCnt):
#        if lateCnt >= 3 or absntCnt >= 2: return 0
#        if n == 0: return 1
#        if (n,lateCnt, absntCnt) in dp: return dp[(n,lateCnt, absntCnt)]
#        ans = (dfs(dp, n-1, 0, absntCnt) % m + dfs(dp, n-1, lateCnt + 1, absntCnt) % m
#           + dfs(dp, n-1, 0, absntCnt +1) % m) % m
#        dp[(n, lateCnt, absntCnt)] = ans
#        return dp[(n, lateCnt, absntCnt)]
#
#        dfs(dp, n, 0, 0)
# Complexity : O(n)

m = 1e9 + 7


def dfs(dp, n, lateCnt, absntCnt):
    if lateCnt >= 3 or absntCnt >= 2:
        return 0

    if n == 0:
        return 1

    if (n,lateCnt, absntCnt) in dp:
        return dp[(n,lateCnt, absntCnt)]

    # 3 option possible
    # put 'P', late count resets, absent count continues
    # put 'L', late count increases, absent count continues
    # put 'A', late count resets, absent count increases
    ans = (dfs(dp, n-1, 0, absntCnt) % m + dfs(dp, n-1, lateCnt + 1, absntCnt) % m + dfs(dp, n-1, 0, absntCnt +1) % m) % m
    dp[(n, lateCnt, absntCnt)] = ans
    return dp[(n, lateCnt, absntCnt)]


def awardCount(n):
    dp = {}
    return dfs(dp, n, 0, 0)


if __name__ == "__main__":
    n = 2
    print(awardCount(n))

    n = 1
    print(awardCount(n))
