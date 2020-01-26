# CTCI :: Q4_10_Check_Subtree
# https://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
# Question : Given two binary trees, check if the first tree is subtree of the second one. A subtree of a tree T
# is a tree S consisting of a node in T and all of its descendants in T. The subtree corresponding to the root
# node is the entire tree; the subtree corresponding to any other node is called a proper subtree.
#
# Question Type : Generic
# Used : Make a func  areIdentical(root1, root2), It checks if the tree starting from root1 and root2 are same or not.
#        Call a recursive func isSubtree(T, S), If either T or S is None return true
#        Call areIdentical(T, S) and return True if they are same
#        Else return isSubtree(T.left, S) or isSubtree(T.right, S)  (We check by taking left and right subtree as root)
# Complexity : O(n^2)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)


def isSubtree(T, S):
    if S is None:
        return True

    if T is None:
        return True

    if areIdentical(T, S):
        return True

    return isSubtree(T.left, S) or isSubtree(T.right, S)


if __name__ == "__main__":
    """ TREE 1
         Construct the following tree
                  26
                /   \
              10     3
            /    \     \
          4      6      3
           \
            30
        """

    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    """ TREE 2
         Construct the following tree
              10
            /    \
          4      6
           \
            30
        """
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if isSubtree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")
