# https://leetcode.com/problems/sliding-window-median/
# Question : You are given an integer array nums and an integer k. There is a sliding window of size k
# which is moving from the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Return the median array for
# each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
# Example : Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
#
# Question Type : Generic
# Used : Make a sorted list from first k - 1 elements.
#        Loop over the remaining elements.
#        Do binary search for new ele in sortedList and insert.
#        Calculate median.
#        Do binary search for old ele in sortedList and delete.
# Logic: sortedList = nums[:k - 1], sortedList.sort()
#        for i in range(k - 1, len(nums)):
#           sortedList = insert(sortedList, nums[i])
#           medianList.append((sortedList[(k - 1) // 2] + sortedList[k // 2]) / 2)
#           sortedList = remove(sortedList, nums[i - k + 1])
#        return medianList
#
#        def insert(inpArr, key):
#        i = binarySearch(inpArr, key)
#        newArray = inpArr[:i] + [key] + inpArr[i:]
#        inpArr.clear()
#        return newArray
# Complexity : O(n log k) n is no of ele in array and k is window size


def binarySearch(inpArr, key):
    low = 0
    high = len(inpArr) - 1
    while low <= high:
        mid = (low + high) // 2
        if inpArr[mid] == key:
            return mid
        elif inpArr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return low


def insert(inpArr, key):
    i = binarySearch(inpArr, key)
    newArray = inpArr[:i] + [key] + inpArr[i:]
    inpArr.clear()
    return newArray


def remove(inpArr, key):
    i = binarySearch(inpArr, key)
    newArray = inpArr[:i] + inpArr[i + 1:]
    inpArr.clear()
    return newArray


def medianSlidingWindow(nums, k):
    sortedList = nums[:k - 1]
    sortedList.sort()
    medianList = []

    for i in range(k - 1, len(nums)):
        sortedList = insert(sortedList, nums[i])
        medianList.append((sortedList[(k - 1) // 2] + sortedList[k // 2]) / 2)
        sortedList = remove(sortedList, nums[i - k + 1])

    return medianList


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(medianSlidingWindow(nums, k))

    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    print(medianSlidingWindow(nums, k))
