# https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
# Question : Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
# For example, boundary traversal of the following tree is "20 8 4 10 14 25 22"
#
#               20
#            /     \
#           8       22
#          /  \    /  \
#        4    12       25
#            /   \
#           10   14
#
# Question Type : ShouldSee
# Used : We break the problem in 3 parts:
#        1. Print the left boundary in top-down manner.
#        2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
#               2.1 Print all leaf nodes of left sub-tree from left to right.
#               2.2 Print all leaf nodes of right subtree from left to right.
#        3. Print the right boundary in bottom-up manner.
#        printBoundaryLeft :
#        Print the nodes in TOP DOWN manner. So first print and then traverse.
#        If root is present: if root.left is present : print root.data and printBoundaryLeft(root.left).
#        Else is left is None and right is present: print root.data and printBoundaryLeft(root.right).
#        printBoundaryRight :
#        Print the nodes in BOTTOM UP manner. So first traverse then print.
#        If root is present: if root.right is present: printBoundaryRight(root.right) and print root.data
#        Else is right is None and left is present: printBoundaryRight(root.left) and  print root.data
#        printLeaves :
#        We to in order traversal here. It is a recursive function
#        If root is present: Call printLeaves(root.left).
#        If both left and right subtree is None print root.data.
#        Call printLeaves(root.right)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeaves(root):
    if root:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data,end=" ")
        printLeaves(root.right)


# Print the nodes in TOP DOWN manner. So first print and then traverse.
def printBoundaryLeft(root):
    if root:
        if root.left:
            print(root.data,end=" ")
            printBoundaryLeft(root.left)

        elif root.right:
            print(root.data,end=" ")
            printBoundaryLeft(root.right)


# Print the nodes in BOTTOM UP manner. So first traverse then print.
def printBoundaryRight(root):
    if root:
        if root.right:
            printBoundaryRight(root.right)
            print(root.data,end=" ")

        elif root.left:
            printBoundaryRight(root.left)
            print(root.data,end=" ")


# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if root:
        print(root.data, end=" ")

        # Print the left boundary in top-down manner
        printBoundaryLeft(root.left)

        # Print all leaf nodes
        printLeaves(root.left)
        printLeaves(root.right)

        # Print the right boundary in bottom-up manner
        printBoundaryRight(root.right)


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    printBoundary(root)
