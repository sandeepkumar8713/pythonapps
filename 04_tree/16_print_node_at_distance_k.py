# https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/
# Question : Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.
#
# For example, in the below tree, 4, 5 & 8 are at distance 2 from root.
#             1
#           /   \
#         2      3
#       /  \    /
#     4     5  8
#
# Question Type : Easy
# Used : Do inorder traversal of from the root with value k. If k is 0 print node data else do inorder on left and right
#        child with input k-1
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# in order traversal
def printKDistant(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")
    else:
        printKDistant(root.left, k - 1)
        printKDistant(root.right, k - 1)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    printKDistant(root, 2)
