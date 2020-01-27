# Question : Given a string, the task is to find maximum consecutive repeating character in string.
# https://www.geeksforgeeks.org/maximumConsecutiveRepeatingCharacterString/
#
# Examples:
# Input : str = "geeekk"
# Output : e
# Input : str = "aaaabbcbbb"
# Output : a
#
# Question Type : Easy
# Used : Running counter is used since the input string is sorted.
# Complexity : O(n)


def maxRepeating(inpStr):
    count = 0
    currCount = 1
    result = ''

    for i in range(len(inpStr)):
        if i < len(inpStr)-1 and inpStr[i] == inpStr[i+1]:
            currCount += 1
        else:
            if currCount > count:
                count = currCount
                result = inpStr[i]
            currCount = 1
    return result


if __name__ == "__main__":
    inpStr = "aaaabbaaccde"
    print("most repeating character :", maxRepeating(inpStr))
