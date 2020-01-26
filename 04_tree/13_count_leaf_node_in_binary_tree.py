# Question : Program to count leaf nodes in a binary tree. A node is a leaf node if both left and right child nodes
# of it are NULL.
#
#             1
#           /   \
#         2      3
#       /  \
#     4     5
#
# Question Type : Easy
# Used : Def getLeafCount() and call recursively.
#        If given root is none return 0.
#        If given root has left none and right none return 0 else call getLeafCount() over left and right child and
#        return its sum.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeafCount(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Leaf count of the tree is:", getLeafCount(root))
