# CTCI : Q16_16_Sub_Sort
# https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
# Question : Given an array of integers, write a method to find indices m and n such that if you sorted
# elements m through n , the entire array would be sorted. Minimize n - m (that is, find the smallest
# such sequence).
#
# Question Type : Generic
# Used : 1) Find the candidate unsorted subarray
#        a) Scan from left to right and find the first element which is greater than the next
#           element. Let s be the index of such an element. In the above example 1, s is 3
#           (index of 30).
#        b) Scan from right to left and find the first element (first in right to left order)
#           which is smaller than the next element (next in right to left order). Let e be
#           the index of such an element. In the above example 1, e is 7 (index of 31).
#
#        2) Check whether sorting the candidate unsorted subarray makes the complete array
#           sorted or not. If not, then include more elements in the subarray.
#        a) Find the minimum and maximum values in arr[s..e]. Let minimum and maximum
#           values be min and max. min and max for [30, 25, 40, 32, 31] are 25 and 40
#           respectively.
#        b) Find the first element (if there is any) in arr[0..s-1] which is greater than min,
#           change s to index of this element. There is no such element in above example 1.
#        c) Find the last element (if there is any) in arr[e+1..n-1] which is smaller than max,
#           change e to index of this element. In the above example 1, e is changed to 8
#           (index of 35).
# Complexity : O(n)


def printUnsorted(arr, n):
    e = n - 1
    # step 1(a) of above algo
    for s in range(0, n - 1):
        if arr[s] > arr[s + 1]:
            break

    if s == n - 1:
        print ("The complete array is sorted")
        exit()

    # step 1(b) of above algo
    e = n - 1
    while e > 0:
        if arr[e] < arr[e - 1]:
            break
        e -= 1

    # step 2(a) of above algo
    max = arr[s]
    min = arr[s]
    for i in range(s + 1, e + 1):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

        # step 2(b) of above algo
    for i in range(s):
        if arr[i] > min:
            s = i
            break

    # step 2(c) of above algo
    i = n - 1
    while i >= e + 1:
        if arr[i] < max:
            e = i
            break
        i -= 1

    # step 3 of above algo
    print("The unsorted subarray which makes the given array")
    print("sorted lies between the indexes %d and %d" % (s, e))


if __name__ == "__main__":
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    arr_size = len(arr)
    printUnsorted(arr, arr_size)
