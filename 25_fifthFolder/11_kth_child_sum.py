# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-6-months-intern-on-campus/
# Question : Given a binary tree, return the sum of all the nodes whose Kth parent (Kth ancestor)
# value is even. Where 0 <  K < 10^7.
#
# Example:
# K=2
#       8
#     /   \
#    2     3
#   / \     \
#  4   5     7
#   \       /
#    6     1
# The 2nd ancestor of 4 , 5 ,7 is 8 and 8 is even
# The 2nd ancestor of 6 is 2 and 2 is even
# The 2nd ancestor of 1 is 3 and 3 is odd
# So the answer is 4 +5 +7+6= 22
#
# Question Type : ShouldSee
# Used : Do post-order traversal, while doing so left and right child returns the dict of sum of its children at each
#        level below it. For current node, check if data is even, if yes then pick value from left and right child
#        dictionary with key K - 1 and add it to the overallSum.
#        Make a new children dict which is a sum of both left and right child, with first value as the node.data.
#        postOrderTraversal(node, level, K):
#        if node is None: return {}
#        leftSum = postOrderTraversal(node.left, level+1, K)
#        rightSum = postOrderTraversal(node.right, level+1, K)
#        if node.data % 2 == 0:
#           if K - 1 in leftSum: overAllSum += leftSum[K - 1]
#           if K - 1 in rightSum: overAllSum += rightSum[K - 1]
#        childrenSum = dict()
#        for key in range(0, K):
#           childrenSum[key + 1] = 0
#           if key in leftSum:
#               childrenSum[key+1] += leftSum[key]
#           if key in rightSum:
#               childrenSum[key+1] += rightSum[key]
#        childrenSum[0] = node.data
#        return childrenSum
# Complexity : O(n), space O(K)

overAllSum = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrderTraversal(node, level, K):
    global overAllSum
    if node is None:
        return {}

    leftSum = postOrderTraversal(node.left, level+1, K)
    rightSum = postOrderTraversal(node.right, level+1, K)

    if node.data % 2 == 0:
        if K - 1 in leftSum:
            overAllSum += leftSum[K - 1]
        if K - 1 in rightSum:
            overAllSum += rightSum[K - 1]

    childrenSum = dict()

    for key in range(0, K):
        childrenSum[key + 1] = 0
        if key in leftSum:
            childrenSum[key+1] += leftSum[key]
        if key in rightSum:
            childrenSum[key+1] += rightSum[key]

    childrenSum[0] = node.data
    return childrenSum


def getSumofKthChild(root, K):
    postOrderTraversal(root, 0, K)
    print(overAllSum)


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.right = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(1)

    K = 2
    getSumofKthChild(root, K)
