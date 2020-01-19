# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
# Question : Given a string you need to print longest possible substring that has exactly M unique characters.
# If there are more than one substring of longest possible length, then print any one of them.
#
# Question Type : Easy
# Used : Take a sliding window, traverse over the string and keep track of largest window found yet.
#        Take two endpoints of window wLeft, wRight as 0. Also keep track of uniqueCount in window.
#        Maintain a dict myMap to keep track of char and their frequency.
#        Loop while wRight is less than n.
#           If uniqueCount <= m then, if arr[wRight] in myMap, increment its frequency in myMap and increment zeroCount,
#               else increment uniqueCount by 1 and push this char in myMap. Increment window in right side.
#           If uniqueCount > m then check if arr[wLeft] is in myMap. If true decrement its freq in myDict by 1. If its
#               freq is 0, decrement uniqueCount by 1 and delete from myMap. Increment window in left side.
#           Update max window size by comparing it with (wRight - wLeft)
#       return inpStr[bestLeft:bestLeft + bestWindow]
# Complexity : O(n)


def findLongest(inpStr, m):
    n = len(inpStr)
    wLeft = 0
    wRight = 0

    bestLeft = bestWindow = 0
    uniqueCount = 0
    myMap = dict()

    while wRight < n:
        if uniqueCount <= m:
            if inpStr[wRight] not in myMap.keys():
                uniqueCount += 1
                myMap[inpStr[wRight]] = 1
            else:
                myMap[inpStr[wRight]] += 1
            wRight += 1

        if uniqueCount > m:
            if inpStr[wLeft] in myMap.keys():
                myMap[inpStr[wLeft]] -= 1
                if myMap[inpStr[wLeft]] == 0:
                    uniqueCount -= 1
                    del myMap[inpStr[wLeft]]
            wLeft += 1

        if (wRight - wLeft) > bestWindow:
            bestWindow = wRight - wLeft
            bestLeft = wLeft

    print(inpStr[bestLeft:bestLeft + bestWindow])


if __name__ == "__main__":
    findLongest("aabbb", 1)
    findLongest("aabbcc", 3)
