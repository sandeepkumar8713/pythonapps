# https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/
# Question : Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST.
#
# Input Tree:
#          10
#         /  \
#        5    8
#       / \
#      2   20
#
# In the above tree, nodes 20 and 8 must be swapped to fix the tree.
# Following is the output tree
#          10
#         /  \
#        5    20
#       / \
#      2   8
#
# Question Type : ShouldSee
# Used : Call a recursive function correctBSTUtil((root, first, middle, last, prev) with
#        correctBSTUtil((root, [None], [None], [None], [None]). This function should do
#        inorder as it traverses the BST in increasing order.
#        If root is None: return
#        Call the recursive function on left subtree
#        if prev is not None and current data is less than previous data:
#           (this is BST Violation)
#           If first is None: first = prev and middle = root
#           Else: last = root
#        prev = root
#        Call recursive function on right subtree
#
#        Once we are out of recursive function. If first and last are set: swap them
#        Else if first and middle are set: swap them
#
#        correctBSTUtil(root, first, middle, last, prev):
#        if root is None: return
#        correctBSTUtil(root.left, first, middle, last, prev)
#        if prev[0] is not None and root.data < prev[0].data:
#           if first[0] is None:
#               first[0] = prev[0]
#               middle[0] = root
#           else:
#               last[0] = root
#        prev[0] = root
#        correctBSTUtil(root.right, first, middle, last, prev)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInOrder(root):
    if root is None:
        return

    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


# inOrder traverses the BST in sorted way.
def correctBSTUtil(root, first, middle, last, prev):
    if root is None:
        return

    correctBSTUtil(root.left, first, middle, last, prev)

    if prev[0] is not None and root.data < prev[0].data:
        # First violation
        if first[0] is None:
            first[0] = prev[0]
            middle[0] = root
        else:
            # second violation
            last[0] = root

    prev[0] = root

    correctBSTUtil(root.right, first, middle, last, prev)


def correctBST(root):
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]
    correctBSTUtil(root, first, middle, last, prev)

    if first[0] and last[0]:
        first[0].data, last[0].data = last[0].data, first[0].data
    elif first[0] and middle[0]:
        first[0].data, middle[0].data = middle[0].data, first[0].data


if __name__ == "__main__":
    #           6
    #         /   \
    #        10    2
    #       / \   / \
    #      1   3 7  12
    #      10 and 2 are swapped

    # root = Node(6)
    # root.left = Node(10)
    # root.right = Node(2)
    # root.left.left = Node(1)
    # root.left.right = Node(3)
    # root.right.right = Node(12)
    # root.right.left = Node(7)

    root = Node(10)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(20)

    print("original:", end=" ")
    printInOrder(root)
    print("\nCorrected:", end=" ")
    correctBST(root)
    printInOrder(root)
