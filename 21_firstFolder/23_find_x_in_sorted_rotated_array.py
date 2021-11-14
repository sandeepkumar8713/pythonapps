# CTCI : Q10_03_Search_in_Rotated_Array
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
# https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/
# Question : An element in a sorted array can be found in O(log n) time via binary search.
# But suppose we rotate an ascending order sorted array at some pivot unknown to you
# beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an
# element in the rotated array in O(log n) time.
#
# Question Type : Generic
# Used : Check if key is in mid;
#        if not check if left half is sorted if yes recur in left half,
#        if not found in left half recur in right half
#        If right half is sorted recur in right half,
#        if not found in right half recur in left half
# Complexity : O(log n)


def search(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly check if key lies in half or other half
        if arr[l] <= key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)

    # If arr[l..mid] is not sorted, then arr[mid... r] must be sorted
    if arr[mid] <= key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    key = 3

    # arr = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
    # key = 500

    i = search(arr, 0, len(arr) - 1, key)
    if i != -1:
        print("Index: " + str(i))
    else:
        print("Key not found")
