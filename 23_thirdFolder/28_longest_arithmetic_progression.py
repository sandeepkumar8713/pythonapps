# https://massivealgorithms.blogspot.com/2019/04/leetcode-1027-longest-arithmetic.html
# Similar : https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
# Similar : https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Question : Given an array A of integers, return the length of the longest arithmetic
# subsequence in A. Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k]
# with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if
# B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
#
# Example 1: Input: [3,6,9,12]
# Output: 4
# Explanation: The whole array is an arithmetic sequence with steps of length = 3.
#
# Example 2: Input: [9,4,7,2,10]
# Output: 3
# Explanation: The longest arithmetic subsequence is [4,7,10].
#
# Question Type : Generic
# Used : The main idea is to maintain a map of differences seen at each index. We iteratively
#        build the map for a new index i, by considering all elements to the left one-by-one.
#        For each pair of indices (i,j) and difference d = A[i]-A[j] considered, we check if
#        there was an existing chain at the index j with difference d already.
#        If yes, we can then extend the existing chain length by 1.
#        Else, if not, then we can start a new chain of length 2 with this new difference
#        d and (A[j], A[i]) as its elements.
#        At the end, we can then return the maximum chain length that we have seen so far.
# Logic: def longestArithSeqLength(inpArr):
#        indexMap = dict(), res = 1, n = len(inpArr)
#        diffMap = dict()
#        diffMap[inpArr[0]] = 1
#        indexMap[0] = diffMap
#        for i in range(n):
#           diffMap = dict()
#           for j in range(i):
#               diff = inpArr[i] - inpArr[j]
#               diffMap[diff] = 2
#               previousDiffMap = indexMap[j]
#               if diff in previousDiffMap.keys():
#                   diffMap[diff] = previousDiffMap[diff] + 1
#               res = max(diffMap[diff], res)
#           indexMap[i] = diffMap
#        return res
# Complexity : O(n^2)


def longestArithSeqLength(inpArr):
    #  The main idea is to maintain a map of differences seen at each index.
    indexMap = dict()
    res = 1
    n = len(inpArr)
    diffMap = dict()
    diffMap[inpArr[0]] = 1
    indexMap[0] = diffMap

    for i in range(n):
        diffMap = dict()
        for j in range(i):
            diff = inpArr[i] - inpArr[j]
            diffMap[diff] = 2
            previousDiffMap = indexMap[j]
            if diff in previousDiffMap.keys():
                diffMap[diff] = previousDiffMap[diff] + 1
            res = max(diffMap[diff], res)
        indexMap[i] = diffMap

    return res


if __name__ == "__main__":
    inpArr = [3, 6, 9, 12]
    print(longestArithSeqLength(inpArr))

    inpArr = [9, 4, 7, 2, 10]
    print(longestArithSeqLength(inpArr))

    inpArr = [5, 7, 20, 9, 33]
    print(longestArithSeqLength(inpArr))

    inpArr = [18, 26, 18, 24, 24, 20, 22]
    print(longestArithSeqLength(sorted(inpArr)))
