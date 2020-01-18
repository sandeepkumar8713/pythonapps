# https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/
# Question : Given a string, find the first non-repeating character in it. For example, if the input string is
# "GeeksforGeeks", then output should be 'f'
#
# Used : Used a map to store each character as key and count & index as its value. Loop again to find the first
#        character with count 1 and return
# Complexity : O(n)


def makeTable(inpStr):
    strMap = dict()
    for i in range(len(inpStr)):
        if inpStr[i] in strMap:
            strMap[inpStr[i]]['count'] += 1
        else:
            strMap[inpStr[i]] = {"count": 1, "index": i}
    return strMap


def firstNonRepeat(inpStr):
    strMap = makeTable(inpStr)

    for i in range(len(inpStr)):
        if strMap[inpStr[i]]['count'] == 1:
            return strMap[inpStr[i]]['index']
    return -1


if __name__ == "__main__":
    inpStr = "geeksforgeeks"
    print 'First non repeating character =', firstNonRepeat(inpStr)
