# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
# Question : There are given n ropes of different lengths, we need to connect these ropes
# into one rope. The cost to connect two ropes is equal to sum of their lengths. We need
# to connect the ropes with minimum cost.
#
# For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in
# following ways.
# 1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
# 2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
# 3) Finally connect the two ropes and all ropes have connected.
#
# Total cost for connecting all ropes is 5 + 9 + 15 = 29
#
# Question Type : Easy
# Used : Maintain a minHeap. Insert inpArr and heapify it. set minCost = 0.
#        Run a loop while size(minHeap) > 1:
#           remove two elements from min heap, add them to minCost and insert
#           the sum of the two elements in minHeap
#        After the loop, print minCost
# Logic: findMinCost(inpArr):
#        heap = inpArr.copy()
#        heapq.heapify(heap)
#        minCost = 0
#        while len(heap) > 1:
#           first = heapq.heappop(heap)
#           second = heapq.heappop(heap)
#           minCost += first + second
#           heapq.heappush(heap, first + second)  # Min heap
#        return minCost
# Complexity : O(n log n)
#              Heapify takes O(n log n)
#              Heap push and pop takes O(log n)

import operator


class Heap:
    def __init__(self, op):
        self.data = []
        self.size = 0
        self.op = op

    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.op(self.data[left], self.data[largest]):
            largest = left

        if right < self.size and self.op(self.data[right], self.data[largest]):
            largest = right

        if largest is not i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest)

    def buildHeap(self, arr, n):
        self.size = n
        for i in range(n):
            self.data.append(arr[i])
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def removeTop(self):
        self.data[0], self.data[self.size - 1] = self.data[self.size - 1], self.data[0]
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

    def getCount(self):
        return self.size


def findMinCostOld(inpArr):
    minHeap = Heap(operator.lt)
    minHeap.buildHeap(inpArr, len(inpArr))
    minCost = 0

    while minHeap.getCount() > 1:
        first = minHeap.removeTop()
        second = minHeap.removeTop()
        minCost += first + second
        minHeap.insert(first + second)

    return minCost


import heapq


def findMinCost(inpArr):
    heap = inpArr.copy()
    heapq.heapify(heap)

    minCost = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        minCost += first + second
        heapq.heappush(heap, first + second)  # Min heap

    return minCost


if __name__ == "__main__":
    inpArr = [4, 3, 2, 6]
    print(findMinCost(inpArr))

    inpArr = [8, 4, 6, 12]
    print(findMinCost(inpArr))

    inpArr = [20, 4, 8, 2]
    print(findMinCost(inpArr))

    inpArr = [1, 2, 5, 10, 35, 89]
    print(findMinCost(inpArr))

    inpArr = [2, 2, 3, 3]
    print(findMinCost(inpArr))
