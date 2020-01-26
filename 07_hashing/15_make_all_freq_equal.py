# Question : Given a string which contains lower alphabetic characters, we need to remove at most one character
# from this string in such a way that frequency of each distinct character becomes same in the string.
#
# Input  : str = "xyyz"
# Output : Yes
# We can remove character 'y' from above string to make the frequency of each character same.
#
# Question Type : ShouldSee
# Used : Loop over the elements in input array and update its frequency in hashDict.
#        Find the minimum frequency.
#        Loop over the list of frequencies and find the diff between minValue and current value. If diff is more than 1
#           return False. If diff is equal to 1 then allow for once. If diff is equal to 1 again then return False.
#        If loop is over, return True
# Complexity : O(n)


def makeSameFreq(inpStr):
    hashDict = dict()
    for ele in inpStr:
        if ele in hashDict.keys():
            hashDict[ele] += 1
        else:
            hashDict[ele] = 1

    valueList = hashDict.values()
    minValue = min(valueList)

    alreadyOnceAllowed = False
    for value in valueList:
        diff = value - minValue
        if diff > 1:
            return False
        elif diff == 1:
            if alreadyOnceAllowed:
                return False
            alreadyOnceAllowed = True

    return True


if __name__ == "__main__":
    inpStr = "xyyz"
    print(makeSameFreq(inpStr))

    inpStr = "xyyzz"
    print(makeSameFreq(inpStr))

    inpStr = "xxxxyyzz"
    print(makeSameFreq(inpStr))
