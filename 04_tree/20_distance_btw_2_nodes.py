# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
# https://www.geeksforgeeks.org/print-path-between-any-two-nodes-in-a-binary-tree/
# Question : Find the distance between two keys in a binary tree, no parent pointers are given. Distance
# between two nodes is the minimum number of edges to be traversed to reach one node from other.
#
#             1
#          /    \
#         2      3
#        / \   /   \
#       4   5  6   7
#               \
#                8
#
# Used : Here we will be using least common ancestor. From there find the distance to a and b and sum it.
#        lca = findLCA(root, a , b)
#        d1 = findLevel(lca, a, 0)
#        d2 = findLevel(lca, b, 0)
#        return d1 + d2
# findLevel() : Call recursive function findLevel(root, data, level)
#               If root is None: return -1 (not found)
#               If root.data == data: return level
#               Call findLevel again on left subtree.
#               res = findLevel(root.left, data, level + 1)
#               if res != -1: return res
#               Do the same as above for right subtree.
#               return -1 (not found in left and right subtree)
# Similarly we can print path also, by passing a list, appending the root data and popping it in last(if return -1).
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


def findLevel(root, data, level):
    if root is None:
        return -1

    if root.data == data:
        return level

    res = findLevel(root.left, data, level + 1)
    if res != -1:
        return res
    res = findLevel(root.right, data, level + 1)
    if res != -1:
        return res

    return -1


def printPath(root, data, inplist):
    if root is None:
        return -1

    inplist.append(root.data)
    if root.data == data:
        return 1

    res = printPath(root.left, data, inplist)
    if res != -1:
        return res

    res = printPath(root.right, data, inplist)
    if res != -1:
        return res

    inplist.pop()
    return -1


def findDistance(root, a, b):
    lca = findLCA(root, a, b)
    d1 = findLevel(lca, a, 0)
    d2 = findLevel(lca, b, 0)

    list1 = []
    list2 = []
    printPath(lca, a, list1)
    printPath(lca, b, list2)

    list1.reverse()
    print list1 + list2[1:]

    return d1 + d2


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.left.right = Node(5)
    root.right.left.right = Node(8)

    print "path and distance b/w 2 and 3 is:", findDistance(root, 2, 3)
    print "path and distance b/w 4 and 5 is:", findDistance(root, 4, 5)
    print "path and distance b/w 4 and 6 is:", findDistance(root, 4, 6)
    print "path and distance b/w 4 and 6 is:", findDistance(root, 1, 7)
    print "path and distance b/w 4 and 6 is:", findDistance(root, 7, 1)
