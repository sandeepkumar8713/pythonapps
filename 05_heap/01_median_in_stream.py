# CTCI : Q17_20_Continuous_Median
# https://leetcode.com/problems/find-median-from-data-stream/
# Question : Given that integers are read from a data stream. Find median of elements read so for in efficient way.
# For simplicity assume there are no duplicates.
# input =  5, 15, 1, 3
# output = 5, 10, 5, 4
#
# Question Type : Generic
# Used : Make a left max heap and right max heap. Iterate over the input elements.
#       If the left heap has more elements
#           If new element is less than median then push in left, after moving top element to right
#           else push in right
#           get top from both the heaps and average out to get median
#       If both heap have same number of elements
#           If new element is less than median then push in left and get top element from it as median
#           else push in right anf get top element from it as median
#       If the right heap has more elements
#           If new element is less median then push in left
#           else push in right, after moving top element to left
#           get top from both the heaps and average out to get median
# Complexity : build heap = O(k) , heapify = O(log k),
#              total = O(n log n)

import operator


def signum(a, b):
    if a is b:
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1


def average(a, b):
    return (a+b)/2


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
        for i in range(n/2 - 1, -1, -1):
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


def getMedian(ele, median, leftHeap, rightHeap):
    sig = signum(leftHeap.getCount(), rightHeap.getCount())

    # left has more element
    if sig == 1:
        if ele < median[0]:
            rightHeap.insert(leftHeap.removeTop())
            leftHeap.insert(ele)
        else:
            rightHeap.insert(ele)
        median[0] = average(leftHeap.getTop(), rightHeap.getTop())

    # equal number of left and right
    if sig == 0:
        if ele < median[0]:
            leftHeap.insert(ele)
            median[0] = leftHeap.getTop()
        else:
            rightHeap.insert(ele)
            median[0] = rightHeap.getTop()

    # right has more element
    if sig == -1:
        if ele < median[0]:
            leftHeap.insert(ele)
        else:
            leftHeap.insert(rightHeap.removeTop())
            rightHeap.insert(ele)
        median[0] = average(leftHeap.getTop(), rightHeap.getTop())


if __name__ == "__main__":
    maxHeap = Heap(operator.gt)
    minHeap = Heap(operator.lt)
    median = [0]
    # arr = [5, 15, 1, 3]
    arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    for ele in arr:
        getMedian(ele, median, maxHeap, minHeap)
        print(median[0], end=" ")
