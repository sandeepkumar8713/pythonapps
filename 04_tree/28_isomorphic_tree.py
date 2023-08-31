# https://www.geeksforgeeks.org/tree-isomorphism-problem/
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Similar : https://leetcode.com/problems/invert-binary-tree/
# Question : Write a function to detect if two trees are isomorphic. Two trees are called
# isomorphic if one of them can be obtained from other by a series of flips, i.e. by
# swapping left and right children of a number of nodes. Any number of nodes at any
# level can have their children swapped. Two empty trees are isomorphic.
#
# This is not mirror image
#               1                        1
#            /     \                 /      \
#           2       3               3       2
#          /  \    /                 \     /  \
#         4   5   6                  6    5    4
#           /  \                             /   \
#          7    8                           8    7
#
# Question Type : Easy
# Used : Call a recursive function sIsomorphic(n1, n2).
#        If n1 is None and n2 is None: return True
#        If n1 is None or n2 is None: return False
#        If n1.data != n2.data: return False
#        Now either of two cases can happen: flipped or not flipped.
#        So check for both either should give true.
#        Now call function on n1.left,n2.left and n1.right,n2.right or
#        n1.left,n2.right and n1.right,n2.left
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isIsomorphic(n1, n2):
    if n1 is None and n2 is None:
        return True

    if n1 is None or n2 is None:
        return False

    if n1.data != n2.data:
        return False
    # There are two possible cases for n1 and n2 to be isomorphic
    # Case 1: The subtrees rooted at these nodes have NOT
    # been "Flipped".
    # Both of these subtrees have to be isomorphic, hence the &&
    # Case 2: The subtrees rooted at these nodes have
    # been "Flipped"
    return ((isIsomorphic(n1.left, n2.left) and isIsomorphic(n1.right, n2.right)) or
            (isIsomorphic(n1.left, n2.right) and isIsomorphic(n1.right, n2.left)))


if __name__ == "__main__":
    n1 = Node(1)
    n1.left = Node(2)
    n1.right = Node(3)
    n1.left.left = Node(4)
    n1.left.right = Node(5)
    n1.right.left = Node(6)
    n1.left.right.left = Node(7)
    n1.left.right.right = Node(8)

    n2 = Node(1)
    n2.left = Node(3)
    n2.right = Node(2)
    n2.right.left = Node(4)
    n2.right.right = Node(5)
    n2.left.right = Node(6)
    n2.right.right.left = Node(8)
    n2.right.right.right = Node(7)
    print(isIsomorphic(n1, n2))
