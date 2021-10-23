# https://leetcode.com/problems/max-value-of-equation/
# Question : You are given an array points containing the coordinates of points on a 2D plane,
# sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <=
# points.length. You are also given an integer k. Return the maximum value of the equation
# yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed
# that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
#
# Example : Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
#
# Question Type : ShouldSee
# Used : Since the given array is always sorted, based value of x. we know that (xi - xj) will always -ve.
#        So we modify equation yi + yj + |xi - xj| to yi + yj - xi + xj.
#        Now make a max heap, with value tuple (y_i-x_i, x_i)
#        Loop over the given array. Keep popping ele from heap, which doesn't satisfy the less k condition.
#        Now pop the top element from maxheap, try to pair and update max res.
#        Push the current ele in max heap.
#        Logic :
#        heap = [(-(points[0][1] - points[0][0]), points[0][0])]
#        res = float('-inf')
#           for i in range(1, n):
#           xj, yj = points[i]
#           while heap and xj - heap[0][1] > k:
#               heapq.heappop(heap)
#           if heap:
#               diff_h, x_h = -heap[0][0], heap[0][1]
#               res = max(res, xj + yj + diff_h)
#           heapq.heappush(heap, (-(points[i][1] - points[i][0]), xj))
#        return res
# Complexity : O(n log n)

import heapq


def findMaxValueOfEquation(points, k):
    n = len(points)

    # edge case
    if n == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        return y1 + y0 + x1 - x0

    heap = [(-(points[0][1] - points[0][0]), points[0][0])]  # max-heap stores (y_i-x_i, x_i)
    res = float('-inf')
    for i in range(1, n):
        xj, yj = points[i]

        # find max(y_i - x_i) for i < j and |x_i - x_j| <= k
        while heap and xj - heap[0][1] > k:
            heapq.heappop(heap)
        if heap:
            diff_h, x_h = -heap[0][0], heap[0][1]
            # xj + yj + yi - xi
            res = max(res, xj + yj + diff_h)

        # add (y_j - x_j, x_j) into heap for later use
        heapq.heappush(heap, (-(points[i][1] - points[i][0]), xj))

    return res


if __name__ == "__main__":
    points = [[1, 3], [2, 0], [5, 10], [6, -10]]
    k = 1
    print(findMaxValueOfEquation(points, k))

    points = [[0, 0], [3, 0], [9, 2]]
    k = 3
    print(findMaxValueOfEquation(points, k))
