# https://www.geeksforgeeks.org/remove-all-nodes-which-lie-on-a-path-having-sum-less-than-k/
# Question : Given a binary tree, a complete path is defined as a path from root to a leaf. The sum of all nodes on
# that path is defined as the sum of that path. Given a number K, you have to remove (prune the tree) all nodes
# which don't lie in any path with sum>=k. A node can be part of multiple paths. So we have to delete it only in
# case when all paths from it have sum less than K.
#
# Example :
# Input : K = 8
#            1
#          /   \
#         2     3
#        / \   / \
#       9   3 2  3
# Output :
#            1
#           /
#          2
#         /
#        9
#
# Question Type : ShouldSee
# Used : Call a recursive function prune(root,sum). Do post order traversal, while subtracting sum with node data.
#        If both left and right node return None, then this is leaf node. If sum is more than the node data, return
#        None.
#        def prune(root, sum):
#           if root is None: return None
#           root.left = prune(root.left, sum - root.data)
#           root.right = prune(root.right, sum - root.data)
#           if root.left is None and root.right is None:
#           if sum > root.data: return None
#           return root
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def prune(root, sum):
    if root is None:
        return None

    root.left = prune(root.left, sum - root.data)
    root.right = prune(root.right, sum - root.data)

    if root.left is None and root.right is None:
        if sum > root.data:
            return None

    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(3)

    print("Tree before truncation")
    inorder(root)
    prune(root, 9)
    print("\nTree after truncation")
    inorder(root)
