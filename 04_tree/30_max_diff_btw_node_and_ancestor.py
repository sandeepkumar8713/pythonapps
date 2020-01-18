# https://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/
# Question : Given a binary tree, we need to find maximum value we can get by subtracting value of node B from value
# of node A, where A and B are two nodes of the binary tree and A is an ancestor of B. Expected time complexity is O(n).
#
# Used : Call a recursive function maxDiffUtils(root, res) with input res = [-sys.maxint]
#        if root is None: return return sys.maxint
#        If we are at leaf node then just return its value because it can't be ancestor of any node. Then at each
#        internal node we will try to get minimum value from left subtree and right subtree and calculate the
#        difference between node value and this minimum value and according to that we will update the result.
#        Atlast return the min value from this node: return min(minVal, root.data)
# Complexity : O(n)

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDiffUtils(root, res):
    if root is None:
        return sys.maxint

    if root.left is None and root.right is None:
        return root.data

    minVal = min(maxDiffUtils(root.left, res), maxDiffUtils(root.right, res))
    res[0] = max(res[0], root.data - minVal)

    return min(minVal, root.data)


def maxDiff(root):
    res = [-sys.maxint]
    maxDiffUtils(root, res)
    return res[0]


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    print maxDiff(root)
