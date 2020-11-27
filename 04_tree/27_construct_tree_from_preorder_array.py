# https://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
# Question : Given an array 'pre[]' that represents Preorder traversal of a spacial binary tree where every node
# has either 0 or 2 children. One more array 'preLN[]' is given which has only two possible values 'L' and 'N'.
# The value 'L' in 'preLN[]' indicates that the corresponding node in Binary Tree is a leaf node and value 'N'
# indicates that the corresponding node is non-leaf node. Write a function to construct the tree from the given
# two arrays.
#
# Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
# Output: Root of following tree
#           10
#          /  \
#         30   15
#        /  \
#       20   5
#
# Question Type : ShouldSee
# Used : Call a recursive function constructTreeUtils((pre, preLN, index, n). If index == n, return None.
#        Make a newNode for value per[index] and increment index. If this value is non-leaf call
#        the function again on left and right subtree and update accordingly. Now return this newNode.
#
#        The first element in pre[] will always be root. So we can easily figure out root. If left subtree is empty,
#        the right subtree must also be empty and preLN[] entry for root must be 'L'. We can simply create a node and
#        return it. If left and right subtrees are not empty, then recursively call for left and right subtrees and
#        link the returned nodes to root.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructTreeUtils(pre, preLN, index, n):
    indexValue = index[0]
    if indexValue == n:
        return None

    newNode = Node(pre[indexValue])
    index[0] += 1

    if preLN[indexValue] == 'N':
        newNode.left = constructTreeUtils(pre, preLN, index, n)
        newNode.right = constructTreeUtils(pre, preLN, index, n)

    return newNode


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


def constructTree(pre,preLN):
    root = constructTreeUtils(pre, preLN, [0], len(pre))
    return root


if __name__ == "__main__":
    pre = [10, 30, 20, 5, 15]
    preLN = ['N', 'N', 'L', 'L', 'L']
    root = constructTree(pre, preLN)
    printInOrder(root)
