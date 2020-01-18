# https://www.geeksforgeeks.org/add-greater-values-every-node-given-bst/
# Question : Given a Binary Search Tree (BST), modify it so that all greater values in the given BST are added
# to every node.
#
# For example, consider the following BST.
#               50
#            /      \
#          30        70
#         /   \      /  \
#       20    40    60   80
#
# The above tree should be modified to following
#
#               260
#            /      \
#          330        150
#         /   \       /  \
#       350   300    210   80
#
# Used : The idea is to do reverse inorder traversal of BST. The reverse inorder traversal traverses all nodes in
#        decreasing order.
#        Call a recursive function modifyBSTUtil(root, k) where k is passed by pointer (list[0])
#           If root is None: return
#           Call modifyBSTUtil() over root.right
#           Now it has reached its largest element. Set oldVal = root.data. Add k to original data root.data += k[0]
#           Now update the k value by adding with oldVal :  k[0] += oldVal. This new value k will be sent ahead.
#           Call modifyBSTUtil() over root.left
#        Print the modified tree using inorder traversal
# Complexity : O(n)


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

    # reverse inorder traversal
    def modifyBSTUtil(self, root, k):
        if root is None:
            return

        self.modifyBSTUtil(root.right, k)
        oldVal = root.data
        root.data += k[0]
        k[0] += oldVal

        self.modifyBSTUtil(root.left, k)

    def modifyBST(self):
        self.modifyBSTUtil(self.root, [0])

    def printInOrderUtil(self, root):
        if root is None:
            return
        self.printInOrderUtil(root.left)
        print root.data
        self.printInOrderUtil(root.right)

    def printInOrder(self):
        self.printInOrderUtil(self.root)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    bst.modifyBST()
    bst.printInOrder()
