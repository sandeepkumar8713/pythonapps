# https://www.geeksforgeeks.org/print-nodes-binary-tree-k-leaves/
# Question : Given a binary tree and a integer value K, the task is to find all nodes in given binary tree having K leaves in
# subtree rooted with them.
#
#              1
#            /   \
#           2     4
#          /  \  /  \
#        5    6  7   8
#       / \     /  \
#      9  10   11  12
#
# Used : Here any node having K leaves means sum of leaves in left subtree and in right subtree must be equal to K.
#        So to solve this problem we use post order traversal of tree. First we calculate leaves in left subtree then
#        in right subtree and if sum is equal to K, then print current node. In each recursive call we return sum of
#        leaves of left subtree and right subtree to it's ancestor.
#        Make a call to recursive func kLeaves(root, k). If root is None: return 0
#           Calculate leaves in left and right subtree. total = kLeaves(root.left, k) + kLeaves(root.right, k)
#           If both left and right subtree are none return 1.
#           If total == k: print root.data
#           return total
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# post order traversal
def kLeaves(root, k):
    if root is None:
        return 0

    total = kLeaves(root.left, k) + kLeaves(root.right, k)

    if root.left is None and root.right is None:
        return 1

    if total == k:
        print root.data,

    return total


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.left.left.left = Node(9)
    root.left.left.right = Node(10)
    root.right.right = Node(8)
    root.right.left = Node(7)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)

    print "Nodes with 2 leaves:"
    kLeaves(root, 2)
    print "\nNodes with 3 leaves:"
    kLeaves(root, 3)
