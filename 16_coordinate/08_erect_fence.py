# https://leetcode.com/problems/erect-the-fence/
# https://leetcode.com/problems/erect-the-fence/discuss/1443449/Python-15-lines-Easy-Convex-Hull-with-One-Pass
# Question : You are given an array trees where trees[i] = [xi, yi] represents the location
# of a tree in the garden. You are asked to fence the entire garden using the minimum length
# of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.
# Return the coordinates of trees that are exactly located on the fence perimeter.
#
# Example : Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
#
# Question Type : OddOne
# Used : Find origin from the given array.
#        From that origin, sort the array based on arc angle from origin
#        Run clockwise logic on array while pushing and popping from the stack.
#        return stack as answer
# Complexity : O(n log n)

import math


def clockwise(a, b, c):
    return (c[1] - b[1]) * (b[0] - a[0]) < (c[0] - b[0]) * (b[1] - a[1])


def outerTrees(trees):
    origin = [float('inf'), float('inf')]

    for x, y in trees:
        if x < origin[0] or (x == origin[0] and y < origin[1]):
            origin = [x, y]

    trees.sort(key=lambda p: (math.atan2(p[1] - origin[1], p[0] - origin[0]), -p[1], p[0]))
    stack = [origin]
    for x, y in trees:
        if [x, y] != origin:
            while len(stack) > 1 and clockwise(stack[-2], stack[-1], [x, y]):
                node = stack.pop()
            stack.append((x, y))

    return stack


if __name__ == "__main__":
    points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    print (outerTrees(points))

