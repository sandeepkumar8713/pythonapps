# https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/
# Question : Given an array of integers, find any one combination of four elements in the array whose sum is
# equal to a given value X.
#
# Question Type : Easy
# Used : Run 2 loops to make pairs from the given array. Save its sum as key and indexes as value in map.
#        Now again run 2 loops to make pair, subtract this pair's sum with target sum, check if other
#        part sum is present in the map. Check if indexes are repeated, if not return the result.
# Complexity : O(n^2 * log n)


def findFourElements(inpArr, targetSum):
    n = len(inpArr)
    sumMap = dict()
    for i in range(n-1):
        for j in range(i+1, n):
            sumMap[inpArr[i] + inpArr[j]] = [i,j]

    for i in range(n-1):
        for j in range(i+1, n):
            firstPart = inpArr[i] + inpArr[j]

            if (targetSum - firstPart) in sumMap.keys():
                firstPairIndexes = sumMap[targetSum - firstPart]
                if firstPairIndexes[0] != i and firstPairIndexes[0] != j and firstPairIndexes[1] != i and firstPairIndexes[1] != j:
                        return inpArr[firstPairIndexes[0]], inpArr[firstPairIndexes[1]], inpArr[i], inpArr[j]

    return None


if __name__ == "__main__":
    inpArr = [10, 20, 30, 40, 1, 2]
    targetSum = 91
    print(findFourElements(inpArr, targetSum))
