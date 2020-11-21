# https://leetcode.com/discuss/interview-question/865660/
# Question : Amazon would like to know how much inventory exists in their closed inventory compartments.
# Given a string a consisting of items as "*" and closed compartments as an open and close "|", an array
# of starting indices startIndices, and an array of ending indices endIndices, determine the number of items
# in closed compartments within the substring between the two indices.
#
# Example :
# Input : s = "|**|*|*"
# startIndices = [1, 1]
# endIndices = [5, 6]
# Output = [2, 3]
#
# Question Type : Easy
# Used : Make a map, based on inpStr. Key is index of "|". Value is count "*" between this key and previous key.
#        Now loop over the given index array and find the required value and append in result.
#        getItemCount(myMap, startIndices, endIndices):
#        result = [0] * len(startIndices)
#        for i in range(len(startIndices)):
#           startIndex = startIndices[i] - 1
#           endIndex = endIndices[i] - 1
#           while startIndex not in myMap:
#               startIndex += 1
#           while endIndex not in myMap:
#               endIndex -= 1
#           for key in range(startIndex + 1, endIndex + 1):
#               if key in myMap:
#                   result[i] += myMap[key]
#        return result
# Complexity : O(n)


def getItemCount(myMap, startIndices, endIndices):
    result = [0] * len(startIndices)

    for i in range(len(startIndices)):
        startIndex = startIndices[i] - 1
        endIndex = endIndices[i] - 1

        while startIndex not in myMap:
            startIndex += 1
            if startIndex == len(inpStr):
                break

        while endIndex not in myMap:
            endIndex -= 1
            if endIndex < 0:
                break

        if not(0 <= startIndex < len(inpStr) and 0 <= endIndex < len(inpStr)) or \
                startIndex == endIndex:
            continue

        for key in range(startIndex + 1, endIndex + 1):
            if key in myMap:
                result[i] += myMap[key]

    return result


def countClosedItems(inpStr, startIndices, endIndices):
    myMap = dict()
    tempItemCount = 0
    firstCompartment = True
    for i in range(len(inpStr)):
        if inpStr[i] == "|":
            if firstCompartment:
                myMap[i] = 0
                firstCompartment = False
            else:
                myMap[i] = tempItemCount
            tempItemCount = 0
        else:
            tempItemCount += 1

    return getItemCount(myMap, startIndices, endIndices)


if __name__ == "__main__":
    inpStr = "|**|*|*"
    startIndices = [1, 1]
    endIndices = [5, 6]
    print(countClosedItems(inpStr, startIndices, endIndices))

    inpStr = "*|*|"
    startIndices = [1]
    endIndices = [3]
    print(countClosedItems(inpStr, startIndices, endIndices))

    inpStr = "*|*"
    startIndices = [1]
    endIndices = [3]
    print(countClosedItems(inpStr, startIndices, endIndices))

    inpStr = "****|*|"
    startIndices = [1, 5, 3]
    endIndices = [4, 7, 7]
    print(countClosedItems(inpStr, startIndices, endIndices))
