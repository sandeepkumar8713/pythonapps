# Question : Do basic heap operations such as: insert, delete key, decrease Key, remove top
# Decrease by key,value : replace the value at given position
# Delete by key : delete the element at given position
#
# Question Type : ShouldSee
# Used : Insert : Add the new element at end. Run a loop from n/2 to 0 and call heapify(i)
#        Remove top : Swap first and last element. Delete last. Call heapify(0). return last
#        Decrease by key : Replace the new element at k. Run a loop from k/2 to 0
#                          and call heapify(i)
#        Delete Key : call Decrease by Key(k, minInt). call Remove top.
# Complexity : insert = (n log n), remove top = log n,
#              decrease by key : (n log n), delete by key : (n log n)
#

import operator
import sys


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
        start = max(n / 2 - 1, 0)
        for i in range(start, -1, -1):
            self.heapify(i)

    def removeTop(self):
        self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
        temp = self.data[-1]
        del self.data[-1]
        self.size -= 1
        self.heapify(0)
        return temp

    def deleteKey(self, key):
        self.decreaseKey(key, -sys.maxint - 1)
        self.removeTop()

    def decreaseKey(self, key, value):
        self.data[key] = value
        start = max(key / 2 - 1, 0)
        for i in range(start, -1, -1):
            self.heapify(i)

    def insert(self, ele):
        self.data.append(ele)
        self.size += 1
        n = self.size
        for i in range(n/2 - 1, -1, -1):
            self.heapify(i)

    def getTop(self):
        return self.data[0]

    def getCount(self):
        return self.size


if __name__ == "__main__":
    minHeap = Heap(operator.lt)
    minHeap.insert(11)
    minHeap.insert(3)
    minHeap.insert(2)
    print(minHeap.data)
    minHeap.deleteKey(1)
    minHeap.insert(15)
    minHeap.insert(5)
    minHeap.insert(4)
    minHeap.insert(45)
    print(minHeap.data)
    print(minHeap.removeTop())
    print(minHeap.getTop())
    print(minHeap.data)
    minHeap.decreaseKey(2, 1)
    print(minHeap.getTop())
