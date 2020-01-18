# http://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/
# Question : Write a function to print spiral order traversal of a tree. For below tree, function should print
# 1, 2, 3, 4, 5, 6, 7.
#            1
#         /    \
#        2      3
#       / \   /   \
#      7   6  5   4
#
# Used : Compute height of tree. Assign a bool marker called ltr. Now loop over height of tree.
#        At each level, invert the ltr i.e. true to false or false to true.
#        If ltr is true call left then right child else call right then left child.
#        Other method :
#        We can print spiral order traversal in O(n) time and O(n) extra space. The idea is to use two stacks. We can
#        use one stack for printing from left to right and other stack for printing from right to left. In every
#        iteration, we have nodes of one level in one of the stacks. We print the nodes, and push nodes of next level
#        in other stack.
# Complexity : O(n^2)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    lHeight = height(node.left)
    rHeight = height(node.right)

    if lHeight > rHeight:
        return lHeight + 1
    else:
        return rHeight + 1


def printGivenLevel(root, level, ltr):
    if root is None:
        return

    if level is 1:
        print root.data,
    else:
        if ltr:
            printGivenLevel(root.left, level-1, ltr)
            printGivenLevel(root.right, level-1, ltr)
        else:
            printGivenLevel(root.right, level-1, ltr)
            printGivenLevel(root.left, level-1, ltr)


def printSpiral(root):
  ltr = True
  for i in range(0, height(root)+1):
     printGivenLevel(root, i, ltr)
     ltr = not ltr


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print "Spiral Order traversal of binary tree is \n"
    printSpiral(root)
