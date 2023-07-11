# https://leetcode.com/problems/minimize-deviation-in-array/
# Question : You are given an array nums of n positive integers.
# You can perform two types of operations on any element of the array any number of times:
#     If the element is even, divide it by 2.
#         For example, if the array is [1,2,3,4], then you can do this operation on the
#         last element, and the array will be [1,2,3,2].
#     If the element is odd, multiply it by 2.
#         For example, if the array is [1,2,3,4], then you can do this operation on the
#         first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.
# Return the minimum deviation the array can have after performing some number of operations.
#
# Question Type : Generic
# Used : The intuition behind the approach is to convert odd numbers to even numbers by multiplying
#        them by 2 and then inserting them into a max heap. Also keep track of minimum_number.
#        We can then perform division operations on the maximum element in the heap until we
#        get an odd number, and then insert it back into the heap. We continue this process
#        until we can't divide the maximum element in the heap.
#        Logic :
#        while len(heap) != 0:
#           top = -heapq.heappop(heap)
#           min_deviation = min(min_deviation, top - minimum_number)
#           if top % 2 == 0:
#               minimum_number = min(minimum_number, top // 2)
#               heapq.heappush(heap, -top // 2)
#           else:
#               break
#        return min_deviation
# Complexity : O(n log n)


import heapq
import sys

def minimumDeviation(nums):
    min_deviation = sys.maxsize
    minimum_number = sys.maxsize
    heap = []
    for num in nums:
        if num % 2 == 0:
            heapq.heappush(heap, -num)
            minimum_number = min(minimum_number, num)
        else:
            heapq.heappush(heap, -num * 2)
            minimum_number = min(minimum_number, num * 2)

    while len(heap) != 0:
        top = -heapq.heappop(heap)
        min_deviation = min(min_deviation, top - minimum_number)
        if top % 2 == 0:
            minimum_number = min(minimum_number, top // 2)
            heapq.heappush(heap, -top // 2)
        else:
            break

    return min_deviation


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print (minimumDeviation(nums))
