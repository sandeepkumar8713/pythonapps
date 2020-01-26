# Question : Given a binary tree, check whether it is a mirror of itself.
# For example, this binary tree is symmetric:
#          1
#        /   \
#       2     2
#      / \   / \
#     3   4 4   3
#
# But the following is not:
#         1
#        / \
#       2   2
#        \   \
#        3    3
#
# Question Type : ShouldSee
# Used : We should call isMirror() recursively over the two roots and check following condition :
#        For two trees to be mirror images, the following three conditions must be true
#       1. Their root node's key must be same
#       2. left subtree of left tree and right subtree of right tree have to be mirror images
#       3. right subtree of left tree and left subtree of right tree have to be mirror images
# Complexity : O(n)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.key == root2.key:
            return (isMirror(root1.left, root2.right) and
                    isMirror(root1.right, root2.left))

    return False


def isSymmetric(root):
    return isMirror(root, root)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    print(isSymmetric(root))
