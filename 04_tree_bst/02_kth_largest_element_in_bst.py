# https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
# Question : Given a Binary Search Tree (BST) and a positive integer k, find the k'th largest element in
# the Binary Search Tree.
#
#               50
#            /     \
#           30      70
#          /  \    /  \
#        20   40  60   80
#
# Used : The idea is to do reverse inorder traversal of BST. The reverse inorder traversal traverses all nodes in
#        decreasing order.
#        Call a recursive function largestKthNodeUtil(root, k) where k is passed by pointer (list[0])
#           If root is None: return
#           Call largestKthNodeUtil() over root.right
#           Now it has reached its largest element. decrement k by 1
#           If k == 0 then print root.data and return
#           Call largestKthNodeUtil() over root.left
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

    def largestKthNodeUtil(self, root, k):
        if root is None:
            return

        self.largestKthNodeUtil(root.right, k)
        k[0] -= 1

        if k[0] == 0:
            print root.data
            return

        self.largestKthNodeUtil(root.left, k)

    # reverse inorder traversal
    def largestKthNode(self, k):
        self.largestKthNodeUtil(self.root, [k])


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    for k in range(1, 8):
        bst.largestKthNode(k)
