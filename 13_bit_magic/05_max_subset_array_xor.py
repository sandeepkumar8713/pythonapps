# https://www.geeksforgeeks.org/find-maximum-subset-xor-given-set/
# Question : Given an set of positive integers. find the maximum XOR subset value in the given set.
# Expected time complexity O(n).
#
# Input: set[] = {2, 4, 5}
# Output: 7
# The subset {2, 5} has maximum XOR value
#
# Question Type : Generic
# Used : Set index as 0
#        Run a loop from 31 to 0
#           Set max as -intMax
#           Find max element with i'th bit set
#           if max element not found skip
#           swap max element with index element and maxIndex with index
#           Do Xor operation of all the elements whose i'th bit is set with swapped maxIndex and update arr[j]
#           Increment index by 1
#        Do Xor over all the element, this will give the result
# Logic: index = 0
#        for i in range(INT_BITS-1, -1, -1):
#           maxInd = index
#           maxEle = -sys.maxint
#           for j in range(index, n):
#               if (arr[j] & (1 << i)) != 0 and arr[j] > maxEle:
#                   maxEle = arr[j]
#                   maxInd = j
#           if maxEle == -sys.maxint:
#               continue
#           temp = arr[index]
#           arr[index] = arr[maxInd]
#           arr[maxInd] = temp
#           maxInd = index
#           for j in range(n):
#               if j != maxInd and (arr[j] & (1 << i)) != 0:
#                   arr[j] = arr[j] ^ arr[maxInd]
#           index += 1
#        res = 0
#        for i in range(n):
#           res = res ^ arr[i]
#        return res
# Complexity : O(n)


INT_BITS = 32
import sys


def maxSubarrayXOR(arr, n):
    index = 0
    # Run a loop from 31 to 0
    for i in range(INT_BITS-1, -1, -1):
        maxInd = index
        maxEle = -sys.maxsize
        # Find max element with i'th bit set
        for j in range(index, n):
            if (arr[j] & (1 << i)) != 0 and arr[j] > maxEle:
                maxEle = arr[j]
                maxInd = j

        # if max element not found skip
        if maxEle == -sys.maxsize:
            continue

        # swap max element with index element
        temp = arr[index]
        arr[index] = arr[maxInd]
        arr[maxInd] = temp
        maxInd = index

        # Do Xor operation of all the elements whose i'th bit is set with swapped maxIndex and update arr[j]
        for j in range(n):
            if j != maxInd and (arr[j] & (1 << i)) != 0:
                arr[j] = arr[j] ^ arr[maxInd]

        # increment index by 1
        index += 1

    # Do Xor over all the element, this will give the result
    res = 0
    for i in range(n):
        res = res ^ arr[i]
    return res


if __name__ == "__main__":
    arr = [9, 8, 5]
    n = len(arr)
    print(maxSubarrayXOR(arr, n))
