# https://leetcode.com/discuss/interview-question/417267/some-new-amazon-vo-questions
# Given streaming data, find the median in the K Largest Top Elements.
# Similar : 05_heap/01_median_in_stream.py
#
# Example: K =. 3
# [. 1] ->. 1
# [1,2] -> for 1.5
# [l, 2,3] -> 2
# [1,2,3,1] -> 2
# [1,2,3,1,10] -> 3
#
# Question Type : SimilarAdded
# Used : Maintain left max heap and right min heap whose size should be less than k.
#        When adding element, if element count is equal to k. Remove last element from left_max_heap
#        Add new element in left_max_heap.
#        Pop top ele from left_max_heap and insert in right_min_heap
#        if right_min_heap has more elements than left_max_heap:
#           pop top ele from right_min_heap and insert in left_max_heap
#        left_max_heap should have more or equal size than right_min_heap.
# Logic: def add(self, ele):
#        if len(self.left_max_heap) + len(self.right_min_heap) == self.k:
#           delete_last_element(self.left_max_heap)
#        heapq.heappush(self.left_max_heap, -ele)
#        temp = -heapq.heappop(self.left_max_heap)
#        heapq.heappush(self.right_min_heap, temp)
#        if len(self.left_max_heap) < len(self.right_min_heap):
#           temp = heapq.heappop(self.right_min_heap)
#           heapq.heappush(self.left_max_heap, -temp)
#
#        def find_median(self):
#        stream_len = len(self.left_max_heap) + len(self.right_min_heap)
#        stream_len = min(stream_len, self.k)
#        if stream_len % 2 == 0:
#           return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2.0
#        else:
#           return -self.left_max_heap[0]
# Complexity : O(log k) for each add operation

import heapq


def delete_last_element(heap):
    if len(heap) >= 2:
        if heap[-1] < heap[-2]:
            heap.pop(-2)
            return
    heap.pop(-1)


class StreamMedian:
    def __init__(self, k):
        self.k = k
        self.left_max_heap = []
        self.right_min_heap = []

    def add(self, ele):
        if len(self.left_max_heap) + len(self.right_min_heap) == self.k:
            delete_last_element(self.left_max_heap)

        heapq.heappush(self.left_max_heap, -ele)
        temp = -heapq.heappop(self.left_max_heap)
        heapq.heappush(self.right_min_heap, temp)

        if len(self.left_max_heap) < len(self.right_min_heap):
            temp = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -temp)

    def find_median(self):
        stream_len = len(self.left_max_heap) + len(self.right_min_heap)
        stream_len = min(stream_len, self.k)
        if stream_len % 2 == 0:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2.0
        else:
            return -self.left_max_heap[0]


if __name__ == "__main__":
    stream_median = StreamMedian(3)
    inp_arr = [1, 2, 3, 1, 10]
    for ele in inp_arr:
        stream_median.add(ele)
        print(stream_median.find_median())

    print("")
    stream_median = StreamMedian(4)
    inp_arr = [1, 2, 3, 4]
    for ele in inp_arr:
        stream_median.add(ele)
        print(stream_median.find_median())
