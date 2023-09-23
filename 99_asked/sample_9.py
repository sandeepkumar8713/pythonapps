# https://www.chegg.com/homework-help/questions-and-answers/n-empty-glasses-capacity-1-2--n-liters-exactly-one-glass-unique-capacity--want-pour-exactl-q99064844
# Question : There are N empty glasses with a capacity of 1, 2, N liters (there is exactly one glass of each
# unique capacity). You want to pour exactly K liters of water into glasses. Each glass may be either full or
# empty (a glass cannot be partially filled). What is the minimum number of glasses that you need to contain
# K liters of water?
# Write a function: def solution (N, K)
# that, given two integers N and K, returns the minimum number of glasses that are needed to contain exactly
# K liters of water. If it is not possible to pour exactly K liters of water into glasses then the function
# should return -1.
#
# Examples: Given N = 5 and K = 8, the function should return 2.
# There are five glasses of capacity 1, 2, 3, 4 and 5.
# You can use two glasses with capacity 3 and 5 to hold 8 liters of water.

import bisect


def solution(N, K):
    # Implement your solution here
    if N <= 0 or K <= 0:
        return -1

    total_capacity = (N * (N + 1)) / 2
    if K > total_capacity:
        return -1

    # count = 0
    # remaining_water = K
    # for i in range(N, 0, -1):
    #     if i <= remaining_water:
    #         remaining_water -= i
    #         count += 1
    #     if remaining_water == 0:
    #         return count

    count = 0
    arr = [i for i in range(1, N + 1)]
    picked_up = set()
    remaining_water = K
    candidate = N - 1
    while remaining_water > 0:
        i = bisect.bisect_right(arr, remaining_water, 0, candidate)
        print(f"i {i}")

        candidate = i
        value = arr[candidate]
        if candidate not in picked_up and value <= remaining_water:
            picked_up.add(candidate)
            remaining_water -= value
            count += 1

        candidate -= 1

    return count


if __name__ == "__main__":
    N = 5
    K = 8
    assert solution(N, K) == 2
    #
    #
    # N = 4
    # K = 10
    # assert solution(N, K) == 4
    #
    # N = 1
    # K = 2
    # assert solution(N, K) == -1
    #
    # N = 10
    # K = 5
    # assert solution(N, K) == 1

    # N = 3
    # K = 8
    # assert solution(N, K) == -1

    # N = 3
    # K = 1
    # assert solution(N, K) == 1
    #
    # i = bisect.bisect_right([1, 2, 3], 35)
    # print(i)
