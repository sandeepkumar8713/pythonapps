# https://leetcode.com/problems/remove-invalid-parentheses/solution/
# https://leetcode.com/problems/remove-invalid-parentheses/discuss/415004/Python-DFS
# Question : Remove the minimum number of invalid parentheses in order to make the input string valid.
# Return all possible results. Note: The input string may contain letters other than the parentheses ( and ).
#
# Example :  Input: "()())()"
# Output: ["()()()", "(())()"]
#
# Question Type : ShouldSee
# Used : First we read s from left to right and remove all the invalid ). Then we will get multiple
#        candidate solutions and save them in candidates. Then we read each candidate from right
#        to left (reversely) and remove all the invalid ( and we will get the final solutions.
#        Logic : def dfs(inpStr, left, right, paranMap, sols):
#        bal = 0
#        for j in range(right, len(inpStr)):
#           bal += paranMap.get(inpStr[j], 0)
#           if bal < 0:
#               for i in range(left, j + 1):
#                   if paranMap.get(inpStr[i], 0) == -1 and (i == left or paranMap.get(inpStr[i - 1], 0) != -1):
#                       dfs(inpStr[:i] + inpStr[i + 1:], i, j, paranMap, sols)
#               return
#        sols.append(inpStr[::-1])   # Reverse the inpStr if balanced
#        def removeInvalidParentheses(inpStr):
#        candidates = [], solutions = []
#        paranMap = {"(": 1, ")": -1}
#        paranMapRev = {")": 1, "(": -1}
#        dfs(inpStr, 0, 0, paranMap, candidates)
#        for candidate in candidates:
#           dfs(candidate, 0, 0, paranMapRev, solutions)
#        return solutions
# Complexity : O(2^n) worst case


def dfs(inpStr, left, right, paranMap, sols):
    bal = 0
    for j in range(right, len(inpStr)):
        bal += paranMap.get(inpStr[j], 0)
        if bal < 0:
            for i in range(left, j + 1):
                # To check that there should we cut at ) and one before should not be )
                if paranMap.get(inpStr[i], 0) == -1 and (i == left or paranMap.get(inpStr[i - 1], 0) != -1):
                    dfs(inpStr[:i] + inpStr[i + 1:], i, j, paranMap, sols)
            return

    # Reverse the inpStr if balanced
    sols.append(inpStr[::-1])


def removeInvalidParentheses(inpStr):
    candidates = []
    solutions = []
    paranMap = {"(": 1, ")": -1}
    paranMapRev = {")": 1, "(": -1}

    dfs(inpStr, 0, 0, paranMap, candidates)
    for candidate in candidates:
        dfs(candidate, 0, 0, paranMapRev, solutions)
    return solutions


if __name__ == "__main__":
    inpStr = "()())()"
    print(removeInvalidParentheses(inpStr))

    inpStr = ")))"
    print(removeInvalidParentheses(inpStr))
