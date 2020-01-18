# https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
# Question : Write Code to Determine if Two Trees are Identical. Two trees are identical when they have same data and
# arrangement of data is also same.
#
# Used : we need to (pre-order) traverse both trees simultaneously, and while traversing we need to compare data and
#        children of the trees.
# Complexity : O(m) or O(n) (one with smaller tree)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identicalTrees(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left) and
                identicalTrees(a.right, b.right))

    return False


if __name__ == "__main__":
    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    if identicalTrees(root1, root2):
        print "Both trees are identical"
    else:
        print "Trees are not identical"
