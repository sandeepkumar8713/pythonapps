# https://careercup.com/question?id=5743979809734656
# Question : We need to remove parenthesis if complete string enclose with otherwise return same string.
#
# Example :
# (((abc))) --> abc
# (ab(c)) --> ab(c)
# (abc09%(c)) --> abc09%(c)
# ab(c) --> ab(c)
# (ab)c --> (ab)c
# abc(c)) → INVALID
# (abc)(def) --> (abc)(def)
# (abc)typ(def) --> (abc)typ(def)
# ((abc)(def)) --> (abc)(def)
#
# Question Type : ShouldSee
# Used : Loop over the given inpStr, if ( occurs, push its position from the right side in stack. If ) occurs pop top
#        value from stack. If top value is same as current position, then the substring b/w start and end is balanced
#        it can be the answer.
#        for i in range(0, len(inpStr)):
#           if inpStr[i] == '(': stack.append(len(inpStr) - 1 - i)
#           elif inpStr[i] == ')':
#               if len(stack) == 0: return "Invalid"
#               else:
#                   top = stack.pop()
#                   if top == i:
#                       start += 1, end -= 1
#        return inpStr[start:end+1]
# Complexity : O(n)

def removeOuterParens(inpStr):
    stack = []
    start = 0
    end = len(inpStr) - 1
    for i in range(0, len(inpStr)):
        if inpStr[i] == '(':
            stack.append(len(inpStr) - 1 - i)
        elif inpStr[i] == ')':
            if len(stack) == 0:
                return "Invalid"
            else:
                top = stack.pop()
                if top == i:
                    start += 1
                    end -= 1

    if len(stack) != 0:
        return "Invalid"
    return inpStr[start:end+1]


if __name__ == "__main__":
    print(removeOuterParens("(((abc)))"))
    print(removeOuterParens("(ab(c))"))
    print(removeOuterParens("(abc09%(c))"))
    print(removeOuterParens("ab(c)"))
    print(removeOuterParens("abc(c))"))
    print(removeOuterParens("(abc(c)"))
    print(removeOuterParens("(ab)c"))
    print(removeOuterParens("(abc)(def)"))
    print(removeOuterParens("(abc)typ(def)"))
    print(removeOuterParens("((abc)(def))"))
