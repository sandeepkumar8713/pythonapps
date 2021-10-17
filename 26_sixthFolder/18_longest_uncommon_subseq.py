# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Question : Given an array of strings strs, return the length of the longest uncommon subsequence
# between them. If the longest uncommon subsequence does not exist, return -1. An uncommon
# subsequence between an array of strings is a string that is a subsequence of one string but not the others.
#
# Example : Input: strs = ["abbba", "aaa", "aaa", "aa"]
# Output: 5
# Explanation : abbba is not a subsequence of any other string
#
# Question Type : Generic
# Used : Sort the given input array in descending order.
#        Run 2 loops to make all possible pairs (both left and right).
#        If a word is not subsequence of any other word in array, return its len.
#        After the loop, return -1.
#        Logic :
#        inpStr.sort(key=lambda x: -len(x))
#        for i in range(n):
#           isSub = False
#           for j in range(n):
#               if i != j and isSubsequence(inpStr[i], inpStr[j]):
#                   isSub = True, break
#           if isSub is False:
#               return len(inpStr[i])
#        return -1
# Complexity : O(n * n * k) n is number of ele in array. k is max len of ele.


# Check if all chars of a in b.
def isSubsequence(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == n


def findLongest(inpStr):
    inpStr.sort(key=lambda x: -len(x))
    n = len(inpStr)
    res = -1

    for i in range(n):
        isSub = False
        for j in range(n):
            if i != j and isSubsequence(inpStr[i], inpStr[j]):
                isSub = True
                break
        if isSub is False:
            return len(inpStr[i])

    return res


if __name__ == "__main__":
    strs = ["aba", "cdc", "eae"]
    print(findLongest(strs))

    strs = ["aaa", "aaa", "aa"]
    print(findLongest(strs))

    # here abbba is not a subsequence of any other string
    strs = ["abbba", "aaa", "aaa", "aa"]
    print(findLongest(strs))
