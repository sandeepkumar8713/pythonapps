# https://www.geeksforgeeks.org/print-possible-inpStrs-can-made-placing-spaces/
# Question : Given a inpStr you need to print all possible strings that can be made by placing spaces
# (zero or one) in between them.
#
# Input:  str[] = "ABC"
# Output: ABC
#         AB C
#         A BC
#         A B C
#
# Question Type : Easy
# Used : Given a inpStr of length n, let its index be i.
#        Make a list buff of length 2n and index j.
#        Set first element of buff : buff[0] = inpStr[0]. Call the recursive function
#        printPatternUtil(inpStr, buff, i, j, n) with i = 1 and j = 2.
#        In recursive function if i == n: set buff[j] = '\0', print buff and return
#           Here we have two option either to place space or not, so take both the routes.
#           buff[j] = inpStr[i], printPatternUtil(inpStr, buff, i + 1, j + 1, n)
#           buff[j] = ' ', buff[j + 1] = inpStr[i], printPatternUtil(inpStr, buff, i + 1, j + 2, n)
# Complexity : Since number of Gaps are n-1, there are total 2^(n-1) patters each having length
#              ranging from n to 2n-1. Thus overall complexity would be O(n*(2^n)).


def toString(List):
    s = ""
    for x in List:
        if x == '\0':
            break
        s += x
    return s


def printPatternUtil(inpStr, buff, i, j, n):
    if i == n:
        buff[j] = '\0'
        print(toString(buff))
        return

    # Either put the character
    buff[j] = inpStr[i]
    printPatternUtil(inpStr, buff, i + 1, j + 1, n)

    # Or put a space followed by next character
    buff[j] = ' '
    buff[j + 1] = inpStr[i]
    printPatternUtil(inpStr, buff, i + 1, j + 2, n)


def printPattern(inpStr):
    n = len(inpStr)
    buff = [0] * (2 * n)
    buff[0] = inpStr[0]
    printPatternUtil(inpStr, buff, 1, 1, n)


if __name__ == "__main__":
    inpStr = "ABCD"
    printPattern(inpStr)
