# CTCI : Q4_02_Minimal_Tree
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
# Question : Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.
#
# Input: Array {1, 2, 3, 4}
# Output: A Balanced BST
#       3
#     /  \
#    2    4
#  /
# 1
#
# Question Type : ShouldSee
# Used : For the given sorted input array call a recursive function sortedArrayToBst(inpArr, left, right) with input
#        sortedArrayToBst(inpArr,0,n-1). It is used to do preorder and make BST tree.
#        if left > right: return None
#        find mid of left and right and make a node for that element
#        Now call function again for left side of array to set left subtree. Similarly for right side.
#        root.left = sortedArrayToBst(inpArr, left, mid-1)
#        root.right = sortedArrayToBst(inpArr, mid+1, right)
#        return root
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sortedArrayToBst(inpArr, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    root = Node(inpArr[mid])

    root.left = sortedArrayToBst(inpArr, left, mid-1)
    root.right = sortedArrayToBst(inpArr, mid+1, right)

    return root


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


if __name__ == "__main__":
    inpArr = [1, 2, 3, 4, 5, 6, 7]
    root = sortedArrayToBst(inpArr, 0, len(inpArr) - 1)
    printInOrder(root)
    print("")
