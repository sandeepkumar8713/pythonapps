# https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/
# Question : Given a binary tree, print all root-to-leaf paths.
#
# Question Type : Easy
# Used : Do pre-order traversal of binary tree and keep pushing elements in the stack.
#        When leaf node is found print the stack.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPaths(root,path):
    if root is not None:
        path.append(root.data)
    else:
        return

    if root.left is None and root.right is None:
        print(path)

    printPaths(root.left, path)
    printPaths(root.right, path)
    path.pop()


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    path = []
    printPaths(root, path)
