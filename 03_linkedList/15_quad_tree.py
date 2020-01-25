# http://stackoverflow.com/questions/6179635/what-is-a-good-data-structure-for-storing-and-searching-2d-spatial-coordinates-i
# http://algs4.cs.princeton.edu/92search/QuadTree.java.html
# Question : Quad Tree ( SW, SE, NE, NW)
#
# Question Type : OddOne
# Used : Quad Tree child : SW, SE, NE, NW
#        Save few 2D points in quad tree. Print all the points within the given the rectangle.
# Complexity : O(log n)

import random


def less(a, b):
    if a <= b:
        return True
    return False


class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.NW = None
        self.NE = None
        self.SE = None
        self.SW = None


class QuadTree:
    def __init__(self):
        self.head = None

    def push(self, x,y, value):
        self.head = self.pushInChild(self.head,x,y,value)

    def pushInChild(self, root, x, y, value):
        if root is None:
            newNode = Node(x, y, value)
            return newNode

        if less(x, root.x) and less(y, root.y):
            root.SW = self.pushInChild(root.SW, x, y, value)

        elif less(x, root.x) and not less(y, root.y):
            root.NW = self.pushInChild(root.NW, x, y, value)

        elif not less(x, root.x) and less(y, root.y):
            root.SE = self.pushInChild(root.SE, x, y, value)

        elif not less(x, root.x) and not less(y, root.y):
            root.NE = self.pushInChild(root.NE, x, y, value)

        return root

    def query2D(self, rect):
        self.query2DInChild(self.head, rect)

    def query2DInChild(self, root, rect):
        if root is None:
            return

        xMin = rect["intervalX"]["xMin"]
        yMin = rect["intervalY"]["yMin"]
        xMax = rect["intervalX"]["xMax"]
        yMax = rect["intervalY"]["yMax"]

        if xMin <= root.x < xMax and yMin <= root.y < yMax:
            print(root.x, root.y, root.value)
            return

        if less(xMin, root.x) and less(yMin, root.y):
             self.query2DInChild(root.SW, rect)

        if less(xMin, root.x) and not less(yMax, root.y):
            self.query2DInChild(root.NW, rect)

        if not less(xMax, root.x) and less(yMin, root.y):
            self.query2DInChild(root.SE, rect)

        if not less(xMax, root.x) and not less(yMax, root.y):
            self.query2DInChild(root.NE, rect)


if __name__ == "__main__":
    quadTree = QuadTree()

    for i in range(200):
        x = random.randint(1, 101)
        y = random.randint(1, 101)
        quadTree.push(x, y, 5)

    rect = dict()
    rect["intervalX"] = dict()
    rect["intervalY"] = dict()
    for i in range(10):
        xMin = random.randint(1, 101)
        yMin = random.randint(1, 101)
        xMax = xMin + random.randint(1, 11)
        yMax = yMin + random.randint(1, 21)
        # print xMin, xMax, yMin, yMax
        rect["intervalX"]["xMin"] = xMin
        rect["intervalX"]["xMax"] = xMax
        rect["intervalY"]["yMin"] = yMin
        rect["intervalY"]["yMax"] = yMax

        quadTree.query2D(rect)
