# https://www.geeksforgeeks.org/connect-nodes-at-same-level/
# Question : Write a function to connect all the adjacent nodes at the same level in a binary tree.
#
#                       10
#                     /    \
#                    8      2
#                   /        \
#                  3         90
# Output :
#                       10 --> NULL
#                     /    \
#                    8  --> 2 --> NULL
#                   /        \
#                  3   -->   90 --> NULL
#
# Question Type : Generic, SimilarAdded
# Used : Do Level order traversal using queue and keeping track of count of elements on each level.
#        Loop over the count and connect the nodes on same level.
#        Logic :
#        while len(queue) > 0:
#           count = len(queue)
#           while count > 0:
#               count -= 1
#               temp = queue.pop(0)
#               if count >= 1:
#                   temp.nextRight = queue[0]
#               if temp.left:
#                   queue.append(temp.left)
#               if temp.right:
#                   queue.append(temp.right)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def connectNodes(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        count = len(queue)

        while count > 0:
            count -= 1
            temp = queue.pop(0)

            if count >= 1:
                temp.nextRight = queue[0]

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


def printNext(node):
    print(node.data, '->',end=" ")
    if node.nextRight is None:
        print(-1)
    else:
        print(node.nextRight.data)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(90)

    connectNodes(root)

    printNext(root)
    printNext(root.left)
    printNext(root.right)
    printNext(root.left.left)
    printNext(root.right.right)
