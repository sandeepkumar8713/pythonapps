# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Question : Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# An n-Ary tree was given with their level of stickiness on the edges.If the water is falling from the root, find
# the max time taken to wet the whole tree.
#
# Used : Call a recursive function which return node, count in each of its children. Return maxCount + 1.
#        Logic : def dfs(root):
#        res = 0
#        if root is None: return res
#        else:
#        for child in root.children:
#           res = max(res, dfs(child))
#        return res + 1
# Complexity : O(n)

N = 3


class Node:
    def __init__(self, val):
        self.val = val
        self.children = [None] * N


def dfs(root):
    res = 0
    if root is None:
        return res
    else:
        for child in root.children:
            res = max(res, dfs(child))
        return res + 1


if __name__ == "__main__":
    root = Node(1)
    root.children[0] = Node(3)
    root.children[1] = Node(2)
    root.children[2] = Node(4)
    root.children[0].children[0] = Node(5)
    root.children[0].children[1] = Node(6)

    print dfs(root)
