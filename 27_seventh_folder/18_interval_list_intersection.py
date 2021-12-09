# https://leetcode.com/problems/interval-list-intersections/
# Question : You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals
# is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty
# or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
#
# Question Type : Generic
# Used : Run loop over the given 2 arrays.
#        While doing so for each index, find max of start and min of end b/w 2 array
#           and append the range in ans array.
#           Increment index of array whose ele is less.
#        After the loop return ans array.
#        Logic :
#        while i < n and j < m:
#           low = max(a[i][0], b[j][0])
#           high = min(a[i][1], b[j][1])
#           if low <= high:
#               ans.append([low, high])
#           if a[i][1] < b[j][1]:
#               i += 1
#           else:
#               j += 1
#        return ans
# Complexity : O(n)

def intervalIntersection(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    ans = []

    while i < n and j < m:
        low = max(a[i][0], b[j][0])
        high = min(a[i][1], b[j][1])

        if low <= high:
            ans.append([low, high])

        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return ans


if __name__ == "__main__":
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(firstList, secondList))

    firstList = [[1, 3], [5, 9]]
    secondList = []
    print(intervalIntersection(firstList, secondList))

    firstList = [[1, 7]]
    secondList = [[3, 10]]
    print(intervalIntersection(firstList, secondList))
