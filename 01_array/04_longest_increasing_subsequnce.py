# Question : The Longest Increasing sub sequence (LIS) problem is to find the length of the longest sub sequence of a
# given sequence such that all elements of the sub sequence are sorted in increasing order. For example, the length
# of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
#
# Used : Make a array called tail filled with zeros. Note that we are dealing with end elements only. We need not to
#        maintain all the lists. We can store the end elements in an array.
#        Now through the given array.  Also, ensure we have maintained the condition, "end element of smaller list is
#        smaller than end elements of larger lists"
#        If arr[i] is smaller than tail[0], replace it with arr[i] and form a new LIS
#        If arr[i] is larger than tail[length-1], then extend the tail by appending with arr[i]
#        Else arr[i] would be somewhere in between the tail elements. Do binary search for it.
#        Place it at its correct position, while discarding the right remaining elements of the tail.
# Complexity : 0(n log n)


def ceilIndex(arr, left, right, key):
    while right-left > 1:
        mid = left + (right-left)/2
        # binary search, return when diff is 1
        if key <= arr[mid]:
            right = mid
        else:
            left = mid

    return right


def LIS(arr):
    if len(arr) is 0:
        return 0

    tail = [0] * len(arr)
    # always points empty slot in tail
    length = 1

    tail[0] = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < tail[0]:
            # new smallest value
            tail[0] = arr[i]
        elif arr[i] > tail[length-1]:
            # arr[i] extends largest sub sequence
            tail[length] = arr[i]
            length += 1
        else:
            # arr[i] will become end candidate of an existing subsequence or
            # Throw away larger elements in all LIS, to make room for upcoming grater elements than arr[i]
            # and also, arr[i] would have already appeared in one of LIS, identify the location and replace it
            tail[ceilIndex(arr, -1, length-1, arr[i])] = arr[i]

    print tail[:length]
    return length


if __name__ == "__main__":
    arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]
    print LIS(arr)
