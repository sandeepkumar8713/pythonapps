# https://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/
# Question : Given k sorted lists of integers of size n each, find the smallest range that includes at least
# element from each of the k lists. If more than one smallest ranges are found, print any one of them.
#
# Input:
# K = 3
# arr1[] : [4, 7, 9, 12, 15]
# arr2[] : [0, 8, 10, 14, 20]
# arr3[] : [6, 12, 16, 30, 50]
# Output:
# The smallest range is [6 8]
# Explanation: Smallest range is formed by number 7 from first list, 8 from second list and 6 from third list.
#
# Question Type : Generic
# Used : Make a structure Node : ele, i, j where ele is the element in array, along with its index in inpLists and next
#           element index in that array. Make a min heap which would have above mentioned Node as data
#        Push first element of each array of inpList in the min Heap as Node and keep comparing and updating
#        maxVal if required. Heapify the minHeap after all the elements are pushed.
#        While True: Pop top node from min heap. Assign minVal = node.ele. Compare valRange with diff of minVal and
#                    maxVal and update valRange, startElement and endElement if required.
#                    If j has reached its array end then break; if node.j < n: break
#                    Else read next element using node.j, Make a node out of it and insert in minHeap. Compare new
#                    element with maxVal and update if required
#        After the loop: print startElement, endElement
# Complexity : (nk log nk)

import sys
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


def findSmallestRange(inpLists):
    k = len(inpLists)
    n = len(inpLists[0])
    minVal = sys.maxsize
    maxVal = -sys.maxsize
    valRange = sys.maxsize

    startElement = 0
    endElement = 0

    heapArr = []
    for i in range(k):
        # Store the first element of each array, along with its index in inpLists and next element index in that array
        ele = inpLists[i][0]
        node = Node(ele, i, 1)
        heapArr.append(node)

        if ele > maxVal:
            maxVal = ele

    minHeap = Heap(operator.lt)
    minHeap.buildHeap(heapArr, len(heapArr))

    while True:
        node = minHeap.removeTop()
        minVal = node.ele

        if valRange > (maxVal - minVal + 1):
            valRange = maxVal - minVal + 1
            startElement = minVal
            endElement = maxVal

        if node.j >= n:
            break

        ele = inpLists[node.i][node.j]
        newNode = Node(ele, node.i, node.j + 1)
        minHeap.insert(newNode)

        if ele > maxVal:
            maxVal = ele

    print(startElement, endElement)


if __name__ == "__main__":
    inpLists = [[4, 7, 9, 12, 15],
                [0, 8, 10, 14, 20],
                [6, 12, 16, 30, 50]]
    findSmallestRange(inpLists)
