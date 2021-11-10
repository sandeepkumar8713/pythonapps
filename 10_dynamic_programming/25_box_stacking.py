# CTCI : Q8_13_Stack_of_Boxes
# https://www.geeksforgeeks.org/box-stacking-problem-dp-22/
# Question : You are given a set of n types of rectangular 3-D boxes, where the i^th box has
# height h(i), width w(i) and depth d(i) (all real numbers). You want to create a stack of
# boxes which is as tall as possible, but you can only stack a box on top of another box if
# the dimensions of the 2-D base of the lower box are each strictly larger than those of the
# 2-D base of the higher box. Of course, you can rotate a box so that any side functions as
# its base. It is also allowable to use multiple instances of the same type of box.
#
# Question Type : Generic, SimilarAdded
# Used : Make a class of Box with field : height, width and depth.
#        Make a list of box objects with all 3 possible rotation
#        Sort the list in decreasing order based on area. (width * depth)
#        Now use longest increasing sub sequence(LIS) in dynamic programming approach.
#        Maintain a list MSH where MSH[i] now stores the maximum stake height ending with box i.
#        Initialize MSH[i] with height[i].
#        MSH(i) = Maximum possible Stack Height with box i at top of stack
#        Run 2 loops from i : 1 to n and j : 0 to i
#           if depth[j] > depth[i] and width[j] > width[i] and MSH[i] < MSH[j] + height[i]:
#               MSH[i] = MSH[j] + height[i]
#        return max(MSH)
# Complexity : O(n^2)

DIMENSION_SIZE = 3


class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def getArea(self):
        return self.width * self.depth

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

    def getWidth(self):
        return self.width


def getMaxStackSize(inpMat):
    allBoxList = []
    for dimension in inpMat:
        for i in range(DIMENSION_SIZE):
            start = i
            count = 0
            rotatedDimension = []
            while count < DIMENSION_SIZE:
                rotatedDimension.append(dimension[start])
                start = (start + 1) % DIMENSION_SIZE
                count += 1
            allBoxList.append(Box(rotatedDimension[0], rotatedDimension[1], rotatedDimension[2]))

    # Sort in decreasing order based on area.
    allBoxList.sort(key=lambda x: x.getArea(), reverse=True)

    MSH = []
    for box in allBoxList:
        MSH.append(box.getHeight())
    n = len(allBoxList)

    # This is used in longest increasing sub sequence in dynamic programming approach
    for i in range(1, n):
        for j in range(0, i):
            if allBoxList[i].getDepth() < allBoxList[j].getDepth() and \
                    allBoxList[i].getWidth() < allBoxList[j].getWidth() and \
                    MSH[i] < MSH[j] + allBoxList[i].getHeight():
                    MSH[i] = MSH[j] + allBoxList[i].getHeight()

    # MSH[i] now stores the maximum stake height ending with box i
    return max(MSH)


if __name__ == "__main__":
    inpMat = [[4, 6, 7],
              [1, 2, 3],
              [4, 5, 6],
              [10, 12, 32]]
    print(getMaxStackSize(inpMat))
