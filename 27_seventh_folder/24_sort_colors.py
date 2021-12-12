# https://leetcode.com/problems/sort-colors/
# Question : Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in the order
# red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red,
# white, and blue, respectively. You must solve this problem without using the library's
# sort function.
#
# Question Type : Generic
# Used : Make 3 index low,mid and high.
#        Loop over the input array. If mid is 0, swap to low.
#        If mid is 1, inc mid
#        If mid is 2, swap to high
#        Logic :
#        low = 0, mid = 0, high = len(inpArr) - 1
#        while mid < high:
#           ele = inpArr[mid]
#           if ele == 0:
#               inpArr[mid], inpArr[low] = inpArr[low], inpArr[mid]
#               low += 1, mid += 1
#           elif ele == 1:
#               mid += 1
#           elif ele == 2:
#               inpArr[high], inpArr[mid] = inpArr[mid], inpArr[high]
#               high -= 1
#        return inpArr
# Complexity : O(n)


def sortColors(inpArr):
    low = 0
    mid = 0
    high = len(inpArr) - 1

    while mid < high:
        ele = inpArr[mid]

        if ele == 0:
            inpArr[mid], inpArr[low] = inpArr[low], inpArr[mid]
            low += 1
            mid += 1
        elif ele == 1:
            mid += 1
        elif ele == 2:
            inpArr[high], inpArr[mid] = inpArr[mid], inpArr[high]
            high -= 1

    return inpArr


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums))
