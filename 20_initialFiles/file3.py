# Question : binary tree
# print a binary tree with structure
#
# Question Type : OddOne
# Used : TODO :: add used
# Complexity :

class Node:
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        if self.cargo:
            return str(self.cargo)
        return ''


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.treeHeight = self.findHeight(self.root)
        self.masterList=[[] for _ in range(self.treeHeight+1)]

    def findHeight(self,node):
        if not node:
            return 0
        else:
            return 1 + max(self.findHeight(node.left),self.findHeight(node.right))

    def __str__(self):
        self.printTree(self.root,0)
        return self.formString()

    def formString(self):
        noOfLeafs = pow(2,self.treeHeight-1)
        nofSpaceAndElementInLastRow = noOfLeafs + noOfLeafs//2 + (noOfLeafs//2 - 1)*3
        output = ' ' * (nofSpaceAndElementInLastRow//2)
        output += str(self.masterList[0][0]) + '\n'

        noOfInitialSpace = [0] * self.treeHeight
        for i in range(0,self.treeHeight):
            if i < 2:
                noOfInitialSpace[i] = i * 2
            else:
                noOfInitialSpace[i] = 3 * pow(2,i-2) * 2

        #noOfInitialSpace = [0,2,6,12,24]
        #print noOfInitialSpace
        noOfElementInRowList=[0]*self.treeHeight
        noOfElementInRowList[self.treeHeight-1] = nofSpaceAndElementInLastRow
        for i in range(self.treeHeight-2,-1,-1):
            noOfElementInRowList[i] = noOfElementInRowList[i+1] - noOfInitialSpace[self.treeHeight-1-i]

        # noOfElementInRowList = [1,13,19,21] for tree of height 4
        # noOfElementInRowList = [1,25,37,43,45] for tree of height 5
        for i in range(1,self.treeHeight):
            if self.treeHeight < 3:
                gapBetweenTwoElemnet = 1
            else:
                gapBetweenTwoElemnet = (noOfElementInRowList[i] - pow(2,i))//(pow(2,i)-1)
            if i == self.treeHeight-1:
                gapBetweenTwoElemnet = 3

            output += ' ' * (nofSpaceAndElementInLastRow//2 - noOfElementInRowList[i]//2)

            if i==self.treeHeight-1:
                singleSeperator = ' '
            else:
                singleSeperator = ' ' * gapBetweenTwoElemnet
            for j in range(0,len(self.masterList[i]),2):
                output += str(self.masterList[i][j]) + singleSeperator + str(self.masterList[i][j+1]) + ' ' * gapBetweenTwoElemnet
            output += '\n'

        return output

    def printTree(self, node,level):
        if node:
            self.masterList[level].append(str(node))
            self.printTree(node.left, level + 1)
            self.printTree(node.right, level + 1)
        else:
            self.masterList[level].append(' ')


if __name__ == '__main__':
    #binaryTree = Tree(Node(9,Node(6),Node(7,None,Node(15))))
    #binaryTree = Tree(Node(9, Node(6,Node(8),Node(1)), Node(7, Node(1), Node(5))))
    leftNode = Node(9, Node(6,Node(8),Node(1)), Node(7, Node(1), Node(5)))
    rightNode = Node(9, Node(6, Node(8), Node(1)), Node(7, Node(1), Node(5)))
    bigLeft = Node(6,leftNode,rightNode)
    bigRight = Node(6, leftNode, rightNode)
    binaryTree = Tree(Node(5,bigLeft,bigRight))

    #binaryTree = Tree(Node(5,Node(9),Node(6)))
    #binaryTree = Tree(leftNode)

    #binaryTree = Tree(Node(9, Node(6,None,Node(8)), Node(7)))
    print(binaryTree)

