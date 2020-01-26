# https://www.geeksforgeeks.org/find-level-maximum-sum-binary-tree/
# Question : Given a Binary Tree having positive and negative nodes, the task is to find maximum sum level in it.
#
#             1
#            / \
#           2   3
#          /  \  \
#         4    5  8
#                / \
#               6   7
# Output: 17
#
# Question Type : Generic
# Used : Call func maxLevelSum(root). If root is None return 0.
#        set maxSum = root.data
#        Do Level order traversal using queue and keep track of count of elements on each level.
#           Loop over the count and calculate the sum on this level
#           Check if levelSum is more than maxSum and update if required. maxSum = max(maxSum, levelSum)
#        return maxSum
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxLevelSum(root):
    if root is None:
        return 0
    maxSum = root.data

    # Level order Traversal
    queue = []
    queue.append(root)
    while len(queue) > 0:
        count = len(queue)
        levelSum = 0

        while count > 0:
            count -= 1
            temp = queue.pop(0)
            levelSum += temp.data

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        maxSum = max(maxSum, levelSum)

    return maxSum


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print(maxLevelSum(root))
