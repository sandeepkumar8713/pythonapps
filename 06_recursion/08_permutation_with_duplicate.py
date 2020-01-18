# CTCI : Q8_08_Permutations_With_Dups
# https://www.geeksforgeeks.org/print-all-permutations-of-a-string-with-duplicates-allowed-in-input-string/
# Question : Given a string that may contain duplicates, write a function to print all
# permutations of given string such that no permutation is repeated in output.
#
# Used : Make a freq map of input string.
#       Call a recursive function : printPerms(charMap, prefix, remainingLength, resultList)
#       If remainingLength is 0: append prefix in resultList and return
#       Loop over the characters in charMap, if its freq > 0: decrement the freq, add call the function again:
#           printPerms(charMap, prefix + c, remainingLength - 1, resultList)
#           decrement the freq
#       Note : count is : n!/(repeatedCount!)
# Complexity : O(n!)


def buildFreqTable(inpStr):
    charMap = {}
    for c in inpStr:
        if c in charMap:
            charMap[c] += 1
        else:
            charMap[c] = 1
    return charMap


def printPerms(charMap, prefix, remainingLength, resultList):
    if remainingLength == 0:
        resultList.append(prefix)
        return
    for c in charMap.keys():
        if charMap[c] > 0:
            charMap[c] -= 1
            printPerms(charMap, prefix + c, remainingLength - 1, resultList)
            charMap[c] += 1


def getAllPermuation(inpStr):
    charMap = buildFreqTable(inpStr)
    resultList = []
    printPerms(charMap, "", len(inpStr), resultList)
    return resultList


if __name__ == "__main__":
    #inpStr = "AAB"
    inpStr = "ABCAA"
    resultList = getAllPermuation(inpStr)
    print (resultList)
    print (len(resultList))
