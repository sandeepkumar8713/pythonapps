# https://www.geeksforgeeks.org/convert-a-given-tree-to-sum-tree/
# Question : Given a Binary Tree where each node has positive and negative values.
# Convert this to a tree where each node contains the sum of the left and right sub
# trees in the original tree. The values of leaf nodes are changed to 0.
#
# Input :
#                   10
#                /     \
#              -2       6
#            /   \    /  \
#           8    -4  7    5
#
# Output :
#                20(4-2+12+6)
#                /      \
#            4(8-4)     12(7+5)
#            /   \      /  \
#           0     0    0    0
#
# Question Type : Generic
# Used : Call recursive function toSumTree(root). If root is None: return 0
#        save current value in oldVal =  root.data
#        Call toSumTree() on left and right and set its sum to current value.
#           root.data = toSumTree(root.left) + toSumTree(root.right)
#        return oldValue + root.data (Sum of left, right subtree and oldValue)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def toSumTree(root):
    if root is None:
        return 0

    oldValue = root.data
    root.data = toSumTree(root.left) + toSumTree(root.right)
    return oldValue + root.data


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    toSumTree(root)
    printInOrder(root)
