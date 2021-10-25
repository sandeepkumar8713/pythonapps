# https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/
# Question : Given an array of positive integers. We need to make the given array a 'Palindrome'.
# Only allowed operation on array is merge. Merging two adjacent elements means replacing them
# with their sum. The task is to find minimum number of merge operations required to make given
# array a 'Palindrome'.
#
# Input : arr[] = {1, 4, 5, 1}
# Output : 1
# We can make given array palindrome with minimum one merging (merging 4 and 5 to make 9)
#
# Question Type : ShouldSee
# Used : Set mergeCount = 0. Take 2 pointers left = 0 and right = n - 1.
#        Logic :
#        findMinOps(arr, n):
#        Loop while left < right:
#           if arr[left] == arr[right] : increment left and decrement right by 1
#           if left is bigger than right:
#               decrement right by 1
#               do merge arr[right] += arr[right + 1], mergeCount++
#           else :
#               increment left by 1
#               do merge arr[left] += arr[left - 1], and mergeCount++
#        return mergeCount
# Complexity : O(n)


def findMinOps(arr, n):
    mergeCount = 0
    left = 0
    right = n - 1
    while left <= right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1

        elif arr[left] > arr[right]:
            right -= 1   # need to merge from tail.
            arr[right] += arr[right + 1]
            mergeCount += 1
        else:
            left += 1   # Else we merge left two elements
            arr[left] += arr[left - 1]
            mergeCount += 1

    return mergeCount


if __name__ == "__main__":
    arr = [1, 4, 5, 9, 1]
    n = len(arr)
    print("Min merge operation: ", findMinOps(arr, n))
