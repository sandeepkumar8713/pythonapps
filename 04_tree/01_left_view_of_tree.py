# Question : Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of
# nodes visible when tree is visited from left side.
#
#                       12
#                     /    \
#                   10     20
#                       /    \
#                      25      40
#
# Question Type : Asked
# Used : We can keep track of level of a node by passing a parameter to all recursive calls.
#        The idea is to keep track of maximum level also. Whenever we see a node whose level
#        is more than maximum level so far, we print the node because this is the first node
#        in its level. (Preorder)
#        For right view : Do pre order but first call right subtree and then left subtree.
# Logic: leftViewUtil(root, level, max_level):
#        if root is None: return
#        if max_level[0] < level:
#           print(root.data,end=" ")
#           max_level[0] = level
#        leftViewUtil(root.left, level + 1, max_level)
#        leftViewUtil(root.right, level + 1, max_level)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftViewUtil(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data,end=" ")
        max_level[0] = level

    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)
    # leftViewUtil(root.left, level + 1, max_level)
    # Do pre order but first call right and then left for right view


def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)


if __name__ == "__main__":
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)

    leftView(root)
