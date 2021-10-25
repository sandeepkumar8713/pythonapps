# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# Question : Length of the longest substring without repeating characters
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substrings without repeating characters for "ABDEFGABEF" are "BDEFGA"
# and "DEFGAB", with length 6.
#
# Question Type : ShouldSee
# Used : Maintain char dict, key is char and value is index in inpStr.
#        Loop over the given inpStr.
#        If the char is not present in dict, add it.
#        Else get its old position from the dict. update with new position.
#           Remove all ch's whose pos is less than oldPos.
#        Keep track of max size of dict while looping.
#        After the loop return the maxLen.
#        Logic :
#        for i in range(len(inpStr)):
#           item = inpStr[i]
#           if item not in charSet:
#               charSet[item] = i
#           else:
#               oldPos = charSet[item]
#               charSet[item] = i
#               remove = [ch for ch in charSet if charSet[ch] < oldPos]
#               for ch in remove:
#                   del charSet[ch]
#           if len(charSet) > maxLen:
#               maxLen = len(charSet)
#        return maxLen
# Complexity : O(n) where n is length of the input string


def nonRepeatSubstr(inpStr):
    charSet = dict()
    maxLen = 0
    for i in range(len(inpStr)):
        item = inpStr[i]

        if item not in charSet:
            charSet[item] = i
        else:
            oldPos = charSet[item]
            charSet[item] = i  # new pos

            remove = [ch for ch in charSet if charSet[ch] < oldPos]
            for ch in remove:
                del charSet[ch]

        if len(charSet) > maxLen:
            maxLen = len(charSet)

    return maxLen


if __name__ == "__main__":
    inpStr = "ABDEFGABEF"
    print(nonRepeatSubstr(inpStr))

    inpStr = "ABDEFGAMNOPQRST"
    print(nonRepeatSubstr(inpStr))

    inpStr = "CABDEFGA"
    print(nonRepeatSubstr(inpStr))
