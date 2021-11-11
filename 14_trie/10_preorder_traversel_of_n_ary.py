# https://careercup.com/question?id=5732671899041792
# Question : Given an n-ary tree and some queries for the tree, in every query you’ll be given a
# node you are supposed to print preorder traversal of the subtree rooted at that node.
#
# Example :
# Input :
# 		   A
# 	    / / \  \
# 	   B F  D   E
#     /\    |  /|\
#    K J    G C H I
#   /\		  |   |
#  N M	      O   L
# Output : A B K N M J F D G E C O H I L
#
# Question Type : ShouldSee
# Used : Do preprocessing of the given input i.e. keep a list of preorder traversed nodes and children
#        count of each node. While searching, just print from the key node till children count of the
#        preorder traversed nodes.
#        Logic :
#        traverseTreeUtils(temp, preOrder, allChildrenCount):
#        count = 0, preOrder.append(temp)
#        allChildrenCount.append(count)
#        index = len(preOrder) - 1
#        for child in temp.children:
#           count += traverseTreeUtils(child, preOrder, allChildrenCount) + 1
#        allChildrenCount[index] = count
#        return count
# Complexity : O(n)


class newNode():
    def __init__(self, key):
        self.key = key
        self.children = []


def traverseTreeUtils(temp, preOrder, allChildrenCount):
    count = 0
    preOrder.append(temp)
    allChildrenCount.append(count)
    index = len(preOrder) - 1
    for child in temp.children:
        count += traverseTreeUtils(child, preOrder, allChildrenCount) + 1
    allChildrenCount[index] = count
    return count


def traverse_tree(root):
    temp = root
    preOrder = []
    allChildrenCount = []
    count = traverseTreeUtils(temp, preOrder, allChildrenCount)
    allChildrenCount[0] = count
    return preOrder, allChildrenCount


def searchNode(preOrder, allChildrenCount, key):
    keyIndex = -1
    for i in range(0, len(preOrder)):
        if preOrder[i].key == key:
            keyIndex = i
            continue

    if keyIndex != -1:
        childrenCount = allChildrenCount[keyIndex]
        for i in range(keyIndex, keyIndex + childrenCount + 1):
            print(preOrder[i].key, end=" ")
    print()


if __name__ == '__main__':
    root = newNode('A')
    (root.children).append(newNode('B'))
    (root.children).append(newNode('F'))
    (root.children).append(newNode('D'))
    (root.children).append(newNode('E'))
    (root.children[0].children).append(newNode('K'))
    (root.children[0].children).append(newNode('J'))
    (root.children[2].children).append(newNode('G'))
    (root.children[3].children).append(newNode('C'))
    (root.children[3].children).append(newNode('H'))
    (root.children[3].children).append(newNode('I'))
    (root.children[0].children[0].children).append(newNode('N'))
    (root.children[0].children[0].children).append(newNode('M'))
    (root.children[3].children[0].children).append(newNode('O'))
    (root.children[3].children[2].children).append(newNode('L'))

    preOrder, allChildrenCount = traverse_tree(root)

    searchNode(preOrder, allChildrenCount, 'A')
    searchNode(preOrder, allChildrenCount, 'B')
    searchNode(preOrder, allChildrenCount, 'C')
    searchNode(preOrder, allChildrenCount, 'D')
    searchNode(preOrder, allChildrenCount, 'E')
