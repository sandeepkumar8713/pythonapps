# https://leetcode.com/discuss/interview-question/676381/find-longest-contiguous-sub-array-from-two-string-arrays
# Question : Find max sequence of two string arrays.
#
# Example : Input:
# user1 = ["grey", "pink", "green", "red","black","silver"]
# user2 = ["grey", "rose red", "white", "pink", "green", "red","black","silver"]
# Output : ["pine", "green", "red", "black", "silver"]
#
# Question Type : Generic
# Used : Make a 2D matrix and loop over it. This matrix will keep track of lengths of common
#        substring. To print the substring, keep track of i,j for max length. Now traverse
#        diagonally down from i,j till dp is not 0. Here we should have a memorization
#        table to track.
# Logic: dp = [[0] * (n + 1) for _ in range(m + 1)]
#        for i in range(m+1):
#           for j in range(n+1):
#               if i == 0 or j == 0:
#                   dp[i][j] = 0, continue
#               if arr_1[i-1] == arr_2[j-1]:
#                   dp[i][j] = 1 + dp[i-1][j-1]
#                   max_len = max(max_len, dp[i][j])
#                   row = i, col = j
#               else:
#                   dp[i][j] = 0
#        while dp[row][col] != 0:
#           output_arr = [arr_1[row-1]] + output_arr
#           row -= 1, col -= 1
#        return output_arr, max_len
# Complexity : O(m*n)

import sys


def max_subsequnce(arr_1, arr_2):
    m = len(arr_1)
    n = len(arr_2)
    max_len = -sys.maxsize
    row = -1
    col = -1

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if arr_1[i - 1] == arr_2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_len = max(max_len, dp[i][j])
                row = i
                col = j
            else:
                dp[i][j] = 0

    output_arr = []
    while dp[row][col] != 0:
        output_arr = [arr_1[row - 1]] + output_arr
        row -= 1
        col -= 1

    return output_arr, max_len


if __name__ == "__main__":
    user1 = ["grey", "pink", "green", "red", "black", "silver"]
    user2 = ["grey", "rose red", "white", "pink", "green", "red", "black", "silver"]
    print(max_subsequnce(user1, user2))
