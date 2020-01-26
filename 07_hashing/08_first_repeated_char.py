# Question : Given a string, find the first repeated character in it. We need to find the character that occurs
# more than once and whose index of first occurrence is smallest.
#
# Input:  ch = "geeksforgeeks"
# Output: e
# e is the first element that repeats
#
# Question Type : Easy
# Used : Loop over input string, if char is present in set return char else add char to set.
# Complexity : O(n)


def findFirstRepeat(inpStr):
    hashSet = set()
    for char in inpStr:
        if char in hashSet:
            return char
        else:
            hashSet.add(char)


if __name__ == "__main__":
    inpStr = "geeksforgeeks"
    print("First repeated char:", findFirstRepeat(inpStr))
