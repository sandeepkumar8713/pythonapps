# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# Question : Delete the node, for the given key from Binary Search Tree.
#
#               50
#            /     \
#           30      70
#          /  \    /  \
#        20   40  60   80
#
# Used : Call a recursive function deleteNode(root, key): If root is None : return None
#        if key < root.data: call function over left subtree : root.left = deleteNode(root.left, key)
#        Else if key > root.data: call function over right subtree
#        Else this we have to delete this root node. If root.left is None: return root.right
#           Else if root.right is None: return root.left
#           Else : Find the next inOrder successor, by finding minVal in right subtree. Update root.data = minVal
#                  Now delete this min Node. So call func again on right subtree
#                  root.right = deleteNode(root.right, minVal)
#        return root
# Complexity : O(log n)


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
        print root.data,
        self.printInOrderUtil(root.right)

    def printInOrder(self):
        self.printInOrderUtil(self.root)
        print


def findMin(node):
    while node.left is not None:
        node = node.left
    return node


def deleteNode(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:  # if we have to delete this node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inOrder successor
        temp = findMin(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    bst.printInOrder()
    bst.root = deleteNode(bst.root, 50)
    # bst.root = deleteNode(bst.root, 30)
    # bst.root = deleteNode(bst.root, 80)
    bst.printInOrder()
