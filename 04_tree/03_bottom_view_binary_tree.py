# Question : Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output
# if x is the bottommost node at its horizontal distance. Horizontal distance of left child of a node x is equal
# to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.
#
# Examples:
#                       20
#                     /    \
#                   8       22
#                 /   \      \
#               5      3      25
#                     / \
#                   10    14
# For the above tree the output should be 5, 10, 3, 14, 25.
#
# Used : Do level order traversal of tree while maintaining Horizontal Distance (HD) of each node.
#        Push root element in queue, loop until queue is empty while pushing left and right nodes in queue.
#        In each iteration, update the map with HD value and data
#        After the loop, sort the map based on keys and print its value
# Complexity : O(n)

import sys
INT_MAX = sys.maxint


class Node:
    def __init__(self, data):
        self.data = data
        self.hd = INT_MAX
        self.left = None
        self.right = None


def bottomView(root):
    if root is None:
        return

    hd = 0
    map = dict()
    queue = []
    root.hd = hd
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)

        hd = temp.hd
        #print temp.data
        map[hd] = temp.data

        if temp.left:
            temp.left.hd = hd - 1
            queue.append(temp.left)

        if temp.right:
            temp.right.hd = hd + 1
            queue.append(temp.right)

    for key in sorted(map):
        print map[key],


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    bottomView(root)

