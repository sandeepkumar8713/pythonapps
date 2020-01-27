# Question : Given an expression exp of length n consisting of some brackets. The task is to print the bracket
# numbers when the expression is being parsed.
#
# Input : (a+(b*c))+(d/e)
# Output : 1 2 2 1 3 3
#
# Question Type : Easy
# Used : traverse through the expression, if '(' is found increment bracket number by 1, print it and append in list
#        if ')' is found , pop a last element from list, print it
# Complexity : O(n)


def printBracketNumber(expr):
    bracketNumList = []
    bracketNumber = 0
    for item in expr:
        if item == '(':
            bracketNumber += 1
            print(bracketNumber, end=" ")
            bracketNumList.append(bracketNumber)

        if item == ')':
            print(bracketNumList.pop(), end=" ")


if __name__ == "__main__":
    expr = "(a+(b*c))+(d/e)"
    printBracketNumber(expr)
