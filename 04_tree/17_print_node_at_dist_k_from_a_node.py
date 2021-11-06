# https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
# Question : Given a binary tree, a target node in the binary tree, and an integer value k,
# print all the nodes that are at distance k from the given target node.
# No parent pointers are available.
#
# Input : Target is node 12, k = 2
#             20
#            /   \
#          8     22
#        /  \
#      4     12
#          /   \
#         10    14
# Output : 4, 20
#
# Question Type : ShouldSee
# Used : Here we have to print values below and above at distance k from given target.
#        Make a function printKDistant(root, k) which print node data at distance k form node k.
#        Call a recursive function printKDistanceNode(root, target, k).
#        Return of printKDistanceNode is distance between root and target.
#        printKDistanceNode(root, target, k):
#        if root is None: return -1
#        if root == target:
#           printKDistant(root, k), return 0
#        dl = printKDistanceNode(root.left, target, k)
#        if dl != -1:
#           if dl + 1 == k: print(root.data)
#           else:
#               printKDistant(root.right, k - dl - 2)
#           return 1 + dl
#        dr = printKDistanceNode(root.right, target, k)
#        if dr != -1:
#           if dr + 1 == k: print(root.data)
#           else:
#               printKDistant(root.left, k - dr - 2)
#           return 1 + dr
#        return -1
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printKDistant(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print(root.data)
        return

    printKDistant(root.left, k - 1)
    printKDistant(root.right, k - 1)


def printKDistanceNode(root, target, k):
    if root is None:
        return -1

    if root == target:
        printKDistant(root, k)
        return 0

    dl = printKDistanceNode(root.left, target, k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data)
        else:
            printKDistant(root.right, k - dl - 2)
        return 1 + dl

    dr = printKDistanceNode(root.right, target, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data)
        else:
            printKDistant(root.left, k - dr - 2)
        return 1 + dr

    # If target was neither present in left nor in right subtree
    return -1


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = root.left.right

    printKDistanceNode(root, target, 2)
