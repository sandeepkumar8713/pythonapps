# https://leetcode.com/problems/first-missing-positive/discuss/269453/0-ms-beat-100-java-submission-first-missing-positive
# Question : Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1: Input: [1,2,0]
# Output: 3
#
# Question Type : Easy
# Used : Run a loop over the given elements. If this ele is positive and less than count of inpArr. Assign this in
#        tempArr at same index. Later on run loop for the tempArr, return the index at which its value doesn't match.
#        Logic :
#        for ele in inpArr:
#           if ele > 0 and ele <= n:
#               if tempArr[ele] != ele: tempArr[ele] = ele
#        j = 1
#        while j < len(tempArr):
#           if tempArr[j] != j: return j
#           j += 1
#        return j
# Complexity : O(n)


def firstMissingPositive(inpArr):
    n = len(inpArr)
    tempArr = [0] * (n + 1)
    for ele in inpArr:
        if ele > 0 and ele <= n:
            if tempArr[ele] != ele:
                tempArr[ele] = ele

    j = 1
    while j < len(tempArr):
        if tempArr[j] != j:
            return j
        j += 1

    return j


if __name__ == "__main__":
    inpArr = [3, 4, -1, 1]
    print(firstMissingPositive(inpArr))
