# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# Question : There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array
# obtained after merging the above 2 arrays(i.e. array of length 2n).
#
#
# Used : Make a call to recursive function getMedian(arr1, arr2, n). If n <= 0: return -1
#            if n == 1: return arr1[0] + arr2[0] / 2
#            if n == 2: return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
#            find median of arr1 and arr2, m1 and m2
#            If m1 < m2 : median exist in arr1[mid...n-1] and arr2[0....mid]. Call the function again on it.
#            Else median exist in arr1[0...mid] and arr2[mid...n-1]. Call function on it.
#        While calling recursive function take care of n being odd or even.
#        If n = 10 send 5 values to recursive function, i.e from index 0 to 4 and 5 to 9
#        If n = 11 send 6 values to recursive function, i.e from index 0 to 5 and 5 to 10
# Complexity : O(log n)


def median(arr, n):
    if n % 2 == 0:
        # even
        return (arr[n/2] + arr[n/2-1])/2
    else:
        # odd
        return arr[n/2]


def getMedian(arr1, arr2, n):
    # print arr1, arr2
    if n <= 0:
        return -1

    if n == 1:
        return arr1[0] + arr2[0] / 2

    if n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    m1 = median(arr1, n)
    m2 = median(arr2, n)

    if m1 == m2:
        return m1

    # median exist in arr1[mid...n-1] and arr2[0....mid]
    # In python a[0:3] will give you value from 0 to 2
    if m1 < m2:
        if n % 2 == 0:
            return getMedian(arr1[n/2:], arr2[0:n/2], n / 2)
        return getMedian(arr1[n/2:], arr2[0:n/2 + 1], n / 2 + 1)
    else:    # median exist in arr1[0...mid] and arr2[mid...n-1]
        if n % 2 == 0:
            return getMedian(arr1[0:n/2], arr2[n/2:], n / 2)
        return getMedian(arr1[0:n/2+1], arr2[n/2:], n / 2 + 1)


if __name__ == "__main__":
    # arr1 = [1, 2, 3, 6]
    # arr2 = [4, 6, 8, 10]
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 3, 17, 30, 45]
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 == n2:
        print getMedian(arr1, arr2, n1)

