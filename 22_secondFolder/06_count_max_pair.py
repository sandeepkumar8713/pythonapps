# Question : Given an array arr[], count number of pairs arr[i], arr[j] such that
# arr[i] + arr[j] is maximum and i < j.
#
# Question Type : ShouldSee
# Used : Keep count of running maxCount and secondMaxCount.
#        if (maxCount > 1):
#           return maxCount * (maxCount - 1) / 2
#        return secondMaxCount
#
#        sum(a, n):
#        maxVal = a[0], maxCount = 1
#        secondMax = sys.maxsize
#        for i in range(1, n):
#           if (a[i] == maxVal):
#               maxCount += 1
#           elif (a[i] > maxVal):
#               secondMax = maxVal
#               secondMaxCount = maxCount
#               maxVal = a[i]
#               maxCount = 1
#           elif (a[i] == secondMax):
#               secondMax = a[i]
#               secondMaxCount += 1
#           elif (a[i] > secondMax):
#               secondMax = a[i]
#               secondMaxCount = 1
#        if (maxCount > 1):
#           return maxCount * (maxCount - 1) / 2
#        return secondMaxCount
# Complexity : O(n)

import sys


def sum(a, n):
    # Find maximum and second maximum elements.
    # Also find their counts.
    maxVal = a[0];
    maxCount = 1
    secondMax = sys.maxsize

    for i in range(1, n):

        if (a[i] == maxVal):
            maxCount += 1

        elif (a[i] > maxVal):
            secondMax = maxVal
            secondMaxCount = maxCount
            maxVal = a[i]
            maxCount = 1

        elif (a[i] == secondMax):
            secondMax = a[i]
            secondMaxCount += 1

        elif (a[i] > secondMax):
            secondMax = a[i]
            secondMaxCount = 1

    # If maximum element appears more than once.
    if (maxCount > 1):
        return maxCount * (maxCount - 1) / 2

    # If maximum element appears only once.
    return secondMaxCount


if __name__ == "__main__":
    array = [1, 1, 1, 2, 2, 2, 3]
    n = len(array)
    print(sum(array, n))
