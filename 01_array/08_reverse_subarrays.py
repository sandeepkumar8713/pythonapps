# Question : Given an array, reverse every sub-array formed by consecutive k elements.
#
# Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#        k = 3
# Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]
#
# Used : for a given sub array, loop from left and right inward and swap
# complexity : O(n)


def reverse(arr, n, k):
    i = 0
    while i < n:
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right - +1
        i += k


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    n = len(arr)
    reverse(arr, n, k)
    print "Reversed Array:", arr
