# CTCI : Q4_05_Validate_BST
# http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# Question : A program to check if a binary tree is BST or not.
#
# A binary search tree (BST) is a node based binary tree data structure which has the following properties.
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# From the above properties it naturally follows that:
# Each node (item in the tree) has a distinct key.
#
# Used :  The trick is to write a utility helper function isBSTUtil(struct node* node, int min, int max) that traverses
#         down the tree keeping track of the narrowing min and max allowed values as it goes, looking at each node only
#         once. The initial values for min and max should be INT_MIN and INT_MAX. Note that empty tree is a BST.
# Complexity : O(n)

import sys

INT_MAX = sys.maxint
INT_MIN = -sys.maxint


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


def isBSTUtil(node, mini, maxi):
    # Note that empty tree is a BST
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if isBST(root):
        print "Is BST"
    else:
        print "Not a BST"
