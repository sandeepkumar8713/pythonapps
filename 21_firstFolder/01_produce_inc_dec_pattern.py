# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/ see 3rd one
# Question : Given a pattern containing only N's and M's. I for increasing and D for decreasing. Devise an
# algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can't repeat.
# Inc = N, Dec = M
# -1 for not possible
#
# Question Type : ShouldSee
# Used : Use stack, in case of inc pop else push. At end of loop pop everything
#        Logic :
#        for i in range(0, len(pattern)+1):
#           if i < len(pattern) and not(pattern[i] == 'M' or pattern[i] == 'N'):
#               return '-1'
#           stk.append(i+1)
#           if i == len(pattern) or pattern[i] == 'N':
#               while len(stk) != 0:
#                   resStr += str(stk.pop())
#        if len(resStr) == 0:
#           return '-1'
#        return resStr
# Complexity : O(n)


def findPossibleSmallestNumberMatchingPattern(pattern):
    resStr = ''
    stk = list()

    for i in range(0, len(pattern)+1):
        if i < len(pattern) and not(pattern[i] == 'M' or pattern[i] == 'N'):
            return '-1'
        stk.append(i+1)

        if i == len(pattern) or pattern[i] == 'N':
            while len(stk) != 0:
                resStr += str(stk.pop())

    if len(resStr) == 0:
        return '-1'
    return resStr


if __name__ == "__main__":
    print(findPossibleSmallestNumberMatchingPattern("N"))
    print(findPossibleSmallestNumberMatchingPattern("MNM"))
    print(findPossibleSmallestNumberMatchingPattern("MOM"))
    print(findPossibleSmallestNumberMatchingPattern("M"))
