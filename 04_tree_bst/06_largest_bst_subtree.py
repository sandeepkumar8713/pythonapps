# https://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
# https://leetcode.com/problems/largest-bst-subtree/
# Question : Given a Binary Tree, write a function that returns the size of the largest subtree
# which is also a Binary Search Tree (BST). If the complete Binary Tree is BST, then
# return the size of whole tree.
#
# Input:
#       5
#     /  \
#    2    4
#  /  \
# 1    3
#
# Output: 3
# The following subtree is the maximum size BST subtree
#    2
#  /  \
# 1    3
#
# Question Type : ShouldSee
# Used : If we traverse the tree in bottom up manner, then we can pass information about
#        subtrees to the parent. The passed information can be used by the parent to do
#        BST test (for parent node) only in constant time (or O(1) time).
#        A left subtree need to tell the parent whether it is BST or not and also need to
#        pass maximum value in it. So that we can compare the maximum value with the parent's
#        data to check the BST property.
#        Similarly, the right subtree need to pass the minimum value up the tree.
#        Make a call to recursive function
#        largestBSTUtil(node, minKey, maxKey, maxSize, isBst) with input :
#        largestBSTUtil(root, [sys.maxint], [-sys.maxint], maxSize, [False])
#        and return maxSize[0].
#        It returns the size of tree if it is BST else 0.
# Logic: def largestBSTUtil():
#        If root is null. set isBst[0] = True and return 0.
#        set maxKey[0] = -sys.maxint and call largestBSTUtil() on left subtree
#        if left subtree is bst and current node value is more than maxKey[0]:
#        set leftIsBst = True, save leftMin = minKey[0]
#        set minKey[0] = sys.maxint and call largestBSTUtil() on right subtree
#        if right subtree is bst and current node value is less than minKey[0]:
#        set rightIsBst = True
#        if leftMin < minKey[0]: minKey[0] = leftMin
#        (As min and max from left and right, need to send up)
#        if node.data < minKey[0]: minKey[0] = node.data
#        (We get min and max from leaf node only)
#        if node.data > maxKey[0]: maxKey[0] = node.data
#        If both left and right are bst:
#           if sum of (left + right + 1) is more than maxSize update maxSize
#               return sum
#        Else: isBst[0] = False and return 0
# Complexity : O(n)

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# It returns size of the tree
def largestBSTUtil(node, minKey, maxKey, maxSize, isBst):
    if node is None:
        isBst[0] = True
        return 0

    leftIsBst = False
    rightIsBst = False

    maxKey[0] = -sys.maxsize
    leftSize = largestBSTUtil(node.left, minKey, maxKey, maxSize, isBst)
    if isBst and node.data > maxKey[0]:
        leftIsBst = True

    leftMin = minKey[0]

    minKey[0] = sys.maxsize
    rightSize = largestBSTUtil(node.right, minKey, maxKey, maxSize, isBst)
    if isBst and node.data < minKey[0]:
        rightIsBst = True

    if leftMin < minKey[0]:
        minKey[0] = leftMin

    # Minimum and Maximum key will be at the leaf node of the BST
    if node.data < minKey[0]:
        minKey[0] = node.data
    if node.data > maxKey[0]:
        maxKey[0] = node.data

    if leftIsBst and rightIsBst:
        if leftSize + rightSize + 1 > maxSize[0]:
            maxSize[0] = leftSize + rightSize + 1
        return leftSize + rightSize + 1
    else:
        isBst[0] = False
        return 0


def largestBST(root):
    maxSize = [0]
    largestBSTUtil(root, [sys.maxsize], [-sys.maxsize], maxSize, [False])
    return maxSize[0]


if __name__ == "__main__":
    #           50
    #        /      \
    #      10        60
    #     /  \       /  \
    #    5   20    55    70
    #             /     /  \
    #           45     65    80

    root = Node(50)
    root.left = Node(10)
    root.right = Node(60)
    root.left.left = Node(5)
    root.left.right = Node(20)
    root.right.left = Node(55)
    root.right.left.left = Node(45)
    root.right.right = Node(70)
    root.right.right.left = Node(65)
    root.right.right.right = Node(80)

    print(largestBST(root))
