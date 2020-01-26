# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
# Question :  Given a stream of integers, a value k and a value w, consider the integers in the window w
# and chop off greater k and smaller k elements from the window w. From the remaining elements,
# compute the average.
#
# Question Type : Generic
# Used : make use of Min and Max heaps. Similar to find kth largest in stream.
#       For smaller values use Max Heap, For larger value use Min heap. For middle value, maintain both min and max heap
# Complexity : insert = (w log w), deleteByKey : (w log w)

import operator
import sys
totalSum = 0
totalCount = 0


class Heap:
    def __init__(self, op):
        self.data = []
        self.size = 0
        self.op = op

    def heapify(self, i):
        smallest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < self.size and self.op(self.data[left], self.data[smallest]):
            smallest = left

        if right < self.size and self.op(self.data[right], self.data[smallest]):
            smallest = right

        if smallest is not i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest)

    def buildHeap(self, arr, n):
        self.size = n
        for i in range(n):
            self.data.append(arr[i])
        for i in range(n//2 - 1, -1, -1):
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
        for i in range(n//2 - 1, -1, -1):
            self.heapify(i)

    def getTop(self):
        return self.data[0]

    def getCount(self):
        return self.size

    def getLast(self):
        return self.data[self.size]

    def search(self, value):
        if value in self.data:
            return self.data.index(value)
        else:
            return -1

    def deleteByKey(self, key):
        if self.op == operator.lt:
            topValue = -sys.maxsize
        else:
            topValue = sys.maxsize
        self.decreaseKey(key, topValue)
        self.removeTop()

    def decreaseKey(self, key, value):
        self.data[key] = value
        start = max(key / 2 - 1, 0)
        for i in range(start, -1, -1):
            self.heapify(i)

    def deleteByValue(self, value):
        key = self.search(value)
        if key != -1:
            self.deleteByKey(key)
            return 1
        else:
            return 0

def checkElementInMiddle(ele, middleMinHeap, middleMaxHeap):
    if middleMinHeap.size == 0:
        return False

    if ele >= middleMinHeap.getTop() and ele <= middleMaxHeap.getTop():
        return True

def insertInMiddle(ele, middleMinHeap, middleMaxHeap):
    global totalSum, totalCount
    middleMaxHeap.insert(ele)
    middleMinHeap.insert(ele)
    totalSum += ele
    totalCount += 1

def deleteInMiddle(ele, middleMinHeap, middleMaxHeap):
    global totalSum, totalCount
    middleMaxHeap.deleteByValue(ele)
    middleMinHeap.deleteByValue(ele)
    totalSum -= ele
    totalCount -= 1

def showAverage(inpArr, w, k):
    global totalSum, totalCount
    startIndex = 0
    endIndex = k

    leftMaxHeap = Heap(operator.gt)
    rightMinHeap = Heap(operator.lt)
    middleMaxHeap = Heap(operator.gt)
    middleMinHeap = Heap(operator.lt)

    i = 0
    while i < k:
        print(None,end=" ")
        i += 1

    rightMinHeap.buildHeap(inpArr, k)
    leftMaxHeap.buildHeap(inpArr, k)

    while (endIndex - startIndex + 1) <= w:
        x = inpArr[endIndex]
        insertInEdge = False
        if x >= rightMinHeap.getTop():
            insertInEdge = True
            poppedElement = rightMinHeap.removeTop()
            rightMinHeap.insert(x)
            if (endIndex + startIndex + 1) > 2*k:
                insertInMiddle(poppedElement, middleMinHeap, middleMaxHeap)

        if x <= leftMaxHeap.getTop():
            insertInEdge = True
            poppedElement = leftMaxHeap.removeTop()
            leftMaxHeap.insert(x)
            if (endIndex + startIndex + 1) > 2 * k:
                insertInMiddle(poppedElement, middleMinHeap, middleMaxHeap)

        if not insertInEdge:
            insertInMiddle(x, middleMinHeap, middleMaxHeap)

        if totalCount == 0:
            print(None,end=" ")
        else:
            print(totalSum / float(totalCount),end=" ")

        endIndex += 1

    endIndex -= 1
    while endIndex < len(inpArr) - 1:
        poppedElement = None
        oldEle = inpArr[startIndex]

        if checkElementInMiddle(oldEle, middleMinHeap, middleMaxHeap):
            deleteInMiddle(oldEle, middleMinHeap, middleMaxHeap)
        else:
            if oldEle <= leftMaxHeap.getTop():
                leftMaxHeap.deleteByValue(oldEle)
            else:
                rightMinHeap.deleteByValue(oldEle)

        startIndex += 1
        endIndex += 1

        x = inpArr[endIndex]
        insertInEdge = False
        if x >= rightMinHeap.getTop():
            insertInEdge = True
            poppedElement = rightMinHeap.removeTop()
            rightMinHeap.insert(x)
            if (endIndex + startIndex + 1) > 2 * k:
                insertInMiddle(poppedElement, middleMinHeap, middleMaxHeap)
        elif x <= leftMaxHeap.getTop():
            insertInEdge = True
            poppedElement = leftMaxHeap.removeTop()
            leftMaxHeap.insert(x)
            if (endIndex + startIndex + 1) > 2 * k:
                insertInMiddle(poppedElement, middleMinHeap, middleMaxHeap)

        if not insertInEdge:
            insertInMiddle(x, middleMinHeap, middleMaxHeap)

        while leftMaxHeap.size < k:
            ele = middleMinHeap.getTop()
            deleteInMiddle(ele, middleMinHeap, middleMaxHeap)
            leftMaxHeap.insert(ele)

        while rightMinHeap.size < k:
            ele = middleMaxHeap.getTop()
            deleteInMiddle(ele, middleMinHeap, middleMaxHeap)
            rightMinHeap.insert(ele)

        if totalCount == 0:
            print(None,end=" ")
        else:
            print(totalSum / float(totalCount),end=" ")


if __name__ == "__main__":
    inpArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # inpArr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    w = 6
    k = 2
    showAverage(inpArr, w, k)
