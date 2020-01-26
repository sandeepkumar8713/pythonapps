# https://www.geeksforgeeks.org/find-next-right-node-given-key-set-2/
# Question : Given a Binary tree and a key in the binary tree, find the node right to the given key. If there is
#  no node on right side, then return NULL. Expected time complexity is O(n) where n is the number of nodes in the
#  given binary tree.
#
# For example, consider the following Binary Tree. Output for 2 is 6, output for 4 is 5. Output for 10, 6 and 5 is NULL.
#
#                   10
#                /      \
#              2         6
#            /   \         \
#          8      4          5
# Input : 2
# Output : 6
#
# Question Type : Easy
# Used : Do pre order traversal of the given tree. While doing to find the given key, save its level. Next time when you
#        reach the same, this node is our answer.
#        Logic : def nextRightNode(root, k, level, valueLevel):
#        if root is None: return None
#        if root.key == k: valueLevel[0] = level, return None
#        elif valueLevel[0]:
#           if level == valueLevel[0]:
#               return root
#        leftNode = nextRightNode(root.left, k, level + 1, valueLevel)
#        if leftNode: return leftNode
#        return nextRightNode(root.right, k, level + 1, valueLevel)
# Complexity : O(n)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def nextRightNode(root, k, level, valueLevel):
    if root is None:
        return None

    if root.key == k:
        valueLevel[0] = level
        return None

    # if value_level is already set, then current node is the next right node
    elif valueLevel[0]:
        if level == valueLevel[0]:
            return root

    # recurse for left subtree
    leftNode = nextRightNode(root.left, k, level + 1, valueLevel)

    # if node is found in left subtree, return it
    if leftNode:
        return leftNode

    # recurse for right subtree
    return nextRightNode(root.right, k, level + 1, valueLevel)


def nextRightNodeUtil(root, k):
    valueLevel = [0]
    return nextRightNode(root, k, 1, valueLevel)


def test(root, k):
    nextRight = nextRightNodeUtil(root, k)
    if nextRight is not None:
        print("Next Right of", k, "is", nextRight.key)
    else:
        print("No next right node found for", k)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(6)
    root.right.right = Node(5)
    root.left.left = Node(8)
    root.left.right = Node(4)

    test(root, 10)
    test(root, 2)
    test(root, 6)
    test(root, 5)
    test(root, 8)
    test(root, 4)
