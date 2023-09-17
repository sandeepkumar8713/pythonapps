# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Question : Given a binary tree root, a node X in the tree is named good if in the path from root to X
# there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.
#
# Example :
#        3
#     /     \
#    1      4
#   /      /  \
#  3      1    5
# Output : 4 (3, 3, 4, 5 are good nodes)
# TODO : add used

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def good_nodes(root) -> int:
    res = [0]

    # Pre order traversal
    def helper(root, maxi):
        if root:
            maxi = max(maxi, root.data)
            if maxi <= root.data:
                res[0] += 1
            if root.left:
                helper(root.left, maxi)
            if root.right:
                helper(root.right, maxi)

    helper(root, -sys.maxsize)
    return res[0]


if __name__ == "__main__":
    inp_arr = [3, 1, 4, 3, None, 1, 5]
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.left = Node(3)
    root.right.left = Node(1)
    root.right.right = Node(5)

    print(good_nodes(root))

    inp_arr = [3, 3, None, 4, 2]
    root = Node(3)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)

    print(good_nodes(root))
