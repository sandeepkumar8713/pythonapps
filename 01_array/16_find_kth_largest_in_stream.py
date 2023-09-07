# CTCI : Q17_14_Smallest_K
# http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Question : Given an infinite stream of integers, find the k'th largest element at any point of time.
# Similar : https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
# Write an efficient program for printing k largest elements in an array.
# Elements in array can be in any order. (Here answer will be whole min heap of size k.)
#
# stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
# k = 3
# Output: {_,   _, 10, 11, 20, 40, 50,  50, ...}
#
# Question Type : Asked
# Used : Maintain a min heap which saves top k elements at any given point of time.
#        For first k elements make a min heap
#        Now loop through the remaining elements, if x is greater than top of heap
#        replace and heapify.
#        for each iteration top of the heap is kth largest element till now.\
# Logic: mh = MinHeap()
#        mh.buildHeap(arr, k)
#        result.append(mh.getMin())
#        for i in range(k, len(arr)):
#           x = arr[i]
#           if x > mh.getMin():
#               mh.replaceMin(x)
#           result.append(mh.getMin())
#        print(result)
# Complexity : build heap = O(k) , heapify = O(log k), search and replace = O( n log k)
#              total = O( k log k + n log k)


class MinHeap:
    def __init__(self):
        self.data = []
        self.size = 0

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.data[left] < self.data[smallest]:
            smallest = left

        if right < self.size and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest is not i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest)

    def buildHeap(self, arr, n):
        self.size = n
        for i in range(n):
            self.data.append(arr[i])
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def replaceMin(self, x):
        self.data[0] = x
        self.heapify(0)

    def getMin(self):
        return self.data[0]


def kindKthLargest(arr, k):
    result = []
    i = 0
    while i < k - 1:
        result.append(-1)
        i += 1

    mh = MinHeap()
    mh.buildHeap(arr, k)
    result.append(mh.getMin())

    for i in range(k, len(arr)):
        x = arr[i]
        if x > mh.getMin():
            mh.replaceMin(x)

        result.append(mh.getMin())
    print(result)


if __name__ == "__main__":
    arr = [23, 10, 15, 70, 5, 80, 100]
    k = 3
    print("kth largest element in stream:"),
    kindKthLargest(arr, k)
