# Question : Given an unsorted array of integers, find a subarray which adds to a given number. If there are more
# than one sub arrays with sum as the given number,print any of them
#
# Used : Do cumulative sum over the array and keep saving in dict as cumuSave and index.
#        Now while looping check if difference of current cumulative sum and target sum is present in the map
#        if cumuSum == targetSum: return 0, i
#        if (cumuSum - targetSum) in cumuSumMap: return cumuSumMap[cumuSum - targetSum] + 1, i
# Complexity : 0(n)


def subArraySum(arr,targetSum):
    cumuSum = 0
    cumuSumMap = dict()
    for i in xrange(len(arr)):
        cumuSum += arr[i]

        if cumuSum == targetSum:
            return 0, i

        if cumuSum - targetSum in cumuSumMap:
            return cumuSumMap[cumuSum - targetSum] + 1, i

        cumuSumMap[cumuSum] = i

    return -1, -1


if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    targetSum = -10

    # arr = [1, 2, 3, 7, 5]
    # targetSum = 12

    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # targetSum = 15

    print subArraySum(arr, targetSum)
