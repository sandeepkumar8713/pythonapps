# https://www.geeksforgeeks.org/check-if-a-given-number-is-fancy/
# Question : A fancy number is one which when rotated 180 degrees is the same. Given a number,
# find whether it is fancy or not. 180 degree rotations of 6, 9, 1, 0 and 8 are 9, 6, 1, 0 and 8 respectively
#
# Examples:
# Input:  num =  96
# Output: Yes
# If we rotate given number by 180, we get same number
#
# Question Type : Generic
# Used : Make a map of fancy number
#        Now loop over the input from left and right side
#        Check left element to in map and it should equal to fancy of right element
#        Else : return False
#        After the loop return True
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


if __name__ == "__main__":
    num = "9088806"
    print(isFancy(num))
