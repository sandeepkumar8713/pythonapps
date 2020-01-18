# CICI : Q4_11_Random_Node (Similar problem: k = (random number % size of tree) Now return kth element)
# https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
# Question : Given root of binary search tree and K as input, find K-th smallest element in BST.
#
#               50
#            /     \
#           30      70
#          /  \    /  \
#        20   40  60   80
#
# This can be solved using inorder traversal, but its complexity will be O(n). (kth largest element in bst)
# Used : Assume that the root is having N nodes in its left subtree. If K = N + 1, root is K-th node. If K < N, we will
#        continue our search (recursion) for the Kth smallest element in the left subtree of root. If K > N + 1, we
#        continue our search in the right subtree for the (K - N - 1)-th smallest element.
#        While inserting elements in the BST, also keep track of elements in the left subtree of each node.
#        Call function kthSmallestElement(k). It set res = -1. If root is None: return res.
#        Set temp = root. Now loop while temp is not None. If temp.leftCount + 1 == k: return temp.data .
#           Else if k > temp.leftCount: k = k - (temp.leftCount + 1),  temp = temp.right
#               It means that kth element is in right subtree. So go in right subtree to search (K-N-1)-th smallest ele.
#           Else temp = temp.left, search in left subtree.
#        If come out of loop return res(-1). Which means not found.
# Complexity : O(h) here h is height of binary tree so O(log n)


class Node:
    def __init__(self, data):
        self.data = data
        self.leftCount = 0
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
            root.leftCount += 1
            root.left = self.insertUtils(root.left, data)
        else:
            root.right = self.insertUtils(root.right, data)

        return root

    def insert(self, data):
        self.root = self.insertUtils(self.root, data)

    def kthSmallestElement(self, k):
        res = -1

        if self.root is None:
            return res

        temp = self.root
        while temp:
            if temp.leftCount + 1 == k:
                res = temp.data
                return res
            elif k > temp.leftCount:
                k = k - (temp.leftCount + 1)
                temp = temp.right
            else:
                temp = temp.left
        return res


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
        print (bst.kthSmallestElement(k))
