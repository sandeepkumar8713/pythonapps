# https://leetcode.com/discuss/interview-question/3936802/MICROSOFT-OA
# Question : There is a line chart consisting of N points (numbered from 0 to N-1) connected by line segments.
# The K-th point has coordinates x=K,y=Y[K]. There are no horizontal lines; that is, no two consecutive points
# has the same y-coordinate. We can draw an infinitely long horizontal line. What is the maximum number of
# points of intersection of the line with the chart?
# Write a function: int solution(int Y[], int N);
# that, given array Y, returns the maximum number of common points between the horizontal line and our
# line chart if we draw the line optimally.
#
# 1. Given Y = [1, 2, 1, 2, 1, 3, 2], the function should return 5. A horizontal line at y 1.5 intersects the
# chart at points (0.5, 1.5), (1.5, 1.5), (2.5, 1.5), (3.5, 1.5) and (4.25, 1.5).
#
# TODO : add used

import sys


def line_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    # return (round(x,1), round(y,1))
    return (x, y)


def count_all_intersections(points, line_2):
    n = len(points)
    result = set()
    for i in range(n - 1):
        a = points[i]
        b = points[i + 1]
        line_1 = (a, b)
        intersection = line_intersection(line_1, line_2)
        if intersection is not None:
            result.add(intersection)

    return result


def solve(Y):
    points = []
    max_y = -sys.maxsize
    min_y = sys.maxsize
    min_x = 0
    max_x = len(Y) - 1

    for x, y in enumerate(Y):
        points.append((x, y))
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    max_count = 0
    y = min_y
    while y <= max_y:
        line_2 = ((min_x, y), (max_x, y))
        result = count_all_intersections(points, line_2)
        if len(result) > max_count:
            max_count = len(result)

        y = round(y + 0.1, 1)

    return max_count


if __name__ == "__main__":
    Y = [1, 2, 1, 2, 1, 3, 2]
    print(solve(Y))

    Y = [2, 1, 2, 1, 2, 3, 2, 3, 2]
    print(solve(Y))

    Y = [1000001, 1000000, 1000002, 1000001]
    print(solve(Y))

    Y = [2, 1, 3, 4, 5, 6, 7]
    print(solve(Y))
