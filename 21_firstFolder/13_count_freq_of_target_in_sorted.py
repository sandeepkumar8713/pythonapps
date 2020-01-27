# https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
# Question : Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[].
#
# Question Type : Generic
# Used : Use Binary search to get index of the first occurrence of x in arr. Let the index of the first occurrence be i.
#        Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
#        return j - i + 1
# Complexity : O(log n)


def freqCount(arr, x, n):
    i = first(arr, 0, n - 1, x, n)
    if i == -1:
        return i
    j = last(arr, i, n - 1, x, n)
    return j - i + 1


def first(arr, low, high, x, n):
    if high >= low:
        mid = (low + high) // 2

    if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
    elif x > arr[mid]:
        return first(arr, (mid + 1), high, x, n)
    else:
        return first(arr, low, (mid - 1), x, n)
    return -1


def last(arr, low, high, x, n):
    if high >= low:
        mid = (low + high) // 2

    if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return last(arr, low, (mid - 1), x, n)
    else:
        return last(arr, (mid + 1), high, x, n)
    return -1


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 3]
    x = 3
    n = len(arr)
    c = freqCount(arr, x, n)
    print("frequency :", c)
