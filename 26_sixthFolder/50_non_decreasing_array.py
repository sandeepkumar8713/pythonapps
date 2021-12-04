# https://leetcode.com/problems/non-decreasing-array/
# Question : Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element. We define an array is non-decreasing if
# nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
#
# Example : Input =  [1, 3, 7, 2, 8]
# Output : True
# Explanation : replace 2 by 7
#
# Question Type : Easy
# Used : Run loop over given input array, if we find any element greater than next, mark it as 1 modification
#        and do the modification by setting current value with next value. If we find second
#        modification return False.
#        If we exit the loop return False.
#        Logic :
#        n = len(inpArr), needModification = False
#        for i in range(n - 1):
#           if inpArr[i] > inpArr[i + 1]:
#               if needModification:
#                   return False
#               needModification = True
#               if i > 0 and inpArr[i + 1] < inpArr[i - 1]:
#                   inpArr[i + 1] = inpArr[i]
#        return True
# Complexity : O(n)


def checkPossibility(inpArr):
    if inpArr is None and len(inpArr) < 2:
        return True

    n = len(inpArr)
    needModification = False
    for i in range(n - 1):
        if inpArr[i] > inpArr[i + 1]:
            if needModification:
                return False
            needModification = True
            if i > 0 and inpArr[i + 1] < inpArr[i - 1]:
                # one modification allowed
                inpArr[i + 1] = inpArr[i]

    return True


if __name__ == "__main__":
    inpArr = [1, 3, 7, 2, 8]
    print(checkPossibility(inpArr))
