# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
# Question : Consider lines of slope -1 passing between nodes. Given a Binary Tree,
# print all diagonal elements in a binary tree belonging to same line
#
#                        8
#                     /    \
#                   3     10
#                 /     /    \
#                1     6     14
#                       \    /
#                        7  13
#
# Question Type : ShouldSee
# Used : Maintain a hashDict diagonalPrintMap here key is vertical dist from root and value is
#        list of nodes at that distance. Call a recursive function which does preOrder
#        diagonalPrintUtil(root, d, diagonalPrintMap) with input diagonalPrintUtil(root, 0, {}).
#        Insert this node in map : diagonalPrintMap[d].append(root.data)
#        Call function again on left subtree with d+1
#        Call function again on right subtree with d.
#        (Note that nodes at same vertical distance goes into same key in map)
#        Once the recursion is over, print arrays of diagonalPrintMap one by one based on
#        keys starting with 0.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# preOrder
def diagonalPrintUtil(root, d, diagonalPrintMap):
    if root is None:
        return
    # Store all nodes of same line together as a vector
    try:
        diagonalPrintMap[d].append(root.data)
    except KeyError:
        diagonalPrintMap[d] = [root.data]

    # Increase the vertical distance if left child
    diagonalPrintUtil(root.left, d + 1, diagonalPrintMap)
    # Vertical distance remains same for right child
    diagonalPrintUtil(root.right, d, diagonalPrintMap)


def diagonalPrint(root):
    diagonalPrintMap = dict()
    diagonalPrintUtil(root, 0, diagonalPrintMap)

    for d, nodes in diagonalPrintMap.items():
        print(nodes)


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    diagonalPrint(root)
