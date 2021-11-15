# https://leetcode.com/problems/remove-duplicate-letters/
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Question : Given a string s, remove duplicate letters so that every letter appears once and
# only once. You must make sure your result is the smallest in lexicographical order among
# all possible results.
#
# Example : Input: s = "cbacdcbc"
# Output: "acdb"
#
# Question Type : Generic
# Used : Make a char freq dict. Make a visited list of len 26.
#        Loop over the given input str, decrement the freq of ch,
#        Skip if current ch has been already visited
#        If last element of res, still has more occurrences to come and it is greater
#          than curr ch, pop it from res and mark it as unvisited.
#        push current ch in res and mark as visited
#        return res
#        Logic :
#        visited = [False] * MAX_CHAR, res = []
#        for i in range(n):
#           index = charToIndex(inpStr[i])
#           map[index] -= 1
#           if visited[index]: continue
#           while len(res) > 0 and map[charToIndex(res[-1])] > 0 and
#               inpStr[i] < res[-1]:
#               visited[charToIndex(res[-1])] = False
#               res.pop()
#           res.append(inpStr[i])
#           visited[index] = True
#        return "".join(res)
# Complexity : O(n)

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


def removeDuplicate(inpStr):
    if inpStr is None or len(inpStr) == 0:
        return ""

    n = len(inpStr)
    map = dict()
    for ch in inpStr:
        index = charToIndex(ch)
        map[index] = map.get(index, 0) + 1

    visited = [False] * MAX_CHAR
    res = []
    for i in range(n):
        index = charToIndex(inpStr[i])
        map[index] -= 1

        if visited[index]:
            continue

        # move window
        # if last element of res is greater than curr element, pop out
        while len(res) > 0 and map[charToIndex(res[-1])] > 0 and inpStr[i] < res[-1]:
            visited[charToIndex(res[-1])] = False
            res.pop()

        res.append(inpStr[i])
        visited[index] = True

    return "".join(res)


if __name__ == "__main__":
    s = "cbacdcbc"
    print(removeDuplicate(s))

    s = "bcabc"
    print(removeDuplicate(s))
