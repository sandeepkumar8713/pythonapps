# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
# Question : Arrange given numbers to form the biggest number.
# If the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
#
# Question Type : ShouldSee
# Used : In the used sorting algorithm, instead of using the default comparison, write a
#        comparison function myCompare() and use it to sort numbers. Given two numbers X and Y,
#        how should myCompare() decide which number to put first we compare two numbers
#        XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is
#        larger, then X should come before Y in output, else Y should come before.
#        comparator(a, b):
#        ab = str(a) + str(b)
#        ba = str(b) + str(a)
#        return cmp(int(ba), int(ab))
# Complexity : O(n^2)

import functools


def cmp(a, b):
    return (a > b) - (a < b)


def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return cmp(int(ba), int(ab))


if __name__ == "__main__":
    arr = [54, 546, 548, 60]
    sortedArray = sorted(arr, key=functools.cmp_to_key(comparator))
    print(sortedArray)
    number = ''
    for i in range(len(sortedArray)):
        number += str(sortedArray[i])
    print("Largest number :", number)
