# https://www.geeksforgeeks.org/longest-path-values-binary-tree/
# Question : Given a binary tree, find the length of the longest path where each node in the path has the same
# value. This path may or may not pass through the root. The length of path between two nodes is represented by
# the number of edges between them.
#
# Example :
# Input :
#               4
#              / \
#             4   4
#            / \   \
#           4   9   5
# Output : 3
#
# Question Type : Generic
# Used : We have to do post order traversal. We will call a recursive function which takes node and
#        overall ans as input. It returns the length of path passing through given node.
#        If this length is greater than ans, we update ans.
#        def longestPath(node, ans):
#        left = longestPath(node.left, ans)
#        right = longestPath(node.right, ans)
#        leftMax = 0, rightMax = 0
#        if node.left and node.left.data == node.data: leftMax += left + 1
#        if node.right and node.right.data == node.data: rightMax += right + 1
#        ans[0] = max(ans[0], leftMax + rightMax)
#        return max(leftMax, rightMax)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def longestPath(node, ans):
    if node is None:
        return 0

    left = longestPath(node.left, ans)
    right = longestPath(node.right, ans)

    leftMax = 0
    rightMax = 0

    if node.left and node.left.data == node.data:
        leftMax += left + 1

    if node.right and node.right.data == node.data:
        rightMax += right + 1

    ans[0] = max(ans[0], leftMax + rightMax)
    return max(leftMax, rightMax)


def longestSameValuePath(root):
    ans = [0]
    longestPath(root, ans)
    return ans[0]


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(4)
    root.right = Node(4)
    root.left.left = Node(4)
    root.left.right = Node(9)
    root.right.right = Node(5)
    print(longestSameValuePath(root))
