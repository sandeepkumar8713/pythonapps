# https://careercup.com/question?id=5659623095271424
# Question : You have an array of numbers. You have to give the range in which each number is the maximum element.
#
# Example:
# Input : 1, 5, 4, 3, 6
# Output :
# 1 [1, 1]
# 5 [1, 4]
# 4 [3, 4]
# 3 [4, 4]
# 6 [1, 5]
#
# Question Type : Generic
# Used : For each element in inpArr, find the left most index till which given element is max.
#        Similarly do the same for right index.
#        def getLeftRange(inpArr):
#        maxNum = inpArr[0]
#        leftIdx = [0] * len(inpArr), leftIdx[0] = 1
#        for i in range(1, len(inpArr)):
#           if maxNum < inpArr[i]:
#               maxNum = inpArr[i]
#               leftIdx[i] = leftIdx[0]
#           if inpArr[i-1] > inpArr[i]:
#               leftIdx[i] = i + 1
#           elif inpArr[i] != maxNum:
#               leftIdx[i] = leftIdx[i-1]
#        return leftIdx
# Complexity : O(n)

def getLeftRange(inpArr):
    maxNum = inpArr[0]
    leftIdx = [0] * len(inpArr)
    leftIdx[0] = 1
    for i in range(1, len(inpArr)):
        if maxNum < inpArr[i]:
            maxNum = inpArr[i]
            leftIdx[i] = leftIdx[0]

        if inpArr[i-1] > inpArr[i]:
            leftIdx[i] = i + 1

        elif inpArr[i] != maxNum:
            leftIdx[i] = leftIdx[i-1]

    return leftIdx

def getRightRange(inpArr):
    maxNum = inpArr[-1]
    rightIdx = [0] * len(inpArr)
    rightIdx[-1] = len(inpArr)
    for i in range(len(inpArr)-2, -1, -1):
        if maxNum < inpArr[i]:
            maxNum = inpArr[i]
            rightIdx[i] = len(inpArr)

        if inpArr[i+1] > inpArr[i]:
            rightIdx[i] = i + 1

        elif inpArr[i] != maxNum:
            rightIdx[i] = rightIdx[i+1]

    return rightIdx


def findRange(inpArr):
    leftIdx = getLeftRange(inpArr)
    rightIdx = getRightRange(inpArr)
    for i in range(0, len(inpArr)):
        print(inpArr[i], "[", leftIdx[i], rightIdx[i], "]")


if __name__ == "__main__":
    inpArr = [1, 5, 4, 3, 6]
    findRange(inpArr)
