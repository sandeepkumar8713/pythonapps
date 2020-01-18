# https://www.geeksforgeeks.org/reverse-individual-words/
# Question : Given a string str, we need to print reverse of individual words.
#
# Input : Hello World
# Output : olleH dlroW
#
# Used : Loop over the input string. If the char is not ' ' push it in stack.
#           If char is ' ', pop all the elements from the stack and append to new String with space
# Complexity : O(n)


def reverseword(inpString):
    stack = []
    res = ''
    for ch in inpString:
        if ch != ' ':
            stack.append(ch)
        else:
            while len(stack) != 0:
                res += stack.pop()
            res += ch

    while len(stack) != 0:
        res += stack.pop()
    print res


if __name__ == "__main__":
    inpString = "Hello World Sandeep"
    reverseword(inpString)

