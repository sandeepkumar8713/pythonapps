# https://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
# Question : Given k arrays of size n each. You have to select one number from each of them such that the
# difference between them is minimum. Initially, the question was for 3 arrays, I told him the solution
# quickly then he changed 3 to k.
#
# Used : Considering the arrays are sorted. We should have current indexes of the array.
#        Run a loop until all the indexes hve reached their end.
#           Find max and min among current elements.
#           If difference of max and min is less than diff, than update diff.
#           If diff is 0, break
#           increment the index of the array, which had minimum element.
#       Logic :
#       while allArrayWithinLimit(maxLen, currentIndex):
#           minimum, arraysIndex = getMinimum(inpMat, currentIndex)
#           maximum = getMaximum(inpMat, currentIndex)
#           if maximum - minimum < diff: bestIndex = currentIndex[:]
#               diff = maximum - minimum
#           if diff is 0: break
#           currentIndex[arraysIndex] += 1
# Complexity : O(sumOfLenOfArrays)

import sys


def allArrayWithinLimit(maxLen, currentIndex):
    for i in range(len(maxLen)):
        if currentIndex[i] >= maxLen[i]:
            return False
    return True


def getMinimum(inpMat, currentIndex):
    tempArray = []
    for i in range(len(currentIndex)):
        tempArray.append(inpMat[i][currentIndex[i]])
    minimum = min(tempArray)
    minIndex = tempArray.index(minimum)
    return minimum, minIndex


def getMaximum(inpMat, currentIndex):
    tempArray = []
    for i in range(len(currentIndex)):
        tempArray.append(inpMat[i][currentIndex[i]])
    return max(tempArray)


def findClosest(inpMat):
    diff = sys.maxint
    k = len(inpMat)
    maxLen = [0] * k
    for i in range(k):
        maxLen[i] = len(inpMat[i])

    currentIndex = [0] * k
    bestIndex = [0] * k
    while allArrayWithinLimit(maxLen, currentIndex):
        minimum, arraysIndex = getMinimum(inpMat, currentIndex)
        maximum = getMaximum(inpMat, currentIndex)

        if maximum - minimum < diff:
            bestIndex = currentIndex[:]
            diff = maximum - minimum

        if diff is 0:
            break

        currentIndex[arraysIndex] += 1

    for i in range(k):
        print (inpMat[i][bestIndex[i]]),


if __name__ == "__main__":
    inpMat = [[1, 4, 10],
              [2, 15, 20],
              [10, 12]]
    # inpMat = [[20, 24, 100],
    #           [2, 19, 22, 79, 800],
    #           [10, 12, 23, 24, 119]]
    findClosest(inpMat)
