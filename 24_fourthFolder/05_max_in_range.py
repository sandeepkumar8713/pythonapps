# https://www.geeksforgeeks.org/min-max-range-queries-array/
# Question : Given an array arr[0 . . . n-1]. We need to efficiently find the minimum and maximum value
# from index qs (query start) to qe (query end) where 0 <= qs <= qe <= n-1. We are given multiple queries.
#
# Used : Make a segment tree of nodes, with min and max
#        Now find min, max for given range
#        MinMaxUtils(segmentTree, currentStart, currentEnd, queryStart, queryEnd, index):
#           if queryStart <= currentStart and currentEnd <= queryEnd: return segmentTree.nodeList[index]
#           temp = Node()
#           if currentEnd < queryStart or queryEnd < currentStart:
#               temp.minimum = sys.maxint
#               temp.maximum = -sys.maxint
#               return temp
#           midIndex = getMid(currentStart, currentEnd)
#           left = MinMaxUtils(segmentTree, currentStart, midIndex,  queryStart, queryEnd, leftChildIndex)
#           right = MinMaxUtils(segmentTree, midIndex + 1, currentEnd, queryStart, queryEnd, rightChildIndex)
#           temp.minimum = min(left.minimum, right.minimum)
#           temp.maximum = max(left.maximum, right.maximum)
#           return temp
# Complexity : Tree construction O(n) Search O(log n)

import math
import sys


def getMid(startIndex, endIndex):
    return startIndex + (endIndex - startIndex)/2


class Node:
    def __init__(self):
        self.maximum = None
        self.minimum = None


class SegmentTree:
    def __init__(self):
        self.nodeList = []

    def constructUtil(self, inpArr, startIndex, endIndex, index):
        if startIndex == endIndex:
            self.nodeList[index].minimum = inpArr[startIndex]
            self.nodeList[index].maximum = inpArr[startIndex]
            return

        midIndex = getMid(startIndex, endIndex)
        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2
        self.constructUtil(inpArr, startIndex, midIndex, leftChildIndex)
        self.constructUtil(inpArr, midIndex + 1, endIndex, rightChildIndex)

        self.nodeList[index].minimum = min(self.nodeList[leftChildIndex].minimum, self.nodeList[rightChildIndex].minimum)
        self.nodeList[index].maximum = max(self.nodeList[leftChildIndex].maximum, self.nodeList[rightChildIndex].maximum)

    def construct(self, inpArr):
        n = len(inpArr)
        height = int(math.ceil(math.log(n, 2)))
        maxSize = int(2 * math.pow(2, height)) - 1
        for i in range(maxSize):
            self.nodeList.append(Node())
        self.constructUtil(inpArr, 0, n - 1, 0)
        # for i in range(maxSize):
        #     print self.nodeList[i].minimum, self.nodeList[i].maximum


def MinMaxUtils(segmentTree, currentStart, currentEnd, queryStart, queryEnd, index):
        # if query range is larger than current range
        if queryStart <= currentStart and currentEnd <= queryEnd:
            return segmentTree.nodeList[index]

        temp = Node()
        # no overlap
        if currentEnd < queryStart or queryEnd < currentStart:
            temp.minimum = sys.maxint
            temp.maximum = -sys.maxint
            return temp

        midIndex = getMid(currentStart, currentEnd)
        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2
        left = MinMaxUtils(segmentTree, currentStart, midIndex,  queryStart, queryEnd, leftChildIndex)
        right = MinMaxUtils(segmentTree, midIndex + 1, currentEnd, queryStart, queryEnd, rightChildIndex)
        temp.minimum = min(left.minimum, right.minimum)
        temp.maximum = max(left.maximum, right.maximum)
        return temp


def MinMax(segmentTree, n, queryStart, queryEnd):
    if 0 > queryStart or queryEnd > n - 1 or queryStart > queryEnd:
        return None
    return MinMaxUtils(segmentTree, 0, n - 1, queryStart, queryEnd, 0)


if __name__ == "__main__":
    inpArr = [1, 8, 5, 9, 6, 14, 2, 4, 3, 7]
    segmentTree = SegmentTree()
    segmentTree.construct(inpArr)
    rangeList = [[0, 4], [3, 7], [1, 6], [2, 5], [0, 8]]
    for item in rangeList:
        resNode = MinMax(segmentTree, len(inpArr), item[0], item[1])
        print ("Range %s %s : Min %s Max %s" % (item[0], item[1], resNode.minimum, resNode.maximum))
