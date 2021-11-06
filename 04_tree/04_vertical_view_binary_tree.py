# Question : Given a binary tree, print it vertically. The following example illustrates
# vertical order traversal.
#
#            1
#         /    \
#        2      3
#       / \   /   \
#      4   5  6   7
#                /  \
#               8   9
# The output of print this tree vertically will be:
# 4
# 2
# 1 5 6
# 3 8
# 7
# 9
#
# Question Type : Generic
# Used : Do pre-order traversal while calculating HD for each node and adding the elements
#        in map using hd.
#        Elements with same HD comes as 1 vertical line.
#        After traversal, sort the map using keys and print the values.
# Complexity : O(n)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def getVerticalOrder(root, hd, m):
    if root is None:
        return

    try:
        m[hd].append(root.key)
    except:
        m[hd] = [root.key]

    getVerticalOrder(root.left, hd - 1, m)
    getVerticalOrder(root.right, hd + 1, m)


def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)

    for key in sorted(m):
        for item in m[key]:
            print(item,end=" ")
        print("")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    print("Vertical order traversal is")
    printVerticalOrder(root)
