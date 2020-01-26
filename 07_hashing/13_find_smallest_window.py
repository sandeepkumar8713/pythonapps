# Question : Given two strings string1 and string2, find the smallest substring in string1 containing all
# characters of string efficiently.
#
# Input : string = "this is a test string"
# pattern = "tist"
# Output :  Minimum window is "t stri"
#
# Question Type : Generic, SimilarAdded
# Used : Loop over the pattern and add the elements to hashPatt along with frequency.
#        hashStr represents the sliding window. Take start as 0.
#        Loop over the string and add the elements to hashString along with frequency. If ele is present in hashPatt
#            and freq of ele in hashStr is less than or equal to freq of ele in hashPatt(hashStr[ele] <= hashPatt[ele])
#            then increase the count. If count is equal to length of pattern, then we have found the pattern in this
#            window. Now we need to reduce the size of window from left side by removing not matching or repeated ele.
#            Loop while inpStr[start] is not in hashPatt or hashStr[inpStr[start]] > hashPatt[inpStr[start]]
#               decrement starts freq from hashStr and increment start by 1
#            Update the minWindow, size if current window is less than minWindow and keep startIndex
#        print minWindow
# Complexity : O(n)


import sys


def findMinWindow(inpStr, patt):
    hashPatt = dict()
    hashStr = dict()
    for ele in patt:
        if ele in hashPatt.keys():
            hashPatt[ele] += 1
        else:
            hashPatt[ele] = 1

    start = 0
    count = 0
    j = 0
    minWindowLen = sys.maxsize
    minStartIndex = -1

    for ele in inpStr:
        if ele in hashStr.keys():
            hashStr[ele] += 1
        else:
            hashStr[ele] = 1

        if ele in hashPatt.keys() and hashStr[ele] <= hashPatt[ele]:
            count += 1

        if count == len(patt):
            while inpStr[start] not in hashPatt.keys() or hashStr[inpStr[start]] > hashPatt[inpStr[start]]:
                hashStr[inpStr[start]] -= 1
                start += 1

            windowLen = j - start + 1
            if windowLen < minWindowLen:
                minWindowLen = windowLen
                minStartIndex = start

        j += 1

    if minStartIndex is -1:
        print("Not found")
    else:
        print(inpStr[minStartIndex:minStartIndex + minWindowLen])


if __name__ == "__main__":
    string = "this is a test string"
    pattern = "tist"
    findMinWindow(string, pattern)

