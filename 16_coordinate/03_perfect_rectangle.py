# https://leetcode.com/problems/perfect-rectangle/
# Question : Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents
# an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and
# the top-right point of it is (ai, bi). Return true if all the rectangles together form an
# exact cover of a rectangular region.
#
# Question Type : Generic
# Used : Loop over the given list, calculate the the area of each rectangle. Keep
#        updating total area, also make all the 4 points of rectangle, add it in the
#        set if not present else pop out from the set.
#        After the loop, only 4 points should be left in the set. If not return false.
#        Now sort these 4 points, calculate area of this big rectangle and compare
#        with totalArea calculated earlier.
#        Logic :
#        for botX, botY, topX, topY in rectangles:
#           totalArea += (topX - botX) * (topY - botY)
#           for points in [(botX, botY), (botX, topY), (topX, botY), (topX, topY)]:
#               if points in corner_point: corner_point.remove(points)
#               else: corner_point.add(points)
#        if len(corner_point) != 4: return False
#        corner_point = sorted(list(corner_point), key=lambda point: (point[0], point[1]))
#        botX, botY = corner_point[0][0], corner_point[0][1]
#        topX, topY = corner_point[3][0], corner_point[3][1]
#        return totalArea == (topX - botX) * (topY - botY)
# Complexity : O(n) where n is number of rectangles


def isRectangleCover(rectangles):
    totalArea = 0
    corner_point = set()

    for botX, botY, topX, topY in rectangles:
        totalArea += (topX - botX) * (topY - botY)
        for points in [(botX, botY), (botX, topY), (topX, botY), (topX, topY)]:
            if points in corner_point:
                corner_point.remove(points)
            else:
                corner_point.add(points)

    if len(corner_point) != 4:  # a rectangle should only have 4 corner points
        return False
    # check the area is equal or not
    corner_point = sorted(list(corner_point), key=lambda point: (point[0], point[1]))
    botX, botY = corner_point[0][0], corner_point[0][1]
    topX, topY = corner_point[3][0], corner_point[3][1]
    return totalArea == (topX - botX) * (topY - botY)


if __name__ == "__main__":
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print(isRectangleCover(rectangles))

    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]
    print(isRectangleCover(rectangles))
