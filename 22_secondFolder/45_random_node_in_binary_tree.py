# https://www.geeksforgeeks.org/select-random-node-tree-equal-probability/
# Question : Given a Binary Tree with children Nodes, Return a random Node with equal Probability of
# selecting any Node in tree. Consider the given tree with root as 1.
#
# Used : An alternate solution is to modify tree structure. We store count of children in every node.
#        Consider the above tree. We use in-order traversal here also. We generate a random number smaller than
#        or equal count of nodes. We traverse tree and go to the node at that index. We use counts to quickly
#        reach the desired node. With counts, we reach in O(h) time where h is height of tree.
# Complexity : O(log n)


from random import randint


class Node:

    def __init__(self, data):
        self.data = data
        self.children = 0
        self.left = None
        self.right = None


# This is used to fill children counts.
def getElements(root):
    if root == None:
        return 0

    return (getElements(root.left) +
            getElements(root.right) + 1)


# Inserts Children count for each node
def insertChildrenCount(root):
    if root == None:
        return

    root.children = getElements(root) - 1
    insertChildrenCount(root.left)
    insertChildrenCount(root.right)


# Returns number of children for root
def children(root):
    if root == None:
        return 0
    return root.children + 1


def randomNodeUtil(root, count):
    if root == None:
        return 0

    if count == children(root.left):
        return root.data

    if count < children(root.left):
        return randomNodeUtil(root.left, count)

    return randomNodeUtil(root.right,
                          count - children(root.left) - 1)


def randomNode(root):
    count = randint(0, root.children)
    return randomNodeUtil(root, count)


if __name__ == "__main__":
    # Creating Above Tree
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.right = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    insertChildrenCount(root)

    print("A Random Node From Tree :", randomNode(root))
