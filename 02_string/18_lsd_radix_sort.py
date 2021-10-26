# https://en.wikipedia.org/wiki/Radix_sort
# Question : LSD (Least Significant Digit) radix sorts typically use the following sorting order:
# short keys come before longer keys, and then keys of the same length are sorted lexicographically.
# This coincides with the normal order of integer representations, such as the sequence
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#
# Question Type : Generic
# Used : Find the max value in the input array.
#        Run a loop while (10 ** index <= maxval). Call function
#        distributeBasedOnDigit(array, base, index):
#        Make a list of buckets of size base.
#        Loop over input array and distribute them in buckets.
#        digit = (ele // (base ** index)) % base
#        buckets[digit].append(ele)
#        Merge these buckets into the input array.
# Complexity : O(w * n)


def distributeBasedOnDigit(arr, base, index):
    buckets = []
    for i in range(base):
        buckets.append([])

    for ele in arr:
        # Isolate the base-digit from the number
        digit = (ele // (base ** index)) % base
        # Drop the number into the correct bucket
        buckets[digit].append(ele)

    i = 0
    for bucket in buckets:
        for ele in bucket:
            arr[i] = ele
            i += 1


def radixSort(array):
    maxval = max(array)
    base = 10

    index = 0
    # Iterate, sorting the array by each base-digit
    while base ** index <= maxval:
        distributeBasedOnDigit(array, base, index)
        index += 1


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)
    print(arr)
