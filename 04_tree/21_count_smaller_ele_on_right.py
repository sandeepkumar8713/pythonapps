# https://www.geeksforgeeks.org/count-smaller-elements-on-right-side/
# Question : Write a function to count number of smaller elements on right of each element in an array. Given an
# unsorted array arr[] of distinct integers, construct another array countSmaller[] such that countSmaller[i]
# contains count of smaller elements on right side of each element arr[i] in array.
#
# Used : We have use AVL tree. In Node add one more field as size which stores the count of left, right and this nodes.
#        Call a recursive function insert(root, key, smallerCount). We traverse the array from right to left and
#        insert all elements one by one in an AVL tree. While inserting first compare the key with root.
#        If key is smaller than root, call the insert() on left subtree.
#        Else if key is greater than root,  call the insert() on right subtree. Since key is greater than all the nodes
#        in left subtree of root. So we add the size of left subtree to the smallerCount for the key being inserted.
#           smallerCount[0] += self.getSize(root.left) + 1
#        After this update height and size of this node.
#        Then call balance out.
#        (Note to update size while doing leftRotate and rightRotate)
# Complexity : O(n log n)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1


class AVLTree:
    def insert(self, root, key, smallerCount):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key, smallerCount)
        else:
            root.right = self.insert(root.right, key, smallerCount)
            smallerCount[0] += self.getSize(root.left) + 1

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        root.size = self.getSize(root.left) + self.getSize(root.right) + 1
        return self.balanaceOut(root)

    def balanaceOut(self, root):
        balance = self.getBalance(root)
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        z.size = 1 + self.getSize(z.left) + self.getSize(z.right)
        y.size = 1 + self.getSize(y.left) + self.getSize(y.right)
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        z.size = 1 + self.getSize(z.left) + self.getSize(z.right)
        y.size = 1 + self.getSize(y.left) + self.getSize(y.right)
        return y

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getSize(self, root):
        if root is None:
            return 0
        return root.size

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root, result):
        if not root:
            return

        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)


def smallerCount(inpArr):
    avl = AVLTree()
    root = None
    smallerCountList = [0] * len(inpArr)
    for i in range(len(inpArr) - 1, -1, -1):
        smallerCount = [0]
        root = avl.insert(root, inpArr[i], smallerCount)
        smallerCountList[i] = smallerCount[0]
    return smallerCountList


if __name__ == "__main__":
    inpArr = [10, 6, 15, 20, 30, 5, 7]
    # inpArr = [12, 1, 2, 3, 0, 11, 4]
    smallerCountList = smallerCount(inpArr)
    print(smallerCountList)
