#!/bin/python3

# input str = 1102021222
# k = 2
# output : 6

import math
import os
import random
import re
import sys

#
# Complete the 'perfectSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

from collections import defaultdict


def is_perfect(freq_dict, k):
    for item, value in freq_dict.items():
        if value != k:
            return False
    return True


def perfectSubstring(s, k):
    # Write your code here
    left = 0
    right = 0
    n = len(s)
    freq_dict = defaultdict(int)

    res = 0
    # while left < n and right < n:
    #     ele = s[right]
    #     freq_dict[ele] += 1
    #     if is_perfect(freq_dict, k):
    #         res += 1
    #     else:

    if k == 0:
        return 0

    dp = [[0] * n for _ in range(n)]
    for left in range(n):
        freq_dict = defaultdict(int)
        for right in range(left, n):
            ele = s[right]
            freq_dict[ele] += 1
            if is_perfect(freq_dict, k):
                dp[left][right] = dp[left + 1][right - 1] + 1

    for item in dp:
        print(item)

    res = 0
    for i in range(n):
        for j in range(n):
            res += dp[i][j]
    return res


# 1102021222
# k = 2

# left = 0, rigth all possible posiitons
# [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Adding all

## 11 56778 22
## k = 2
## dp[0][1]
## dp[n-2][n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = perfectSubstring(s, k)

    fptr.write(str(result) + '\n')

    fptr.close()