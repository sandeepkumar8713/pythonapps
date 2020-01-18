# https://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/
# Question : Given a Balanced Binary Search Tree and a target sum, write a function that returns true if there
# is a pair with sum equals to target sum, otherwise return false. Expected time complexity is O(n) and only
# O(Log n) extra space can be used. Any modification to Binary Search Tree is not allowed. Note that height
# of a Balanced BST is always O(Log n).
#
#                    15
#                 /     \
#               10      20
#              / \     /  \
#             8  12   16  25
#
# Used : We traverse BST in Normal Inorder and Reverse Inorder simultaneously. In reverse inorder, we start from the
#        rightmost node which is the maximum value node. In normal inorder, we start from the left most node which is
#        minimum value node. We add sum of current nodes in both traversals and compare this sum with given target sum.
#        If the sum is same as target sum, we return true. If the sum is more than target sum, we move to next node in
#        reverse inorder traversal, otherwise we move to next node in normal inorder traversal.
# Inorder : while not done1:
#               If temp1 is not None, push the node in stack and move temp to next left.
#               else: if stack is empty. set done1 = true
#                    else: pop top node from stack. set val1 = temp1.data, move temp1 to next right and set done1 = true
# Reverse Inorder : keeping pushing right node
# Complexity : time : O(n) space : O(log n) for balanced tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insertUtils(self, root, data):
        if root is None:
            newNode = Node(data)
            return newNode

        if data < root.data:
            root.left = self.insertUtils(root.left, data)
        else:
            root.right = self.insertUtils(root.right, data)

        return root

    def insert(self, data):
        self.root = self.insertUtils(self.root, data)


def findPair(bst, targetSum):
    temp1 = bst.root
    temp2 = bst.root

    nodeStack1 = []
    nodeStack2 = []

    done1 = False
    done2 = False

    val1 = -1
    val2 = -1

    while 1:
        while not done1:
            if temp1 is not None:
                nodeStack1.append(temp1)
                temp1 = temp1.left
            else:       # if temp1 is None
                if len(nodeStack1) == 0:
                    done1 = True
                else:
                    temp1 = nodeStack1.pop()
                    val1 = temp1.data
                    temp1 = temp1.right
                    done1 = True

        while not done2:
            if temp2 is not None:
                nodeStack2.append(temp2)
                temp2 = temp2.right
            else:
                if len(nodeStack2) == 0:
                    done2 = True
                else:
                    temp2 = nodeStack2.pop()
                    val2 = temp2.data
                    temp2 = temp2.right
                    done2 = True

        if val1 != val2 and (val1 + val2) == targetSum:
            print val1, val2
            return True

        if (val1 + val2) < targetSum:
            done1 = False

        if (val1 + val2) > targetSum:
            done2 = False

        if val1 >= val2:
            return False


if __name__ == "__main__":
    bst = BST()
    bst.insert(15)
    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(20)
    bst.insert(16)
    bst.insert(25)

    if findPair(bst, 33) is False:
        print "Pair Not Found"
