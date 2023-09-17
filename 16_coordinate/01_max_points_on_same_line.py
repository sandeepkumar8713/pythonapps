# https://www.geeksforgeeks.org/count-maximum-points-on-same-line/
# https://leetcode.com/problems/max-points-on-a-line/
# Question : Given N point on a 2D plane as pair of (x, y) co-ordinates, we need to find maximum number of point
# which lie on the same line.
#
# Examples:
# Input : points[] = {-1, 1}, {0, 0}, {1, 1},
#                     {2, 2}, {3, 3}, {3, 4}
# Output : 4
# Then maximum number of point which lie on same
# line are 4, those point are {0, 0}, {1, 1}, {2, 2}, {3, 3}
#
# Question Type : ShouldSee
# Used : For each point p, calculate its slope with other points and use a map to record how many
#        points have same slope, by which we can find out how many points are on same line with p as
#        their one point. For each point keep doing the same thing and update the maximum number of
#        point count found so far. Make sure to keep separate count of overlapping and vertical
#        points(xdiff will be 0).
# Logic: for i in range(0, len(points)-1):
#           curMax = overlapPoints = verticalPoints = 0
#           slopeMap = dict()
#           for j in range(i+1, len(points)):
#               if points[i].x == points[j].x and points[i].y == points[j].y:
#                   overlapPoints += 1
#               elif points[i].x == points[j].x:
#                   verticalPoints += 1
#               else:
#                   slope = findSlope(points[i], points[j])
#                   if slope in slopeMap.keys(): slopeMap[slope] += 1
#                   else: slopeMap[slope] = 1
#                   curMax = max(curMax, slopeMap[slope])
#               curMax = max(curMax, verticalPoints)
#           maxPoint = max(maxPoint, curMax + overlapPoints + 1)
# Complexity : O(n^2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)


# gcd/hcf
def findHcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


def findSlope(pointA, pointB):
    yDif = pointB.y - pointA.y
    xDif = pointB.x - pointA.x

    # hcf = findHcf(xDif, yDif)
    # xDif = xDif / hcf
    # yDif = yDif / hcf

    return float(yDif) / float(xDif)


def maxPointOnSameLine(points):
    if len(points) < 2:
        return len(points)

    maxPoint = 0
    for i in range(0, len(points)-1):
        curMax = overlapPoints = verticalPoints = 0
        slopeMap = dict()
        for j in range(i+1, len(points)):
            if points[i].x == points[j].x and points[i].y == points[j].y:
                overlapPoints += 1
            elif points[i].x == points[j].x:
                verticalPoints += 1
            else:
                slope = findSlope(points[i], points[j])
                if slope in slopeMap.keys():
                    slopeMap[slope] += 1
                else:
                    slopeMap[slope] = 1
                curMax = max(curMax, slopeMap[slope])

            curMax = max(curMax, verticalPoints)

        # updating global maximum by current point's maximum
        maxPoint = max(maxPoint, curMax + overlapPoints + 1)

    return maxPoint


if __name__ == "__main__":
    inpMat = [[-1, 1], [0, 0], [1, 1], [2, 2],
              [3, 3], [3, 4]]

    points = []
    for item in inpMat:
        points.append(Point(item[0], item[1]))

    print(maxPointOnSameLine(points))

    inpMat = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points = []
    for item in inpMat:
        points.append(Point(item[0], item[1]))

    print(maxPointOnSameLine(points))
