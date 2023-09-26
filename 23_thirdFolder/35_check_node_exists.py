# https://leetcode.com/playground/5ZjWvodJ
# Question : Given a complete (virtual) binary tree, return true/false if the given target
# node exists in the tree or not. Here, the virtual means the tree nodes are numbered assuming
# the tree is a complete binary tree.
# Follow up Question : Given a complete binary tree, count the number of nodes. In a complete
# binary tree every level, except possibly the last, is completely filled, and all nodes
# in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive
# at the last level h.
#
# Example:
#                1
# 		    /         \
# 		   2             3
#        /   \         /  \
#      4   (5)nil     6  (7)nil
# doesNodeExist(root, 4); // true
# doesNodeExist(root, 7); // false, given the node on #7 is a nil node
#
# Question Type : Generic
# Used : Given the target value, push it in stack, divide it by 2 and push again.
#        Repeat this until target becomes 1.
#        Now traverse the tree, pop elements from stack, if it is divisible by 2
#        go left else right. If node is None, return False.
#        Else after the loop return True.
#        For follow up question, find the depth of tree. We would know low and high
#        value of the last level. Now using the function defined in previous question
#        do binary search over it(return high).
# Logic: def doesNodeExist(root, target):
#        if root is None: return False
#        path = getPathFromRootTo(target)
#        return verifyPath(root, path)
#        def getPathFromRootTo(child):
#        stack = []
#        while child != ROOT:
#           stack.append(child)
#           child = child // 2
#        return stack
#        def verifyPath(node, path):
#        while len(path) > 0:
#           if path.pop() % 2 == 0:
#               node = node.left
#           else:
#               node = node.right
#           if node is None: return False
#        return True
#        def findCount(root):
#        depth = getDepth(root)
#        low = 2 ** (depth - 1)
#        high = (2 ** depth) - 1
#        while low < high:
#           mid = low + (high - low)
#           if doesNodeExist(root, mid):
#               low = mid + 1
#           else:
#               high = mid - 1
#        return high
# Complexity : O(log n)

ROOT = 1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def doesNodeExist(root, target):
    if root is None:
        return False
    path = getPathFromRootTo(target)
    return verifyPath(root, path)


def verifyPath(node, path):
    while len(path) > 0:
        if path.pop() % 2 == 0:
            node = node.left
        else:
            node = node.right
        if node is None:
            return False
    return True


def getPathFromRootTo(child):
    stack = []
    while child != ROOT:
        stack.append(child)
        child = child // 2
    return stack


def getDepth(node):
    depth = 0
    while node is not None:
        node = node.left
        depth += 1
    return depth


def findCount(root):
    depth = getDepth(root)
    low = 2 ** (depth - 1)
    high = (2 ** depth) - 1

    while low < high:
        mid = low + (high - low)
        if doesNodeExist(root, mid):
            low = mid + 1
        else:
            high = mid - 1
    return high


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(6)

    print(doesNodeExist(root, 5))
    print(doesNodeExist(root, 7))
    print(doesNodeExist(root, 3))

    root.left.right = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    print(findCount(root))
