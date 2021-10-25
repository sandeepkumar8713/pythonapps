# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# Question : Given an array and an integer k, find the maximum for each and every
# contiguous sub array of size k. Find maximum in every sliding window of size k
# in the given array.
#
# Input : arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
#         k = 3
# Output : 3 3 4 5 5 5 6
#
# Question Type : ShouldSee
# Used : Deque, push larger element at rear after removing all smaller elements,
#        pop the first element as result.
#        Loop for i : 0 to k-1, keep popping smaller(than a[i]) element from last,
#        after that appending(indexof a[i]) in Qi.
#        loop for i : k to n-1, print arr[Qi[0]]. keep pop element from start while Qi[0] <= i - k.
#            keep popping smaller(than a[i]) element from last, after that append(indexof a[i]) in Qi.
#        print arr[Qi[0]]
# Complexity : O(n)


def printMax(arr, n, k):
    Qi = []

    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop(len(Qi) - 1)
        Qi.append(i)

    for i in range(k, n):
        print(str(arr[Qi[0]]))
        while Qi and Qi[0] <= i - k:
            Qi.pop(0)

        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop(len(Qi) - 1)
        Qi.append(i)

    print(str(arr[Qi[0]]))


if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    print("max values:")
    printMax(arr, len(arr), k)
