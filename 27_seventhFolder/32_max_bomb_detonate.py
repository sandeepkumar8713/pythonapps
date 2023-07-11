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
# Used : Parent and union
#        Find out distances b/w all edges, call union on the one whose dist <= radius
#        Run a loop to find grandparent.
#        Using freq dict find out which disjoint set has max size. That is the answer.
# Logic: for i, [x1, y1, r1] in enumerate(bombs):
#           for j, [x2, y2, r2] in enumerate(bombs[i + 1:], i + 1):
#               dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#               if r1 >= dist: union(i, j, ids)
#               if r2 >= dist: union(j, i, ids)
#        for i in range(len(ids)):
#           find(i, ids)
#        ans = size of max disjoint set(in ids).
# Complexity : O(e log v) where e is the number of edges in the graph and v is the number of vertices.

import math


def union(i, j, ids):
    ids[find(i, ids)] = find(j, ids)


def find(i, ids):
    while i != ids[i]:
        ids[i] = ids[ids[i]]
        i = ids[i]
    return i


def maximumDetonation(bombs):
    ids = []
    for i in range(len(bombs)):
        ids.append(i)

    for i, [x1, y1, r1] in enumerate(bombs):
        for j, [x2, y2, r2] in enumerate(bombs[i + 1:], i + 1):
            dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
            if r1 >= dist:
                union(i, j, ids)
            if r2 >= dist:
                union(j, i, ids)

    for i in range(len(ids)):
        find(i, ids)
    disjoint_count_dict = {}
    for i in ids:
        if i in disjoint_count_dict:
            disjoint_count_dict[i] += 1
        else:
            disjoint_count_dict[i] = 1
    ans = -1
    for _, count in disjoint_count_dict.items():
        ans = max(ans, count)

    return ans


if __name__ == "__main__":
    bombs = [[2, 1, 3], [6, 1, 4]]
    print(maximumDetonation(bombs))

    bombs = [[1, 1, 5], [10, 10, 5]]
    print(maximumDetonation(bombs))

    bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    print(maximumDetonation(bombs))
