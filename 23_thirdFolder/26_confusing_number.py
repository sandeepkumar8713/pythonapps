# https://atprogrammer.com/2019/06/20/1088-Confusing-Number-II/
# https://github.com/openset/leetcode/tree/master/problems/confusing-number-ii
# Question : Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees,
# they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit
# valid.(Note that the rotated number can be greater than the original number.)
# Find count of numbers which consist of only fancy numbers. But when they are rotated, they are not the same.
#
# Example : Input: 20
# Output: 6
# Explanation: The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
#
# Question Type : Generic
# Used : Make numbers of fancy digits and check that they should not be fancy numbers.
#        call as : getCountUtils(0, limit, [0])
#        Logic : def getCountUtils(n, limit, count):
#        if n > limit: return
#        if not isFancy(str(n)): count[0] += 1
#        if n != 0: getCountUtils(n * 10, limit, count)
#        getCountUtils(n * 10 + 1, limit, count)
#        getCountUtils(n * 10 + 6, limit, count)
#        getCountUtils(n * 10 + 8, limit, count)
#        getCountUtils(n * 10 + 9, limit, count)
# Complexity : O(n)


fancyMap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


def isFancy(inpArr):
    leftIndex = 0
    rightIndex = len(inpArr) - 1

    while leftIndex <= rightIndex:
        leftElement = inpArr[leftIndex]
        rightElement = inpArr[rightIndex]

        if leftElement not in fancyMap or leftElement != fancyMap[rightElement]:
            return False

        leftIndex += 1
        rightIndex -= 1

    return True


def getCountUtils(n, limit, count):
    if n > limit:
        return

    if not isFancy(str(n)):
        count[0] += 1

    if n != 0:
        getCountUtils(n * 10, limit, count)

    getCountUtils(n * 10 + 1, limit, count)
    getCountUtils(n * 10 + 6, limit, count)
    getCountUtils(n * 10 + 8, limit, count)
    getCountUtils(n * 10 + 9, limit, count)


def getNotFancyCount(limit):
    count = [0]
    getCountUtils(0, limit, count)
    return count[0]


if __name__ == "__main__":
    n = 20
    print(getNotFancyCount(20))
