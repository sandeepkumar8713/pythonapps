# CTCI : Q8_09_Parens
# https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/
# Question : Write a function to generate all possible n pairs of balanced parentheses.
#
# Used : Call a function : recur(strList, pos, n, open, close) where strList = [''] * 2n,
#        pos = 0, open = 0, close = 0
#           if close == n : print contents of strList and return
#           if open > close : add '}' in strList at pos, then call recur(strList, pos + 1, n, open, close + 1)
#           if open < n : add '{' in strList at pos, the call recur(strList, pos + 1, n, open + 1, close)
#        Note : Combination count : catalan(n)
# Complexity : O(n * catalan(n))


def printParenthesis(strList, n):
    if n > 0:
        printParenthesisRecur(strList, 0, n, 0, 0)


def printParenthesisRecur(strList, pos, n, open, close):
    if close == n:
        result = ""
        print (result.join(strList))
        return

    if open > close:
        strList[pos] = '}'
        printParenthesisRecur(strList, pos + 1, n, open, close + 1)

    if open < n:
        strList[pos] = '{'
        printParenthesisRecur(strList, pos + 1, n, open + 1, close)


if __name__ == "__main__":
    n = 3
    strList = [''] * 2 * n
    printParenthesis(strList, n)
