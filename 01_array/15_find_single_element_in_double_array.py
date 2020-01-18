# Question : Given a sorted array in which all elements appear twice (one after one) and one element appears only once.
#
# Used : Do binary search
#        if low == high:
#           return arr[low]  (answer)
#        if mid is even check mid == mid + 1 if true target is in b/w mid + 2 and right else in left and mid
#        if mid is odd check mid == mid -1 if true target is in b/w mid + 1 and right else in left and mid - 1
# Complexity : O(log n)


def search(arr, low, high):
    if low > high:
        return None

    if low == high:
        return arr[low]

    mid = low + (high - low) / 2
    if mid % 2 == 0:
        # if mid is even
        if arr[mid] == arr[mid + 1]:
            return search(arr, mid + 2, high)
        else:
            return search(arr, low, mid)

    else:
        # if mid is odd
        if arr[mid] == arr[mid - 1]:
            return search(arr, mid + 1, high)
        else:
            return search(arr, low, mid - 1)


if __name__ == "__main__":
    arr = [1, 1, 2, 4, 4, 5, 5, 6, 6]
    print search(arr, 0, len(arr) - 1)
