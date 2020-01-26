# Question : Given a string str and another string patt. Find the character in patt that is present at the
# minimum index in str. If no character of patt is present in str then print 'No character present'.
#
# Input : str = "geeksforgeeks"
#         patt = "set"
# Output : e
# Both e and s of patt are present in str, but e is present at minimum index, which is 1.
#
# Question Type : Easy
# Used : Make a hash dict of str. Now loop over element of pattern, for each char get the corresponding
#        index from dict and update min Index if required
# Complexity : O(n)

import sys


def minIndexChar(str, patt):
    minIndex = sys.maxsize
    hashDict = dict()
    for i in range(len(str)):
        if str[i] not in hashDict.keys():
            hashDict[str[i]] = i

    for ele in patt:
        if ele in hashDict.keys():
            minIndex = min(minIndex, hashDict[ele])

    if minIndex != sys.maxsize:
        return minIndex
    else:
        return None


if __name__ == "__main__":
    str = "geeksforgeeks"
    patt = "set"
    print(minIndexChar(str, patt))
