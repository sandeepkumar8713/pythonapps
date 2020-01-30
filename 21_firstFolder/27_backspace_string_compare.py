# https://leetcode.com/problems/backspace-string-compare/
# Question : Given two strings S and T, return if they are equal when both are typed into empty text
# editors. # means a backspace character.
#
# Example : Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
# Question Type : ShouldSee
# Used : Traverse the inpStr in reverse and skip the characters succeeded by 0.
#        Logic : def getEndResult(inpStr):
#        pendingDelete = 0
#        result = ""
#        for i in range(len(inpStr) - 1, -1, -1):
#           if inpStr[i] == "#":
#               pendingDelete += 1
#           elif pendingDelete > 0:
#               pendingDelete -= 1
#               continue
#           else: result = inpStr[i] + result
#        return result
# Complexity : O(n)


def getEndResult(inpStr):
    pendingDelete = 0
    result = ""
    for i in range(len(inpStr) - 1, -1, -1):
        if inpStr[i] == "#":
            pendingDelete += 1
        elif pendingDelete > 0:
            pendingDelete -= 1
            continue
        else:
            result = inpStr[i] + result

    return result


def backspaceStringCompare(S,T):
    resS = getEndResult(S)
    resT = getEndResult(T)
    return resS == resT


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print(backspaceStringCompare(S, T))
