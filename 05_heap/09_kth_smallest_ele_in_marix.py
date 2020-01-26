# https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/
# Question : Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth
# smallest element in the given 2D array.
#
# Used : The idea is to use min heap. Following are detailed step.
#        1) Build a min heap of elements from first row. A heap entry also stores row number and column number.
#        2) Do following k times.
#           a) Get minimum element (or root) from min heap.
#           b) Find row number and column number of the minimum element.
#           c) Replace root with the next element from same column and min-heapify the root.
#        3) Return the last extracted root.
# Complexity : O(n + k Log n)

import operator


class Node:
    def __init__(self, ele, i, j):
        self.ele = ele
        self.i = i
        self.j = j


class Heap:
    def __init__(self, op):
        self.data = []
        self.size = 0
        self.op = op

    def heapify(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < self.size and self.op(self.data[left].ele, self.data[largest].ele):
            largest = left

        if right < self.size and self.op(self.data[right].ele, self.data[largest].ele):
            largest = right

        if largest is not i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest)

    def buildHeap(self, arr, n):
        self.size = n
        for i in range(n):
            self.data.append(arr[i])
        start = n//2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def removeTop(self):
        self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
        temp = self.data[-1]
        del self.data[-1]
        self.size -= 1
        self.heapify(0)
        return temp

    def insert(self, ele):
        self.data.append(ele)
        self.size += 1
        n = self.size
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)


def kthSmallest(inpMat, k):
    minHeap = Heap(operator.lt)
    nodeList = []
    for j in range(len(inpMat[0])):
        node = Node(inpMat[0][j], 0, j)
        nodeList.append(node)

    minHeap.buildHeap(nodeList, len(nodeList))
    minNode = None
    for it in range(k):
        minNode = minHeap.removeTop()
        if minNode is not None and (minNode.i + 1) < len(inpMat):
            node = Node(inpMat[minNode.i+1][minNode.j], minNode.i + 1, minNode.j)
            minHeap.insert(node)
    if minNode is None:
        return None
    else:
        return minNode.ele


if __name__ == "__main__":
    inpMat = [[10, 20, 30, 40],
              [15, 25, 35, 45],
              [25, 29, 37, 48],
              [32, 33, 39, 50]]
    print(kthSmallest(inpMat, 7))
