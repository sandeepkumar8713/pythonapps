# https://leetcode.com/problems/first-missing-positive/discuss/269453/0-ms-beat-100-java-submission-first-missing-positive
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array-set-2/
# Question : Given an unsorted integer array, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
# Example 1: Input: [1,2,0]
# Output: 3
#
# Question Type : ShouldSee
# Used : Run a while on the given array. Find correct index for the element assuming index starts from 0.
#        c = inpArr[i] - 1.
#        If the current element is +ve and not placed at its correct position, swap element at i and c.
#        else increment i
#        Now run another loop, to find the element which is not at it correct position.
# Logic: while i < n:
#           c = inpArr[i] - 1
#           if inpArr[i] > 0 and c < n:
#               if inpArr[i] != inpArr[c]:
#                   inpArr[c], inpArr[i] = inpArr[i], inpArr[c]
#                   continue
#           i += 1
#        for i in range(n):
#           if inpArr[i] != i + 1:
#               return i + 1
#        return n + 1
# Complexity : O(n)


def firstMissingPositive(inpArr):
    n = len(inpArr)
    i = 0
    while i < n:
        c = inpArr[i] - 1

        if inpArr[i] > 0 and c < n:
            if inpArr[i] != inpArr[c]:
                inpArr[c], inpArr[i] = inpArr[i], inpArr[c]
                continue
        i += 1

    for i in range(n):
        if inpArr[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    inpArr = [3, 4, -1, 1]
    print(firstMissingPositive(inpArr))

    inpArr = [2, 3, 7, 6, 8, -1, -10, 15]
    print(firstMissingPositive(inpArr))
