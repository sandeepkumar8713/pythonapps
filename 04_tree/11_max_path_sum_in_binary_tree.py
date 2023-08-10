# http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Question : Given a binary tree, find the maximum path sum. The path may start and end at any
# node in the tree.
#
#           10
#        /     \
#       2       10
#      / \       \
#     20  1       -25
#                 / \
#                3  4
# 20 + 2 + 10 + 10 = 42
#
# Question Type : Generic
# Used : Call findMaxUtil() on root recursively for left and right. Store value of left
#        and right max.
#        Find max single from either : l + root.data or r + root.data or root.data
#        Find max top from either : max single or l + r + root.data
#        find max ultimate from either : max top or max ultimate
#        return max top
# Logic: findMaxUtil(root):
#        if root is None: return 0
#        l = findMaxUtil(root.left)
#        r = findMaxUtil(root.right)
#        max_single = max(max(l, r) + root.data, root.data)
#        max_top = max(max_single, l + r + root.data)
#        findMaxUtil.res = max(findMaxUtil.res, max_top)
#        return max_single
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMaxUtil(root):
    if root is None:
        return 0

    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    max_single = max(max(l, r) + root.data, root.data)
    max_top = max(max_single, l + r + root.data)
    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single


def findMaxSum(root):
    findMaxUtil.res = float("-inf")

    findMaxUtil(root)
    return findMaxUtil.res


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print("Max path sum is", findMaxSum(root))
