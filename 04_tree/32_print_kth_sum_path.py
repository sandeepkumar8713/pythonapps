# CTCI : Q4_12_Paths_with_Sum
# https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
# Question : A binary tree and a number k are given. Print every path in the tree with sum of the nodes in the path
# as k. A path can start from any node and end at any node and must be downward only, i.e. they need not be root
# node and leaf node and negative numbers can also be there in the tree.
#
# Input : k = 5
#         Root of below binary tree:
#            1
#         /     \
#       3        -1
#     /   \     /   \
#    2     1   4     5
#         /   / \     \
#        1   1   2     6
#
# Output :
# 3 2
# 3 1 1
# 1 3 1
# 4 1
# 1 -1 4 1
# -1 4 2
# 5
# 1 -1 5
#
# Question Type : ShouldSee, SimilarAdded
# Used : We have to do preOrder traversal and keep pushing node.data into path list.  When reach to the path and then
#           calculate the pathSum and compare with k one by one over path list moving in reverse i.e. sum += path[len-1]
#           sum += path[len-2], sum += path[len-3] and so on.... Print path if pathSum == k
#        At the end pop the element pushed in path
#        printKPathUtil(root, path, k):
#        if root is None: return
#        path.append(root.data)
#        printKPathUtil(root.left, path, k)
#        printKPathUtil(root.right, path, k)
#        pathSum = 0
#        for j in range(len(path)-1, -1, -1):
#           pathSum += path[j]
#           if pathSum == k:
#               print(path[j::])
#        path.pop()
# Complexity : O(n log n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# preOrder
def printKPathUtil(root, path, k):
    if root is None:
        return

    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)

    pathSum = 0
    # When reach to the path and then calculate the pathSum and compare with k.
    for j in range(len(path)-1, -1, -1):
        pathSum += path[j]

        if pathSum == k:
            print(path[j::])

    path.pop()


def printKPath(root, k):
    path = []
    printKPathUtil(root, path, k)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)
    k = 5

    # root = Node(1)
    # root.left = Node(3)
    # root.left.left = Node(2)
    # k = 6

    printKPath(root, k)
