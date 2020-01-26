# CTCI : Q4_04_Check_Balanced
# Question : Determine if a binary tree is height-balanced.
# An empty tree is height-balanced. A non-empty binary tree T is balanced if:
# 1) Left subtree of T is balanced
# 2) Right subtree of T is balanced
# 3) The difference between heights of left subtree and right subtree is not more than 1.
#
#                 1
#               /   \
#             2      3
#           /  \    /
#         4     5  6
#        /
#       7
#
# Question Type : ShouldSee
# Used : Call isBalanced() which returns both result and max height, recursively over left and right child.
#        If root is None return height as 0 and result true, else call isBalanced() on left and right child
#        get max height by either : left height + 1 or right height + 1
#        If difference b/w left and right height is more than or equal to 2 return result as false
#        else return and of left and right result
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalanced(root, height):
    lh = [0]
    rh = [0]

    if root is None:
        height[0] = 0
        return 1

    leftBal = isBalanced(root.left, lh)
    rightBal = isBalanced(root.right, rh)

    height[0] = max(lh[0], rh[0]) + 1

    if abs(lh[0] - rh[0]) >= 2:
        return 0
    else:
        return leftBal and rightBal


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    print(isBalanced(root, [0]))


