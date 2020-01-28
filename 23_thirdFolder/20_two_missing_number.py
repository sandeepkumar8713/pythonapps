# CTCI : Q17_19_Missing_Two
# https://brilliant.org/wiki/sum-of-n-n2-or-n3/
# https://www.cliffsnotes.com/study-guides/algebra/algebra-i/quadratic-equations/solving-quadratic-equations
# Question : You are given an array with all the numbers from 1 to N appearing exactly once,
# except for one number that is missing. How can you find the missing number in O(N) time and
# 0(1) space? What if there were two numbers missing?
#
# Question Type : ShouldSee
# Used : Remember that 1+2+3...n = n(n+1)/2 ans 1^2 + 2^2 + 3^2 ... n^2 = n(n+1)(2n+1)/6
#        Using this find s and t of the missing number.
#        Let x and y be missing number.
#        x + y = s -> y = S - X
#        x^2 + y^2 = t -> x^2 + (s-x)^2 = t
#                      -> 2x^2 - 2sx + (s^2 - t) = 0
#        Recall the quadratic formula:
#        x = [-b +- sqrt(b^2 - 4ac)] / 2a
#           where, in this case:
#               a = 2
#               b = -2*S
#               c = S^2 - t
# complexity : O(n)

import math


def solveEquation(s, t):
    a = 2
    b = -2 * s
    c = s * s - t

    part1 = -1 * b
    part2 = math.sqrt(b * b - 4 * a * c)
    part3 = 2 * a

    solutionX = (int)((part1 + part2) / part3)
    solutionY = s - solutionX

    solutionX2 = (int)((part1 - part2) / part3)
    solutionY2 = s - solutionX2

    # print ("Alternate Solution : %s,%s" % (solutionX2, solutionY2))
    return [solutionX, solutionY]


def findMissingTwo(array):
    maxValue = len(array) + 2
    totalProduct = (maxValue * (maxValue + 1) * (2 * maxValue + 1))/6
    totalSum = maxValue * (maxValue + 1) / 2

    for item in array:
        totalProduct -= item * item
        totalSum -= item

    return solveEquation(totalSum, totalProduct)


if __name__ == "__main__":
    x = 12
    y = 56
    array = []
    for i in range(1,101):
        if i != x and i != y:
            array.append(i)
    print(findMissingTwo(array))
