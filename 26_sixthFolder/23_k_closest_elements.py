# https://leetcode.com/problems/find-k-closest-elements/
# Question : Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
# Example : Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
#
# Question Type : Generic
# Used : As the array is sorted, we need to find to binary search to find the starting index of
#        closest array. There are four cases:
#        when x - p <= q - x
#        1. **x**[p******]q*** 2. *****[p*x****]q***
#        when x - p > q - x:
#        3. *****[p****x*]q*** 4. *****[p******]q*x*
#        For case 1 and 2, we set right as mid
#        For case 3 and 4, we set left as mid + 1
#        Logic :
#        left = 0, right = len(arr) - k
#        while left < right - 1:
#           mid = left + (right - left) / 2
#           if x - arr[mid] <= arr[mid + k] - x:
#               right = mid
#           else:
#               left = mid + 1
#        if left + k >= len(arr) or abs(arr[left] - x) <= abs(arr[left + k] - x):
#           index = left
#        else:
#           index = right
#        return arr[index:index + k]
# Complexity : O(log(n-k) + k)


def knn(arr, x, k):
    left = 0
    right = len(arr) - k

    while left < right - 1:
        mid = left + (right - left) / 2
        if x - arr[mid] <= arr[mid + k] - x:
            right = mid
        else:
            left = mid + 1

    if left + k >= len(arr) or abs(arr[left] - x) <= abs(arr[left + k] - x):
        index = left
    else:
        index = right

    return arr[index:index + k]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(knn(arr, x, k))

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    print(knn(arr, x, k))
