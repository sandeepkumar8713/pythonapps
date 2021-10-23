# https://leetcode.com/problems/maximum-number-of-visible-points/
# Question : You are given an array points, an integer angle, and your location, where
# location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.
# Initially, you are facing directly east from your position. You cannot move from your position,
# but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees
# is represented by angle, determining how wide you can see from any given view direction.
# Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is
# the inclusive range of angles [d - angle/2, d + angle/2]. You can see some set of points if,
# for each point, the angle formed by the point, your position, and the immediate east direction
# from your position is in your field of view. There can be multiple points at one coordinate.
# There may be points at your location, and you can always see these points regardless of your
# rotation. Points do not obstruct your vision to other points. Return the maximum number
# of points you can see.
#
# Example : Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
# Output: 1
# Explanation: You can only see one of the two points, as shown above.
#
# Question Type : ShouldSee
# Used : From that users location, find arc angle for all the point except which are at loc.
#        Sort the given angle array. Append the same array with 360 adding to each element.
#        Keep leftIndex at 0. Loop over the sorted array by increment rightIndex.
#        If angle diff b/w leftIndex and rightIndex is more than povAngle, we can ignore
#        the leftIndex and increment it.
#        Count points b/w left and right index and compare it with max res.
#        After the loop return maxRes + self points if any.
#        Logic :
#        for p in points:
#        if p == loc:
#           nloc += 1
#        else:
#           array.append(math.degrees(math.atan2(p[1] - loc[1], p[0] - loc[0])))
#        array.sort()
#        angles = array + [a + 360 for a in array]
#        leftIndex, res = 0, 0
#        for rightIndex in range(len(angles)):
#           if angles[rightIndex] - angles[leftIndex] > povAngle:
#               leftIndex += 1
#           res = max(rightIndex - leftIndex + 1, res)
#        return res + nloc
# Complexity : O(n log n) where n is number of points

import math


def visiblePoints(points, povAngle, loc):
    array = []
    nloc = 0
    for p in points:
        if p == loc:
            nloc += 1
        else:
            array.append(math.degrees(math.atan2(p[1] - loc[1], p[0] - loc[0])))

    array.sort()
    # to cover points with angle 10 and 350 degree
    angles = array + [a + 360 for a in array]

    leftIndex, res = 0, 0
    for rightIndex in range(len(angles)):
        if angles[rightIndex] - angles[leftIndex] > povAngle:
            # Can't cover both left and right, skip left
            leftIndex += 1

        res = max(rightIndex - leftIndex + 1, res)

    return res + nloc


if __name__ == "__main__":
    points = [[1, 0], [2, 1]]
    angle = 13
    location = [1, 1]
    print(visiblePoints(points, angle, location))

    points = [[2, 1], [2, 2], [3, 4], [1, 1]]
    angle = 90
    location = [1, 1]
    print(visiblePoints(points, angle, location))
