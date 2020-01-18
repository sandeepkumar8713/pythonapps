# CTCI : Q17_18_Shortest_Supersequence
# Question : You are given two arrays, one shorter (with all distinct elements) and one
# longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
# array. The items can appear in any order.
#
# Example :
# Input: {1, 5, 9}
# {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}
# Output:[7, 10] (index)
#
# Used : Make a object CountLookup, which keep tracks of weather each element in shorter array has appeared at least
#        once in larger array. Fields : fulfilledCount and freqMap. Now loop over the larger array, it should be
#        like a sliding window, where left side moves only once. But right side moves until the CountLookup is fulfilled
#        i.e. all the shorter array elements have appeared at least once. While running loop, we keep track of smallest
#        sliding window found till now.
#        Logic :
#        bestRange = [], rIndex = 0, countLookup.incrementIfFound(largerArr[rIndex])
#        for lIndex in range(len(largerArr)):
#           index = rIndex + 1
#           while not countLookup.areAllFulfilled() and index < len(largerArr):
#               countLookup.incrementIfFound(largerArr[index])
#               index += 1
#           rIndex = index - 1
#           if not countLookup.areAllFulfilled(): break
#           updateBest(bestRange, [lIndex, rIndex])
#           countLookup.decrementIfFound(largerArr[lIndex])
#        return bestRange
# Complexity : O(n^2)


class CountLookup:
    def __init__(self, arr):
        self.fulfilled = 0
        self.lookup = dict()
        for item in arr:
            self.lookup[item] = 0

    def incrementIfFound(self, value):
        if value not in self.lookup.keys():
            return
        if self.lookup[value] == 0:
            self.fulfilled += 1
        self.lookup[value] += 1

    def decrementIfFound(self, value):
        if value not in self.lookup.keys():
            return
        self.lookup[value] -= 1
        if self.lookup[value] == 0:
            self.fulfilled -= 1

    def areAllFulfilled(self):
        return self.fulfilled == len(self.lookup.keys())


def updateBest(bestPair, currentPair):
    if len(bestPair) is 0:
        bestPair.append(currentPair[0])
        bestPair.append(currentPair[1])
        return
    bestDiff = bestPair[1] - bestPair[0]
    currentDiff = currentPair[1] - currentPair[0]
    if currentDiff < bestDiff:
        bestPair[0] = currentPair[0]
        bestPair[1] = currentPair[1]


def shortestSuperSequence(largerArr, shorterArr):
    if len(shorterArr) > len(largerArr):
        return None
    countLookup = CountLookup(shorterArr)
    bestRange = []
    rIndex = 0
    countLookup.incrementIfFound(largerArr[rIndex])
    for lIndex in range(len(largerArr)):
        index = rIndex + 1
        while not countLookup.areAllFulfilled() and index < len(largerArr):
            countLookup.incrementIfFound(largerArr[index])
            index += 1
        rIndex = index - 1

        if not countLookup.areAllFulfilled():
            break
        # print bestRange, [lIndex, rIndex]
        updateBest(bestRange, [lIndex, rIndex])
        countLookup.decrementIfFound(largerArr[lIndex])

    return bestRange


if __name__ == "__main__":
    largerArr = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    shorterArr = [1, 5, 9]
    print shortestSuperSequence(largerArr, shorterArr)
