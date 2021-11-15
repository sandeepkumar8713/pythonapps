# https://massivealgorithms.blogspot.com/2016/08/leetcode-391-perfect-rectangle.html
# Question : Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of
# a rectangular region. Each rectangle is represented as a bottom-left point and a top-right point. For example,
# a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
#
# Question Type : ShouldSee, SimilarAdded
# Used : From the given rectangles find extreme left, bottom, right and top
#        Run a loop for each small rectangle:
#           update height and width map, with coordinates as key
#           heights[l] += h, heights[r] -= h
#           widths[b] += w, widths[t] -= w
#        Using heights and widths map, calculate sum of cumulative sum.
#        hSum = heights[left]
#        for x in range(left + 1, right):
#           heights[x] += heights[x - 1]
#           if heights[x] != heights[x - 1]: return False
#           hSum += heights[x]
#        Calculated area must be same
#        return hSum == wSum == (top - bottom) * (right - left)
# Complexity : O(n)


def updateDict(map, key, value):
    if key in map.keys():
        map[key] += value
    else:
        map[key] = value


def isRectangleCover(rectangles):
    left = min(x[0] for x in rectangles)
    bottom = min(x[1] for x in rectangles)
    right = max(x[2] for x in rectangles)
    top = max(x[3] for x in rectangles)

    heights = dict()
    widths = dict()

    for rect in rectangles:
        l, b, r, t = rect
        h, w = t - b, r - l
        updateDict(heights, l, h)
        updateDict(heights, r, -h)
        updateDict(widths, b, w)
        updateDict(widths, t, -w)

    hSum = heights[left]
    for x in range(left + 1, right):
        heights[x] += heights[x - 1]
        if heights[x] != heights[x - 1]:
            return False
        hSum += heights[x]

    wSum = widths[bottom]
    for x in range(bottom + 1, top):
        widths[x] += widths[x - 1]
        if widths[x] != widths[x - 1]:
            return False
        wSum += widths[x]

    # Calculate area
    return hSum == wSum == (top - bottom) * (right - left)


if __name__ == "__main__":
    rectangles = [[1, 1, 3, 3],
                  [3, 1, 4, 2],
                  [3, 2, 4, 4],
                  [1, 3, 2, 4],
                  [2, 3, 3, 4]]
    # rectangles = [
    #     [1, 1, 2, 3],
    #     [1, 3, 2, 4],
    #     [3, 1, 4, 2],
    #     [3, 2, 4, 4]
    # ]
    # rectangles = [
    #     [1, 1, 3, 3],
    #     [3, 1, 4, 2],
    #     [1, 3, 2, 4],
    #     [3, 2, 4, 4]
    # ]
    # rectangles = [
    #     [1, 1, 3, 3],
    #     [3, 1, 4, 2],
    #     [1, 3, 2, 4],
    #     [2, 2, 4, 4]
    # ]
    print(isRectangleCover(rectangles))
