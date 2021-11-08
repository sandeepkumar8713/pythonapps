# Question : Do heap sort
#
# Question Type : Easy
# Used : Make a max heap from the input array.
#        For each element swap top and bottom element of heap. Pop the max element and
#        do heapify
#        again from top for remaining element. Store the pop element in stack.
#        After the loop, pop the stack one by one to get the sorted element.
# Complexity : build heap = O(k) , heapify = O(log k),
#              total = O(n log n)

import operator


class Heap:
    def __init__(self, op):
        self.data = []
        self.size = 0
        self.op = op

    def heapify(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

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
        start = max(n // 2 - 1, 0)
        for i in range(start, -1, -1):
            self.heapify(i)

    def removeTop(self):
        self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
        temp = self.data[-1]
        del self.data[-1]
        self.size -= 1
        self.heapify(0)
        return temp

    def getTop(self):
        return self.data[0]

    def getCount(self):
        return self.size


if __name__ == "__main__":
    maxHeap = Heap(operator.gt)
    arr = [12, 11, 13, 5, 6, 7]
    maxHeap.buildHeap(arr, len(arr))
    result = []
    for i in range(0, len(arr)):
        result.append(maxHeap.removeTop())
    for i in range(0, len(arr)):
        print(result.pop(),end=" ")
