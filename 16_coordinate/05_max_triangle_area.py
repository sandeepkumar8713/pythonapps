# https://leetcode.com/problems/largest-triangle-area/
# Question : Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area
# of the largest triangle that can be formed by any three different points. Answers within 10-5 of the
# actual answer will be accepted.
#
# Example : Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
#
# Question Type : ShouldSee
# Used : Run 3 loops, to check all the possible combination for a triangle
#        Calculate its area and compare with max area.
#        Logic:
#        for i in range(n - 2):
#           x1, y1 = points[i]
#           for j in range(i + 1, n - 1):
#               x2, y2 = points[j]
#               for k in range(j + 1, n):
#                   x3, y3 = points[k]
#                   area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
#                   if area > maxArea: maxArea = area
#        return maxArea
# Complexity : O(n^3) where n is number of points


def largestTriangleArea(points):
    maxArea = 0
    n = len(points)
    for i in range(n - 2):
        x1, y1 = points[i]
        for j in range(i + 1, n - 1):
            x2, y2 = points[j]
            for k in range(j + 1, n):
                x3, y3 = points[k]
                area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                if area > area:
                    maxArea = area

    return maxArea


if __name__ == "__main__":
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(largestTriangleArea(points))
