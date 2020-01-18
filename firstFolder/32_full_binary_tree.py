# https://leetcode.com/problems/all-possible-full-binary-trees/
# https://leetcode.com/discuss/interview-question/414082/Google-or-Full-Binary-Trees-With-N-Leaves
# Question : A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# Given an int n, return a list of all possible full binary trees with n leaf nodes. Each element of the answer
# is the root node of one possible tree.
#
# Used : Run a loop from 1 to n, call recur for i leaves in left and n-i leaves in right and then combine the two
#        subtrees into possible tree
#        Logic : def recur(N):
#        if N == 0: return None
#        elif N == 1: return [Node(0)]
#        result = []
#        for i in range(1, N):
#           for left in recur(i):
#               for right in recur(N - i):
#                   root = Node(0)
#                   root.left = left
#                   root.right = right
#                   result.append(root)
#        return result
# Complexity : O(2 ^ n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def preorder(root):
    if root is None:
        print None,
        return
    print root.val,
    preorder(root.left)
    preorder(root.right)


def recur(N):
    # :param N: Number of leaf nodes in the "full" binary tree
    if N == 0:
        return None
    elif N == 1:
        return [Node(0)]

    result = []
    for i in range(1, N):
        for left in recur(i):
            for right in recur(N - i):
                root = Node(0)
                root.left = left
                root.right = right
                result.append(root)
    return result


if __name__ == "__main__":
    N = 4
    for root in recur(N):
        preorder(root)
        print ""
