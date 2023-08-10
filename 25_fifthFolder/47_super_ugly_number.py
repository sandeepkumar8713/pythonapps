# https://leetcode.com/problems/super-ugly-number/
# Similar : https://leetcode.com/problems/ugly-number-ii/
# Question : A super ugly number is a positive integer whose prime factors are in the array primes.
# Given an integer n and an array of integers primes, return the nth super ugly number.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
# Example : Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 super ugly numbers given primes = [2,7,13,19].
#
# Question Type : OddOne
# Used : The idea, is to insert all the prime numbers into minHeap and multiply numbers to them,
#        and keep popping out unless we get nth number.
#        p array keeps track of index of ans array which is not yet multiplied
#        Run a loop n-1 times, as we know first ans[0] = 1
#           append top element of heap to ans and set as curr
#           Run a loop while top ele == curr
#              find out the index of prime factor of top element
#              pop out the top element
#              increment the value of p[i] by 1
#              multiply prime number with ans element indexed at p[i]
#        return ans[-1]
# Logic: p = [0] * len(primes), ans = [1], heap = []
#        for i in range(len(primes)):
#           heapq.heappush(heap, (primes[i] * ans[p[i]], i))
#        for _ in range(n - 1):
#           curr = heap[0][0], ans.append(curr)
#           while heap and heap[0][0] == curr:
#               i = heap[0][1], heapq.heappop(heap)
#               p[i] += 1
#               heapq.heappush(heap, (primes[i] * ans[p[i]], i))
#        return ans[-1]
# Complexity : O(n * m log m) where m is size of prime array and we have to find nth number

import heapq


def nthSuperUglyNumber(n, primes):
    p = [0] * len(primes)  # p[i] stores the index of ugly number in ans that not yet multiplied with primes[i]
    ans = [1]
    heap = []

    for i in range(len(primes)):
        heapq.heappush(heap, (primes[i] * ans[p[i]], i))

    for _ in range(n - 1):
        curr = heap[0][0]
        ans.append(curr)

        while heap and heap[0][0] == curr:  # To avoid, common factor 2*7 = 14, so 14 will come twice
            i = heap[0][1]
            heapq.heappop(heap)
            p[i] += 1
            heapq.heappush(heap, (primes[i] * ans[p[i]], i))

    return ans[-1]


if __name__ == "__main__":
    n = 12
    primes = [2, 7, 13, 19]
    print(nthSuperUglyNumber(n, primes))
