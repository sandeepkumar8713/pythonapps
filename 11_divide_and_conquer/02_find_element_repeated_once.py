# Question : Given a sorted array in which all elements appear twice (one after one) and one element appears only once.
# Find that element in O(log n) complexity.
#
# Used : Do a binary search over the elements.
#       Find the middle index, say 'mid'.
#        If 'mid' is even, then compare arr[mid] and arr[mid + 1]. If both are same, then the required element after
#           'mid' else before mid.
#        If 'mid' is odd, then compare arr[mid] and arr[mid - 1]. If both are same, then the required element after
#           'mid' else before mid.
#        If low > high : return None
#        If low == high : return arr[low]
# Complexity : O(log n)


def binarySearch(arr, low, high):
    if low > high:
        return None

    # found
    if low == high:
        return arr[low]

    mid = (low + high) / 2
    if mid % 2 == 0:
        if arr[mid] == arr[mid + 1]:
            return binarySearch(arr, mid + 2, high)
        else:
            return binarySearch(arr, low, mid)

    else:
        if arr[mid] == arr[mid - 1]:
            return binarySearch(arr, mid + 1, high)
        else:
            return binarySearch(arr, low, mid - 1)


if __name__ == "__main__":
    arr = [1, 1, 2, 4, 4, 5, 5, 6, 6]
    result = binarySearch(arr, 0, len(arr) -1)
    if result is not None:
        print ("The required element is : " + str(result))
    else:
        print ("Invalid Array")
