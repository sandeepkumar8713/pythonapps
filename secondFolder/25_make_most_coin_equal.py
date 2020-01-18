# Question : Given piles of coins of different heights and a separate pile of height x. Find out the maximum
# number of piles, which can be made same of height by distributing coins from separate pile of height x.
#
# input : 3, 10, 7, 9, 100   separatePileHeight = 4
# Output : 3
# Explanation :
# 3, 7, 9, 10, 100 (sort)
# 97 93 91 90   0  here sameCount is 1
#
# 7 3 1 0 -90      here sameCount is 3 (for 0, 1, 3)
#
#
# Used : Sort the given inpArr. Run a loop in reverse i : n-1 to 0. Take inpArr[i], Subtract it from all the elements
#           in inpArr and dave the difference in diffArr. Now run a loop j : i to 0 and try to make most diffArr[j] as
#               0 and keep decrementing remainingPileHeight accordingly and keep incrementing sameCount by 1.
#               If remainingPileHeight is not as big as diffArr[j] then break.
#           compare maxCount with sameCount and update if required.
#        return maxCount
# Complexity : O(n)


def maxSameHeight(inpArr, otherPileHeight):
    inpArr.sort()
    maxCount = 0
    for i in range(len(inpArr)-1, -1, -1):
        diffArr = []
        remainingPileHeight = otherPileHeight
        sameCount = 0
        for item in inpArr:
            diffArr.append(inpArr[i] - item)

        # Make most zero
        for j in range(i, -1, -1):
            if remainingPileHeight >= diffArr[j]:
                remainingPileHeight -= diffArr[j]
                sameCount += 1
            else:
                break

        maxCount = max(maxCount, sameCount)

    return maxCount


if __name__ == "__main__":
    inpArr = [3, 10, 7, 9, 100]
    otherPileHeight = 4
    print maxSameHeight(inpArr, otherPileHeight)
