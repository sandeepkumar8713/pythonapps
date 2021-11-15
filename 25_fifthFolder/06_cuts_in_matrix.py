# https://careercup.com/question?id=5643784826650624
# Question : Given a binary matrix of size M * N. You are given H and V where H denotes the number of horizontal
# cuts and V represents number of vertical cuts. You need to find whether you can make H and V amount of cuts
# such that each sub-matrix formed after the cuts will have equal number of 1.
#
# Example :
# Input :
# 4 5
# 1 1 1 1 1
# 0 0 1 1 1
# 0 1 1 1 1
# 1 0 1 1 1
# Given H=1 and V=3, we can make 1st horizontal cut after 2nd row and 3 vertical cuts after 2nd, 3rd and 4th
# column such that each of the sub matrix will have equal number of 1s.
# Output :
# | ----------------|
# | 1 1 | 1 | 1 | 1 |
# | 0 0 | 1 | 1 | 1 |
# | ----------------|
# | 0 1 | 1 | 1 | 1 |
# | 1 0 | 1 | 1 | 1 |
# | ----------------|
#
# Question Type : Generic
# Used : Do Pre-processing on the given inpMat, find row-wise and column-wise sum.
#        Also sum of the matrix element. Check if H and V cuts will equally distribute
#        the elements. (totalSum % (H+1) == 0)
#        If yes, then loop over the row-size sum elements and check if its sum is equal to
#        the sectionSum(average).
#        Logic :
#        makeCuts(rowSum, sectionSum, cuts, cutIndexes):
#        runningSum = 0, cutsMade = False
#        for i in range(len(rowSum)):
#           runningSum += rowSum[i]
#           if runningSum > sectionSum: break
#           if runningSum == sectionSum:
#               runningSum = 0, cuts -= 1
#               if i != len(rowSum) - 1: cutIndexes.append(i+1)
#               if cuts == 0: cutsMade = True, break
#        return cutsMade
#
#        if totalSum % (H+1) == 0 and makeCuts(rowSum, totalSum/(H+1), H, hCutIndexes):
#           print("Horizontal Cuts :", hCutIndexes)
#        else:
#           print("Horizontal Cuts 0")
#        if totalSum % (V+1) == 0 and makeCuts(colSum, totalSum / (V + 1), V, vCutIndexes):
#           print("Vertical Cuts :", vCutIndexes)
#        else:
#           print("Vertical Cuts 0")
# Complexity : O(n^2)

def makeCuts(rowSum, sectionSum, cuts, cutIndexes):
    runningSum = 0
    cutsMade = False
    for i in range(len(rowSum)):
        runningSum += rowSum[i]
        if runningSum > sectionSum:
            break
        if runningSum == sectionSum:
            runningSum = 0
            cuts -= 1
            if i != len(rowSum) - 1:
                cutIndexes.append(i+1)
            if cuts == 0:
                cutsMade = True
                break

    return cutsMade


def determineCutIndexes(inpMat, H, V):
    totalSum = 0
    rowSum = []
    for row in inpMat:
        totalSum += sum(row)
        rowSum.append(sum(row))

    colSum = []
    for j in range(len(inpMat[0])):
        runningSum = 0
        for i in range(len(inpMat)):
            runningSum += inpMat[i][j]
        colSum.append(runningSum)

    hCutIndexes = []
    vCutIndexes = []
    if totalSum % (H+1) == 0 and makeCuts(rowSum, totalSum/(H+1), H, hCutIndexes):
        print("Horizontal Cuts :", hCutIndexes)
    else:
        print("Horizontal Cuts 0")

    if totalSum % (V+1) == 0 and makeCuts(colSum, totalSum / (V + 1), V, vCutIndexes):
        print("Vertical Cuts :", vCutIndexes)
    else:
        print("Vertical Cuts 0")


if __name__ == "__main__":
    H = 1
    V = 3
    inpMat = [[1, 1, 1, 1, 1],
              [0, 0, 1, 1, 1],
              [0, 1, 1, 1, 1],
              [1, 0, 1, 1, 1]]
    determineCutIndexes(inpMat, H, V)

    print("-----------------------")

    H = 1
    V = 3
    inpMat = [[1, 1, 1, 0, 0],
              [1, 1, 1, 0, 0],
              [0, 0, 1, 1, 1],
              [0, 0, 1, 1, 1]]
    determineCutIndexes(inpMat, H, V)
