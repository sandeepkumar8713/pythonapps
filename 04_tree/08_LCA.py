# CTCI : Q4_08_First_Common_Ancestor
# Question : Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find
# the least common ancestor.
#
#            1
#         /    \
#        2      3
#       / \   /   \
#      4   5  6   7
#
# Question Type : Asked
# Used : Do a recursive call over findLCA(root,n1,n2). In each call search for n1 or n2. If either is found return that
#        node. If none is found, then call findLCA over left and right child. Either of them won't be empty, return
#        that. Since LCA might be present in either left or right child.
#        Logic : def findLCA(root, n1, n2):
#        if root is None: return None
#        if root.data == n1 or root.data == n2:
#           return root
#        left_lca = findLCA(root.left, n1, n2)
#        right_lca = findLCA(root.right, n1, n2)
#        if left_lca and right_lca:
#           return root
#        if left_lca is not None:
#           return left_lca
#        else:
#           return right_lca
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lca = findLCA(root, 4, 5)
    print(4, 5, '->', lca.data)
    lca = findLCA(root, 4, 6)
    print(4, 6, '->', lca.data)
    lca = findLCA(root, 3, 4)
    print(3, 4, '->', lca.data)
    lca = findLCA(root, 2, 4)
    print(2, 4, '->', lca.data)
