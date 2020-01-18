# CTCI : Q16_06_Smallest_Difference
# https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
# Question : Given two arrays of integers, compute the pair of values (one value in each array) with the
# smallest (non-negative) difference. Return the difference.
#
# Used : A.sort(), B.sort()
#        while a < m and b < n:
#        if abs(A[a] - B[b]) < result:
#           result = abs(A[a] - B[b])
#        if A[a] < B[b]:
#            a += 1
#        else:
#            b += 1
# Complexity : O(A logA + B logB)

import sys


def findSmallestDifference(A, B, m, n):
    A.sort()
    B.sort()
    a = 0
    b = 0
    result = sys.maxsize
    pairA = -1
    pairB = -1

    while a < m and b < n:
        if abs(A[a] - B[b]) < result:
            result = abs(A[a] - B[b])
            pairA = A[a]
            pairB = B[b]

        if A[a] < B[b]:
            a += 1
        else:
            b += 1

    print ("Pair : " + str(pairA) + ", " + str(pairB))
    return result


if __name__ == "__main__":
    A = [1, 2, 11, 5]
    B = [4, 12, 19, 23, 127, 235]
    m = len(A)
    n = len(B)
    print(findSmallestDifference(A, B, m, n))
