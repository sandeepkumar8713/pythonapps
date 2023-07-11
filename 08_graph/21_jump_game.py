# https://leetcode.com/problems/jump-game-iv/
# Question : Given an array of integers arr, you are initially positioned at the
# first index of the array. In one step you can jump from index i to index:
#     i + 1 where: i + 1 < arr.length.
#     i - 1 where: i - 1 >= 0.
#     j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
# Notice that you can not jump outside of the array at any time.
#
# Example : Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is
# the last index of the array.
#
# Question Type : ShouldSee
# Used : Make a index dict of the given array.
#        Do BFS over the array, with allowed neighbors as +1, -1 and same value index.
#        We get shorted path fast.
# Complexity : O(n + n log n)

from collections import deque, defaultdict

def minJumps(arr):
    n = len(arr)
    if n == 1:
        return 0

    # build index map of values in the array
    index_map = defaultdict(list)
    for i, val in enumerate(arr):
        index_map[val].append(i)

    # BFS traversal
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        curr_index, curr_jumps = queue.popleft()
        if curr_index == n - 1:
            return curr_jumps
        visited.add(curr_index)

        # add adjacent indices
        for neighbor in [curr_index - 1, curr_index + 1]:
            if 0 <= neighbor < n and neighbor not in visited:
                queue.append((neighbor, curr_jumps + 1))

        # add indices with same value
        if arr[curr_index] in index_map:
            for neighbor in index_map[arr[curr_index]]:
                if neighbor not in visited:
                    queue.append((neighbor, curr_jumps + 1))
            # clear index_map[curr_index] to save memory
            del index_map[arr[curr_index]]

    return -1


if __name__ == "__main__":
    arr = [7, 6, 9, 6, 9, 6, 9, 7]
    print (minJumps(arr))

    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    print(minJumps(arr))

