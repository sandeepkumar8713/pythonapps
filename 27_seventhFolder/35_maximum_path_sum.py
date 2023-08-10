# https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/
# https://leetcode.com/problems/get-the-maximum-score/
# Question : You are given two sorted arrays of distinct integers nums1 and nums2.
# A valid path is defined as follows:
#     Choose array nums1 or nums2 to traverse (from index-0).
#     Traverse the current array from left to right.
#     If you are reading any value that is present in nums1 and nums2 you are
#     allowed to change your path to the other array. (Only one repeated value
#     is considered in the valid path).
# The score is defined as the sum of uniques values in a valid path.
# Return the maximum score you can obtain of all possible valid paths.
# Since the answer may be too large, return it modulo 109 + 7.
#
# Question Type : Generic
# Used : We will traverse the two array like merge sort.
#        While doing so maintain 2 variables sum1 and sum2. sum1 will add lesser elements from ar1.
#        sum2 will add lesser elements from ar2. When same element is found. Choose
#        max of sum1 and sum2 as result.
#        After the loop, find sum1 and sum2 of remaining elements in each of the array.
#        Add max of sum1 and sum2 to result and return result.
# Logic: while (i < m and j < n):
#           if ar1[i] < ar2[j]:
#               sum1 += ar1[i], i += 1
#           elif ar1[i] > ar2[j]:
#               sum2 += ar2[j], j += 1
#           else:
#             result += max(sum1, sum2) + ar1[i]
#             sum1 = 0, sum2 = 0
#             i += 1, j += 1
#        while i < m:
#           sum1 += ar1[i]
#           i += 1
#        while j < n:
#           sum2 += ar2[j]
#           j += 1
#        result += max(sum1, sum2)
#        return result
# Complexity : O(m+n)


def maxPathSum(ar1, ar2):
    m = len(ar1)
    n = len(ar2)
    i, j = 0, 0
    result, sum1, sum2 = 0, 0, 0

    # Below 3 loops are similar to merge in merge sort
    while i < m and j < n:
        # Add elements of ar1[] to sum1
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1
        # Add elements of ar2[] to sum2
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1
        else:  # we reached a common point
            # Take the maximum of two sums and add to result
            result += max(sum1, sum2) + ar1[i]
            # update sum1 and sum2 to be considered fresh for next elements
            sum1 = 0
            sum2 = 0
            # update i and j to move to next element in each array
            i += 1
            j += 1

    # Add remaining elements of ar1[]
    while i < m:
        sum1 += ar1[i]
        i += 1
    # Add remaining elements of b[]
    while j < n:
        sum2 += ar2[j]
        j += 1

    # Add maximum of two sums of remaining elements
    result += max(sum1, sum2)
    return result


if __name__ == "__main__":
    # Driver code
    ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
    ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
    print("Maximum sum path is", maxPathSum(ar1, ar2))

    ar1 = [2, 4, 5, 8, 10]
    ar2 = [4, 6, 8, 9]
    print("Maximum sum path is", maxPathSum(ar1, ar2))
