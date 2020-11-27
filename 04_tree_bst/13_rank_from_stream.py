# CTCI : Q10_10_Rank_from_Stream
# Question : Given a stream of integers, lookup the rank of a given integer x. Rank of an integer in stream is
# "Total number of elements less than or equal to x (not including x)". If element is not found in stream or is
# smallest in stream, return -1.
#
# Question Type : Easy
# Used : In BST we also add leftSize as a member of node. While inserting elements in BST, we keep
#        updating leftSize.
#        We traverse the tree from root and compare the root values to x.
#        If root->data == x : return root.leftSize
#        If x < root.data : return getRankUtils(root.left, x) (If no child, return -1)
#        If x > root->data : return getRank(root->right) + root.leftSize + 1
#           (If no child, return -1; if getRank is -1, return -1)
# Complexity : O(log n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftSize = 0


class BST:
    def __init__(self):
        self.root = None

    def insertUtils(self, root, data):
        if root is None:
            newNode = Node(data)
            return newNode

        if data < root.data:
            root.left = self.insertUtils(root.left, data)
            root.leftSize += 1
        else:
            root.right = self.insertUtils(root.right, data)

        return root

    def insert(self, data):
        self.root = self.insertUtils(self.root, data)

    def getRankUtils(self, root, x):
        if root.data == x:
            return root.leftSize

        if x < root.data:
            if root.left is None:
                return -1
            else:
                return self.getRankUtils(root.left, x)
        else:
            if root.right is None:
                return -1
            else:
                rightSize = self.getRankUtils(root.right, x)
                if rightSize is -1:
                    return rightSize
                return root.leftSize + 1 + rightSize

    def getRank(self, x):
        return self.getRankUtils(self.root, x)


if __name__ == '__main__':
    arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    bst = BST()

    for i in range(len(arr)):
        bst.insert(arr[i])

    x = 4
    print("Rank of", x, "in stream is:", bst.getRank(x))
    x = 13
    print("Rank of", x, "in stream is:", bst.getRank(x))
    x = 100
    print("Rank of", x, "in stream is:", bst.getRank(x))
    x = 0
    print("Rank of", x, "in stream is:", bst.getRank(x))
