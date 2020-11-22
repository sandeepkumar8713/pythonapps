# https://leetcode.com/discuss/interview-question/370112/
# Question : Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.
#
# Example : Input: s = "abcabc", k = 3
# Output: ["abc", "bca", "cab"]
#
# Question Type : ShouldSee
# Used : Map a charMap dict, where key is char and value is last found index. Maintain currSubStrStart which points to
#        the start of substring we are trying to make in given inpStr. Loop over the inpStr. While doing so check if
#        this current char has appeared before. If yes, then we have to update currSubStrStart to previously found
#        index + 1, as we have encountered same char and we should start making substring after first found character.
#        While loop also check if diff b/w current index and currSubStrStart is equal to k. If yes, we found a
#        substring, append this in the result set.
#        subStringK(inpStr, k):
#        charMap = dict(), resultSet = set()
#        currSubStrStart = 0
#        for i in range(len(inpStr)):
#           if inpStr[i] in charMap and charMap[inpStr[i]] >= currSubStrStart:
#               currSubStrStart = charMap[inpStr[i]] + 1
#           charMap[inpStr[i]] = i
#            if i - currSubStrStart + 1 == k:
#               resultSet.add(inpStr[currSubStrStart:i + 1])
#               currSubStrStart += 1
#        return list(resultSet)
# Complexity : O(n)


def subStringK(inpStr, k):
    if not inpStr or k == 0:
        return []

    charMap = dict()
    resultSet = set()
    currSubStrStart = 0
    for i in range(len(inpStr)):
        if inpStr[i] in charMap and charMap[inpStr[i]] >= currSubStrStart:
            currSubStrStart = charMap[inpStr[i]] + 1
        charMap[inpStr[i]] = i
        if i - currSubStrStart + 1 == k:
            resultSet.add(inpStr[currSubStrStart:i + 1])
            currSubStrStart += 1
    return list(resultSet)


if __name__ == "__main__":
    s = "abcabc"
    k = 3
    print(subStringK(s, k))
