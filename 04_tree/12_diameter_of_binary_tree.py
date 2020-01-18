# Question : The diameter of a tree (sometimes called the width) is the number of nodes on the longest path
# between two end nodes. Constructed binary tree is
#
# Given a binary tree, return the farthermost nodes.
# Use the above algorithm, return pointer to leaf along with value
#
#             1
#           /   \
#         2      3
#       /  \
#     4     5
# Used : Call diameterOpt() which returns both max diameter and max height, recursively over left and right child.
#        If root is None return height as 0 and diameter as 0, else call isBalanced() on left and right child
#        get max height by either : left height + 1 or right height + 1
#        get max diameter by either : left height + right height + 1 or left diameter or right diameter
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOpt(root,height):
    lh = [0]
    rh = [0]

    if root is None:
        height[0] = 0
        return 0

    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
    height[0] = max(lh[0], rh[0]) + 1

    return max(lh[0] + rh[0] + 1, max(ldiameter, rdiameter))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print "Diameter of given binary tree is %d" % (diameterOpt(root,[0]))
