# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# Question : You are given a string s, a split is called good if you can split s into 2 non-empty
# strings p and q where its concatenation is equal to s and the number of distinct letters in
# p and q are the same. Return the number of good splits you can make in s.
#
# Example : Input: s = "aacaba"
# Output: 2
#
# Question Type : Generic
# Used : For each split, maintain left and right freqDict.
#        Loop over the given str, and push ele in left dict and pop same from rigth dict
#        Compare key count, increment k if equal.
#        return k
#        Logic :
#        for ch in inpStr:
#           rightDict[ch] = rightDict.get(ch, 0) + 1
#        for ch in inpStr:
#           leftDict[ch] = leftDict.get(ch, 0) + 1
#           rightDict[ch] = rightDict.get(ch) - 1
#           if rightDict[ch] == 0: del rightDict[ch]
#           if len(leftDict) == len(rightDict):
#             k += 1
#        return k
# Complexity : O(n)


def goodSplit(inpStr):
    n = len(inpStr)
    if n == 1:  # never splittable
        return 0
    elif n == 2:  # always splittable
        return 1

    k = 0
    leftDict = {}
    rightDict = {}

    for ch in inpStr:
        rightDict[ch] = rightDict.get(ch, 0) + 1

    for ch in inpStr:
        leftDict[ch] = leftDict.get(ch, 0) + 1

        rightDict[ch] = rightDict.get(ch) - 1
        if rightDict[ch] == 0:
            del rightDict[ch]

        if len(leftDict) == len(rightDict):
            k += 1

    return k


if __name__ == "__main__":
    s = "aacaba"
    print(goodSplit(s))

    s = "aaaaa"
    print(goodSplit(s))

    s = "acbadbaada"
    print(goodSplit(s))

    s = "abcd"
    print(goodSplit(s))
