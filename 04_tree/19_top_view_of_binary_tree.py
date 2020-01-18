# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
# Question : Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
# Given a binary tree, print the top view of it. The output nodes can be printed in any order.
#
#         1
#       /   \
#     2       3
#       \
#         4
#           \
#             5
#              \
#                6
# Top view of the above binary tree is : 2 1 3 6
#
# Used : Do level order traversal of tree while maintaining Horizontal Distance HD of each node.
#        Push root element in queue, set its root.HD = 0. Maintain myMap dict, to store visited HD.
#        Loop until queue is empty
#           a) Pop top node from queue and if node.hd is not in myMap then insert HD and node.data in myMap
#           b) If node.left is present set temp.left.hd = hd - 1 and push it in queue
#           c) If node.right is present set temp.right.hd = hd + 1 push it in queue
#        After the loop, sort the map based on keys and print its value
# Complexity : O(n)


import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.hd = sys.maxint
        self.left = None
        self.right = None


def topView(root):
    if root is None:
        return

    hd = 0
    myMap = dict()
    queue = []
    root.hd = hd
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)

        hd = temp.hd
        if hd not in myMap.keys():
            # print temp.data,
            myMap[hd] = temp.data

        if temp.left:
            temp.left.hd = hd - 1
            queue.append(temp.left)

        if temp.right:
            temp.right.hd = hd + 1
            queue.append(temp.right)

    for key in sorted(myMap):
        print myMap[key],


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    topView(root)
