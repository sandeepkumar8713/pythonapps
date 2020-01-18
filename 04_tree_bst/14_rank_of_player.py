# Question : Given a list of player names and their scores - {Carl, 70; Alex, 55; Isla, 40}, design a data structure
# that can support following modules in optimal time-
# i) updateEntry(string name, int score)
# ii) getEntryFromRank(int rank)
#
# Used : Use a binary search tree to save data, Here keep track of rightCount of children of each node
#        It is reverse of question find kth smallest element in bst.
#        while temp:
#           if temp.rightCount + 1 == k: return temp.name
#           elif k > temp.rightCount:
#                 k = k - (temp.rightCount + 1)
#                 temp = temp.left
#           else: temp = temp.right
#        return res
# Complexity : insertion and rank both O(log n)


class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.rightCount = 0
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insertUtils(self, root, name, score):
        if root is None:
            newNode = Node(name, score)
            return newNode

        if score < root.score:
            root.left = self.insertUtils(root.left, name, score)
        else:
            root.rightCount += 1
            root.right = self.insertUtils(root.right, name, score)

        return root

    def insert(self, name, score):
        self.root = self.insertUtils(self.root, name, score)

    def getValueFromRank(self, k):
        res = None

        if self.root is None:
            return res

        temp = self.root
        while temp:
            if temp.rightCount + 1 == k:
                res = temp.name
                return res
            elif k > temp.rightCount:
                k = k - (temp.rightCount + 1)
                temp = temp.left
            else:
                temp = temp.right
        return res


if __name__ == "__main__":
    bst = BST()
    bst.insert('Carl', 70)
    bst.insert('Alex', 55)
    bst.insert('Isla', 40)
    bst.insert('John', 80)
    bst.insert('Bob', 75)

    for k in range(1, 6):
        print ("Rank %s %s" % (k, bst.getValueFromRank(k)))
