# Question : You are given a list of n-1 integers and these integers are in the range of
# 1 to n. There are no duplicates in list. One of the integers is missing in the list.
# Write an efficient code to find the missing integer.
#
# Question Type : Generic
# Used : Use the Arithmetic Progression to find sum and subtract from given values to get missing number
#        Formula : Sn = n/2(2a + (n-1)d)
# Complexity : O(n)


def getMissingNo(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sumOfA = sum(A)
    return total - sumOfA


if __name__ == "__main__":
    A = [1, 2, 4, 5, 6]
    missedNumber = getMissingNo(A)
    print(missedNumber)
