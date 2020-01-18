# Question : Given an array and a number k where k is smaller than size of array, we need to find the k'th smallest
# element in the given array. It is given that all array elements are distinct.
#
# Used : use the partition function of quicksort, since it gives back position of pivot in sorted array,
#        use it compare with k
#           if pos - left == k - 1: return arr[pos]
#           if pos - left > k - 1: return kthSmallest(arr, left, pos-1, k)
#           else: return kthSmallest(arr, pos+1, right, k - pos + left - 1)
#
#        Same logic can be used for kth largest element by passing n-k to the above function
# Complexity : O(n) , worst : O(n^2)
#              We can even use min heap, form a min heap in O(n) and extract k times : O(n + k log n)


def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(1, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def kthSmallest(arr, left, right, k):
    # k is positive and within left and right
    if 0 < k <= right - left + 1:
        pos = partition(arr, left, right)

        # check if pivot is the position we were looking at
        if pos - left == k - 1:
            return arr[pos]
        if pos - left > k - 1:
            # then go to left half of array
            return kthSmallest(arr, left, pos-1, k)
        else:
            return kthSmallest(arr, pos+1, right, k - pos + left - 1)

    return None


if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    print sorted(arr)
    n = len(arr)
    k = 3
    print kthSmallest(arr, 0, n-1, k)
    # kth largest
    print kthSmallest(arr, 0, n - 1, n - k)
