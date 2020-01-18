# http://buttercola.blogspot.com/2016/06/leetcode-335-self-crossing.html
# Question : You are given an array x of n positive numbers. You start at point (0,0) and moves x[0]
# metres to the north, then x[1] metres to the west, x[2] metres to the south,x[3] metres to the east
# and so on. In other words, after each move your direction changes counter-clockwise.
# Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
#
# Example :
# Given x = [2, 1, 1, 2],
#  __
# |__|_
#    |
#
# Return true (self crossing)
#
# Used : The problem is tricky to solve. There are in total three cases to consider if there is no cross
#        1. Only have internal squirrels. In this case, the length of each step should go smaller and smaller.
#           So we only need to check if x[i] < x[i - 2].
#        2. Only have external squirrels. In this case, the length of each step should go larger and larger. So we only
#          need to check if x[i] > x[i - 2].
#        3. In the third case, it goes external squirrel first then go internal. In this case, the trick part is we
#          may need to update the base of the internal squirrel.
#        Logic : def isSelfCrossing(inpArr):
#        if inpArr is None or len(inpArr) <= 3: return False
#        i = 2, n = len(inpArr)
#        while i < n and inpArr[i] > inpArr[i-2]: i += 1
#        if i == n: return False
#        if (i >= 4 and inpArr[i] + inpArr[i - 4] >= inpArr[i - 2]) or (i == 3 and inpArr[i] == inpArr[i - 2]):
#           inpArr[i - 1] -= inpArr[i - 3]
#        i += 1
#        while i < n and inpArr[i] < inpArr[i - 2]:
#           i += 1
#        return i != n
# Complexity : O(n)


def isSelfCrossing(inpArr):
    if inpArr is None or len(inpArr) <= 3:
        return False

    i = 2
    n = len(inpArr)

    # case 1: outside squrial
    while i < n and inpArr[i] > inpArr[i-2]:
        i += 1

    if i == n:
        return False

    # case 2: transist to inside squrial
    if (i >= 4 and inpArr[i] + inpArr[i - 4] >= inpArr[i - 2]) or (i == 3 and inpArr[i] == inpArr[i - 2]):
        inpArr[i - 1] -= inpArr[i - 3]

    i += 1

    #  case 3: inside squrial
    while i < n and inpArr[i] < inpArr[i - 2]:
        i += 1

    return i != n


if __name__ == "__main__":
    inpArr = [2, 1, 1, 2]
    # inpArr = [2, 1, 5, 2]
    print isSelfCrossing(inpArr)
