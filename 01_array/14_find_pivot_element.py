# Similar : 21_firstFolder/31_binary_searchable.py
# Question : Given an array, find an element before which all elements are smaller than it,
# and after which all are greater than it. Return index of the element if there is such
# an element, otherwise return -1.
#
# Question Type : Generic, SimilarAdded
# Used : Max of left elements should be less than pivot and min of right elements should
#        be greater than pivot.
#        So make a leftMax array, loop from right side on array while keeping the right
#        minimum and check the above line.
#        Logic :
#        for i in range(n-1, -1, -1):
#           if leftMax[i] < arr[i] < rightMin:
#               return i
#           rightMin = min(rightMin, arr[i])
# Complexity : O(n)


def findPivot(arr):
    n = len(arr)
    leftMax = [0] * n
    leftMax[0] = -999999

    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])

    rightMin = 999999

    for i in range(n-1, -1, -1):
        if leftMax[i] < arr[i] < rightMin:
            return i
        rightMin = min(rightMin, arr[i])

    return -1


if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    print('index of pivot:', findPivot(arr))
