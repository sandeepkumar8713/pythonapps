# https://leetcode.com/problems/delete-nodes-and-return-forest/
# https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/403154/Faster-than-99-JAVA
# https://www.geeksforgeeks.org/amazon-interview-experience-for-internship-2021-on-campus/
# Question : Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
# Example : Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
# Question Type : ShouldSee
# Used : Do post order traversal of the given tree, with a result list. If the current node is present in the
#        toBeDeleted list, append left and right subtree in the result list and return None else return Node.
#        Logic : delNodesUtils(root, res, toBeDeleted):
#        leftChild = delNodesUtils(root.left, res, toBeDeleted)
#        rightChild = delNodesUtils(root.right, res, toBeDeleted)
#        if leftChild is None: root.left = None
#        if rightChild is None: root.right = None
#        if root.data in toBeDeleted:
#           if root.left is not None: res.append(root.left)
#           if root.right is not None: res.append(root.right)
#           return None
#        return root
#
#        delNodes(root, toBeDeleted):
#        res = []
#        root = delNodesUtils(root, res, toBeDeleted)
#        if root is not None: res.append(root)
#        return res
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)


def delNodes(root, toBeDeleted):
    res = []

    root = delNodesUtils(root, res, toBeDeleted)
    if root is not None:
        res.append(root)

    return res


def delNodesUtils(root, res, toBeDeleted):
    if root is None:
        return None

    leftChild = delNodesUtils(root.left, res, toBeDeleted)
    rightChild = delNodesUtils(root.right, res, toBeDeleted)

    if leftChild is None:
        root.left = None

    if rightChild is None:
        root.right = None

    if root.data in toBeDeleted:
        if root.left is not None:
            res.append(root.left)

        if root.right is not None:
            res.append(root.right)

        return None

    return root


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    toBeDeleted = [3, 5]

    print("Input Tree : ")
    preorder(root)
    print("")
    print("Forest : ")
    forest = delNodes(root, toBeDeleted)
    for tree in forest:
        preorder(tree)
        print("")
