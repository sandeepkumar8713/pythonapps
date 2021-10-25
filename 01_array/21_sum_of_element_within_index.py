# https://stackoverflow.com/questions/2473114/how-to-find-sum-of-elements-from-given-index-interval-i-j-in-constant-time
# Question : Given an array. How can we find sum of elements in index interval (i, j) in constant time.
# You are allowed to use extra space.
#
# Input : 3 2 4 7 1 -2 8 0 -4 2 1 5 6 -1 , index : 2, 5
# Output : 10
#
# Question Type : Easy
# Used : Make cumulative sum for given input from length n+1.
#        such as : cumulativeSumArray[i] = cumulativeSumArray[i-1] + arr[i-1]
#        To get the required sum do :
#           return cumulativeSumArray[stopIndex + 1] - cumulativeSumArray[startIndex]
#        Note that cumulativeSumArray is 1 step late,
#        arr[i] is stored in cumulativeSumArray[i+1]
# Complexity : Preparation : O(n) Calculation : O(1)


def makeCumulativeArray(arr):
    cumulativeSumArray = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        cumulativeSumArray[i] = cumulativeSumArray[i-1] + arr[i-1]
    return cumulativeSumArray


def getSum(cumulativeSumArray, startIndex, stopIndex):
    return cumulativeSumArray[stopIndex + 1] - cumulativeSumArray[startIndex]


if __name__ == "__main__":
    arr = [3, 2, 4, 7, 1, -2, 8, 0, -4, 2, 1, 5, 6, -1]
    cumulativeSumArray = makeCumulativeArray(arr)
    print(cumulativeSumArray)
    print(getSum(cumulativeSumArray, 2, 5))   # 4,7,1,-2
    print(getSum(cumulativeSumArray, 0, 13))  # All
