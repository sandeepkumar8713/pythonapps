# https://www.geeksforgeeks.org/level-order-tree-traversal/
# Question : Level order traversal of a tree is breadth first traversal for the tree.
#
#                       20
#                     /    \
#                   8       22
#                 /   \    /  \
#               5      3  4   25
#                     / \
#                   10    14
#
# Question Type : Easy
# Used : Create an empty queue q
#        Append root to the queue
#        Loop while queue is not empty
#           a) pop top node from queue and print node.data
#           b) If node.left is present push it in queue
#           c) If node.right is present push it in queue
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# level order traversal
def levelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data, end=" ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)


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
    levelOrder(root)
