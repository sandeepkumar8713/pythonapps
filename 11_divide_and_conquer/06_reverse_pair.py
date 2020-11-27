# https://leetcode.com/articles/reverse-pairs/
# Question : Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# You need to return the number of important reverse pairs in the given array.
#
# Example:
# Input: [1,3,2,3,1]
# Output: 2
#
# Question Type : ShouldSee
# Used : We modify the merge sort and before merging, we check the condition on left and right sub array and keep
#        track of count.
#        mergeSortAndCount(inpArr, start, end):
#        if start >= end: return 0
#        mid = (start + end) / 2
#        count = mergeSortAndCount(inpArr, start, mid) + mergeSortAndCount(inpArr, mid + 1, end)
#        j = mid + 1
#        for i in range(start, mid+1):
#           while j <= end and inpArr[i] > inpArr[j] * 2:
#               j += 1
#           count += j - (mid + 1)
#        merge(inpArr, start, mid, end)
#        return count
# Complexity : O(n log n)


def merge(arr, left, mid, right):
    leftRow = []
    for i in range(left, mid+1):
        leftRow.append(arr[i])

    rightRow = []
    for i in range(mid+1, right+1):
        rightRow.append(arr[i])

    i = 0
    j = 0
    while i < len(leftRow) and j < len(rightRow):
        if leftRow[i] <= rightRow[j]:
            arr[left] = leftRow[i]
            i += 1
        else:
            arr[left] = rightRow[j]
            j += 1
        left += 1

    while i < len(leftRow) and left <= right:
        arr[left] = leftRow[i]
        left += 1
        i += 1

    while j < len(rightRow) and left <= right:
        arr[left] = rightRow[j]
        left += 1
        j += 1


def mergeSortAndCount(inpArr, start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2
    count = mergeSortAndCount(inpArr, start, mid) + mergeSortAndCount(inpArr, mid + 1, end)
    j = mid + 1
    for i in range(start, mid+1):
        while j <= end and inpArr[i] > inpArr[j] * 2:
            j += 1
        count += j - (mid + 1)
    merge(inpArr, start, mid, end)
    return count


if __name__ == "__main__":
    inpArr = [2, 4, 3, 5, 1]
    print(mergeSortAndCount(inpArr, 0, len(inpArr) - 1))
