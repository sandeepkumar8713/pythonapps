# https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
# Question : Given two Binary Search Trees(BST), print the elements of both BSTs in sorted form. The expected
# time complexity is O(m+n) where m is the number of nodes in first tree and n is the number of nodes in second
# tree. Maximum allowed auxiliary space is O(height of the first tree + height of the second tree).
#
# Examples:
# First BST
#        3
#     /     \
#    1       5
# Second BST
#     4
#   /   \
# 2       6
# Output: 1 2 3 4 5 6
#
# Used : If root1 is None do in order of root2, return
#        If root2 is None do in order of root1, return
#        while temp1 is not None or temp2 is not None or len(stack1) != 0 or len(stack2) != 0:
#           if temp1 is not None or temp2 is not None:
#               push temp1 to stack1 and set temp1=temp1.left
#               push temp1 to stack2 and set temp1=temp2.left
#           else:
#               if stack1 is empty: while stack2 is not empty:
#                   temp = stack2.pop(), temp2.left = None, inOrder(temp2.right)
#               return
#               Do same if stack2 is empty
#               temp1 = stack1.pop(), temp2 = stack2.pop()
#               if temp1.data < temp2.data:
#                   i.e. print the lower one, move to its right node and push back larger one in stack
#                   print (temp1.data), temp1 = temp1.right, stack2.append(temp2), temp2 = None
#               else:
#                   print (temp2.data), temp2 = temp2.right, stack1.append(temp1), temp1 = None
# Complexity : Time Complexity: O(m+n)
#              Auxiliary Space: O(height of the first tree + height of the second tree)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print (root.data),
        inOrder(root.right)


def pushLeftInStack(temp, stack):
    if temp is None:
        return None
    stack.append(temp)
    return temp.left


def popFromStack(stack):
    while len(stack) != 0:
        temp = stack.pop()
        temp.left = None
        inOrder(temp.right)


def merge(root1, root2):
    stack1 = []
    stack2 = []
    if root1 is None:
        inOrder(root2)

    if root2 is None:
        inOrder(root1)

    temp1 = root1
    temp2 = root2

    while temp1 is not None or temp2 is not None or len(stack1) != 0 or len(stack2) != 0:
        if temp1 is not None or temp2 is not None:
            temp1 = pushLeftInStack(temp1, stack1)
            temp2 = pushLeftInStack(temp2, stack2)
        else:
            if len(stack1) == 0:
                popFromStack(stack2)
                return

            if len(stack2) == 0:
                popFromStack(stack2)
                return

            temp1 = stack1.pop()
            temp2 = stack2.pop()

            if temp1.data < temp2.data:
                print (temp1.data),
                temp1 = temp1.right
                stack2.append(temp2)
                temp2 = None
            else:
                print (temp2.data),
                temp2 = temp2.right
                stack1.append(temp1)
                temp1 = None


if __name__ == "__main__":
    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)

    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(6)

    merge(root1, root2)
