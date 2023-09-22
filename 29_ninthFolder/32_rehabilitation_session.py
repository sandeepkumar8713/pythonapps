# https://leetcode.com/discuss/interview-question/4066807/Microsoft-Online-Assessment-Test-2023-2024
# A patient needs rehabilitation within next N days(numbered from 0 to N-1). The rehabilitation consists of X sessions.
# For every rehabilitation session,other than the last one,the next session is exactly Y days later.
# You are given an array A of N integers listing the costs of the individual rehabilitation sessions on the N days:
# that is rehabilitation on the kth day costs A[k]. Write a function def solution(A,X,Y) that given the array A and
# the two integers X and Y returns the minimum cost of rehabilitation.
#
# TODO :: add used
# Used : categories the items based on diff among them of y.
#        For each category, check if size of items is greater than x
#        If yes, sort it and then pick the top x elements to a possible result
#        Check if this possible result is min.

from collections import defaultdict
import sys


def solve(A, x, y):
    n = len(A)
    dict_map = defaultdict(list)
    for i in range(n):
        dict_map.get(i % y).append(A[i])

    res = sys.maxsize
    for _, values in dict_map.items():
        if len(values) >= x:
            values.sort()
            candidate = 0
            for i in range(x):
                candidate += values[i]
            res = min(res, candidate)

    return res
