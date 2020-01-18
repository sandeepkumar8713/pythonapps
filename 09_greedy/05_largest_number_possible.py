# Question : Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose
# sum of digits should be equals to 'S'.
#
# Used : First check if is possible to reach the target with given number of digits using this:
#        targetSum > 9 * digitCount
#        Make a result array of size digitCount and initialize all with 0
#        Loop over the element of array and check if target sum is greater or equal than 9. If it is, set 9 in array and
#           decrement targetSum by 9. Else put target sum in the array and set targetSum as 0.
#        return result array.
# Complexity : O(n)


def findLargest(m, s):
    if s is 0:
        if m is 1:
            return [0]
        else:
            print [-1]
        return

    if s > 9 * m:
        return [-1]

    res = [0] * m

    for i in range(0, m):
        if s >= 9:
            res[i] = 9
            s = s - 9
        else:
            res[i] = s
            s = 0

    return res


if __name__ == "__main__":
    # targetSum = 9
    # digitCount = 2

    targetSum = 20
    digitCount = 3
    res = findLargest(digitCount, targetSum)
    number = 0
    for ele in res:
        number = number * 10 + ele
    print "Largest number is:", number
