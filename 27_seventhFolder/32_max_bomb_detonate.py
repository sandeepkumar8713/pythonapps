# https://leetcode.com/problems/detonate-the-maximum-bombs/
# Question : You are given a list of bombs. The range of a bomb is defined as the area where its
# effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas
# ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that
# lie in its range. These bombs will further detonate the bombs that lie in their ranges.
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are
# allowed to detonate only one bomb.
#
# Example : Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
#
# Used : Find out distances b/w all edges, add edge on the one whose dist <= radius.
#        Run DFS by taking each node as start node and find max_node visited.
# Logic: graph = defaultdict(set)
#        for i, [x1, y1, r1] in enumerate(bombs):
#           for j, [x2, y2, r2] in enumerate(bombs[i + 1:], i + 1):
#               dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#               if r1 >= dist:
#                   graph[i].add(j)
#               if r2 >= dist:
#                   graph[j].add(i)
#
#        for i in range(len(bombs)):
#           visited_count = dfs(i, {i})
#           res = max(res, visited_count)
#        return res
# Complexity : O(v^2) where v is the number of vertices.

import math
import sys
from collections import defaultdict


def maximumDetonation(bombs):
    def dfs(node, visited):

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                dfs(child, visited)

        return len(visited)

    graph = defaultdict(set)
    for i, [x1, y1, r1] in enumerate(bombs):
        for j, [x2, y2, r2] in enumerate(bombs[i + 1:], i + 1):
            dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
            if r1 >= dist:
                graph[i].add(j)
            if r2 >= dist:
                graph[j].add(i)

    res = -sys.maxsize
    for i in range(len(bombs)):
        visited_count = dfs(i, {i})
        res = max(res, visited_count)

    return res


if __name__ == "__main__":
    bombs = [[2, 1, 3], [6, 1, 4]]
    print(maximumDetonation(bombs))

    bombs = [[1, 1, 5], [10, 10, 5]]
    print(maximumDetonation(bombs))

    bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    print(maximumDetonation(bombs))

    bombs = [[0, 0, 4], [2, 0, 1], [10, 0, 8], [-4, 0, 1]]
    print(maximumDetonation(bombs))
