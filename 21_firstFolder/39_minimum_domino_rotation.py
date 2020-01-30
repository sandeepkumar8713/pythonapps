# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# Question : In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the i-th domino,
# so that A[i] and B[i] swap values. Return the minimum number of rotations so that all the values in A are the same,
# or all the values in B are the same. If it cannot be done, return -1.
#
# Example : Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
# as indicated by the second figure
#
# Question Type : ShouldSee
# Used : Choose first element(num) of array A, count number of rotations required in both arrays to make all of them
#        equal. if num is not in either of array then return -1. Else return minimum rotation.
#        Repeat the same by choosing first element from array B.
#        Logic : def minDominoRotations(arrA, arrB):
#        length = len(arrA)
#        rotations = get_count(arrA[0], arrA, arrB, length)
#        if rotations != -1 or arrA[0] == arrB[0]:
#           return rotations
#        else:
#           return get_count(arrB[0], arrA, arrB, length)
#        def get_count(num, arrA, arrB, length):
#        rotations_a = rotations_b = 0
#        for i in range(length):
#           if num != arrA[i] and num != arrB[i]: return -1
#           elif num != arrA[i]: rotations_a += 1
#           elif num != arrB[i]: rotations_b += 1
#        return min(rotations_a, rotations_b)
# Complexity : O(n)


def get_count(num, arrA, arrB, length):
    rotations_a = rotations_b = 0
    for i in range(length):
        # if num is not in either of array then return -1
        if num != arrA[i] and num != arrB[i]:
            return -1

        elif num != arrA[i]:
            rotations_a += 1

        elif num != arrB[i]:
            rotations_b += 1

    return min(rotations_a, rotations_b)


def minDominoRotations(arrA, arrB):
    length = len(arrA)
    rotations = get_count(arrA[0], arrA, arrB, length)

    if rotations != -1 or arrA[0] == arrB[0]:
        return rotations
    else:
        return get_count(arrB[0], arrA, arrB, length)


if __name__ == "__main__":
    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(minDominoRotations(A, B))
