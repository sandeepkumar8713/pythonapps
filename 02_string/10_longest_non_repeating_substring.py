# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# Question : Length of the longest substring without repeating characters
# Given a string, find the length of the longest substring without repeating characters. For example, the longest
# substrings without repeating characters for "ABDEFGABEF" are "BDEFGA" and "DEFGAB", with length 6.
#
# Question Type : Easy
# Used : Keep looping through the input string and appending value in charSet and keep count of running
#        length. If a duplicate char is found, update maxLen if required and reset the running length &
#        empty the charSet.
# Complexity : O(n + d) where n is length of the input string and d is number of characters in input string
#               alphabet(26). d is specified to take into account the time taken to search the element in map.


def nonRepeatSubstr(inpStr):
    charSet = set()
    runningLen = 0
    maxLen = 0
    for item in inpStr:
        if item not in charSet:
            charSet.add(item)
            runningLen += 1
        else:
            if runningLen > maxLen:
                maxLen = runningLen
            del charSet
            charSet = set()
            charSet.add(item)
            runningLen = 0

    return maxLen


if __name__ == "__main__":
    inpStr = "ABDEFGABEF"
    print(nonRepeatSubstr(inpStr))
