# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
# Question : AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left
# and right subtrees cannot be more than one for all nodes. Self-balancing (or height-balanced) binary search
# tree is any node-based binary search tree that automatically keeps its height (maximal number of levels below
# the root) small in the face of arbitrary item insertions and deletions. AVL tree (inventors Adelson-Velsky
# and Landis) is a implementation of self-balancing binary search tree. It was the first such data structure
# to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if
# at any time they differ by more than one, re-balancing is done to restore this property.
#
# Question Type : OddOne
# Used : AVL algorithm
# Complexity : insertion : O(log n) deletion : O(log n) , left and right rotate : O(1)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        return self.balanaceOut(root)

    def deleteElem(self, root, key):
        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.deleteElem(root.left, key)

        elif key > root.val:
            root.right = self.deleteElem(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteElem(root.right, temp.val)

        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
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
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

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


if __name__== "__main__":
    myTree = AVL_Tree()
    root = None

    """The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""

    # root = myTree.insert(root, 10)
    # root = myTree.insert(root, 20)
    # root = myTree.insert(root, 30)
    # root = myTree.insert(root, 40)
    # root = myTree.insert(root, 50)
    # root = myTree.insert(root, 25)

    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for item in nums:
        root = myTree.insert(root, item)

    print("Preorder traversal of the", "constructed AVL tree is")
    result = []
    myTree.preOrder(root, result)
    print(result)

    root = myTree.deleteElem(root, 10)
    print("Preorder traversal of the", "after deletion")
    result = []
    myTree.preOrder(root, result)
    print(result)
