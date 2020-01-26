# CTCI : Q4_06_Successor
# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
# Question : In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree.
# Inorder Successor is NULL for the last node in Inoorder traversal.
#
#               20
#            /      \
#          8        22
#        /   \
#      4     12
#           /  \
#         10   14
#
# Question Type : Generic
# Used : 1) If right subtree of node is not NULL, then nextNode lies in right subtree. Do following.
#           Go to right subtree and return the node with minimum key value in right subtree. (By looping until
#           node.left is not null and then return node)
#       2) If right subtree of node is None, the loop while root is not None:
#              if node.data < root.data: nextNode = root, root = root.left
#              elif node.data > root.data: root = root.right
#              else: break (node is matching)
#           return nextNode
# Complexity : O(h) h is height of tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insertUtils(self, root, data):
        if root is None:
            newNode = Node(data)
            return newNode

        if data < root.data:
            root.left = self.insertUtils(root.left, data)
        else:
            root.right = self.insertUtils(root.right, data)

        return root

    def insert(self, data):
        self.root = self.insertUtils(self.root, data)

    def printInOrderUtil(self, root):
        if root is None:
            return
        self.printInOrderUtil(root.left)
        print(root.data,end=" ")
        self.printInOrderUtil(root.right)

    def printInOrder(self):
        self.printInOrderUtil(self.root)

    def findNext(self, node):
        return findNextUtil(self.root, node)


def findMin(node):
    while node.left is not None:
        node = node.left
    return node


def findNextUtil(root, node):
    if root is None or node is None:
        return None

    if node.right is not None:
        return findMin(node.right)

    nextNode = None

    while root is not None:
        if node.data < root.data:
            # We have to keep track of prev node while going in left subtree as, during inorder next node is be root
            nextNode = root
            root = root.left
        elif node.data > root.data:
            root = root.right
        else:
            # node is matching
            break

    return nextNode


if __name__ == "__main__":
    bst = BST()
    bst.insert(20)
    bst.insert(8)
    bst.insert(22)
    bst.insert(4)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)

    bst.printInOrder()

    temp = bst.root.left.right.right
    print("")
    print("node:", temp.data)
    nextNode = bst.findNext(temp)
    if nextNode is not None:
        print("nextNode:", nextNode.data)
