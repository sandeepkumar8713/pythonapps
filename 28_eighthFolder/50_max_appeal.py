# https://leetcode.com/discuss/interview-question/355698/amazon-oa-2019-find-pair-with-max-appeal-sum
# Question : Find pair with maximum Appeal value.
#
# Input: Array
# Output: index {i, j} ( i = j allowed) with maximum Appeal
# Appeal = A[i] +A[j] + abs(i-j)
#
# Question Type : Easy
# Used : A[i] +A[j] + abs(i-j)
#        A[i] + A[j] + (i-j) = (A[i]+i) + (A[j]-j)
#        A[i] + A[j] - (i-j) = (A[i]-i) + (A[j]+j)
#        Since we are allowed to have same i=j, so just find the max value of each (A[i]-i), (A[i]+i).
# Logic: for i, num in enumerate(nums):
#        if num - i > max_2:
#           max_2 = num - i, index_2 = i
#        if num + i > max_1:
#           max_1 = num + i, index_1 = i
#        return [index_1, index_2]
# Complexity : O(n)

import sys


def max_appeal_pair(nums):
    max_1 = -sys.maxsize
    max_2 = -sys.maxsize
    index_1 = 0
    index_2 = 0
    for i, num in enumerate(nums):
        if num - i > max_2:
            max_2 = num - i
            index_2 = i
        if num + i > max_1:
            max_1 = num + i
            index_1 = i

    return [index_1, index_2]


if __name__ == "__main__":
    nums = [6, 2, 7, 4, 4, 1, 6]
    print (max_appeal_pair(nums))
