# https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
# Question : A sorted array is rotated at some unknown point, find the minimum element in it
#
# Used : We need to call a recursive function: findMin(arr, low, high)
#           if low == high return arr[low]
#           mid = (low + high) / 2
#           if arr[mid + 1] is smaller than arr[mid], return arr[mid + 1]
#           if arr[mid] is smaller than arr[mid-1], return arr[mid]
#           if arr[high] > arr[mid]:
#                return findMin(arr, low, mid - 1)
#           else:return findMin(arr, mid + 1, high)
# Complexity : O(log n)


def findMin(arr, low, high):
    # This condition is needed to handle the case when array is not rotated at all
    if high < low:
        return arr[0]
    # If there is only one element left
    if high == low:
        return arr[low]
    # Find mid
    mid = int((low + high) / 2)

    # if mid + 1 is smaller than mid, return mid + 1
    if mid < high and arr[mid + 1] < arr[mid]:
        return arr[mid + 1]

    # if mid is smaller than mid-1, return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    if arr[high] > arr[mid]:
        return findMin(arr, low, mid - 1)
    return findMin(arr, mid + 1, high)


if __name__ == "__main__":
    inpArr = [5, 6, 1, 2, 3, 4]
    n = len(inpArr)
    print("The minimum element is " + str(findMin(inpArr, 0, n - 1)))
