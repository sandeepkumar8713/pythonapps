# https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
# Question : Given a Binary Tree, check whether the Binary tree contains a duplicate
# sub-tree of size 2 or more.
#
# Input :  Binary Tree
#                A
#              /    \
#            B        C
#          /   \       \
#         D     E       B
#                      /  \
#                     D    E
# Output : Yes
#
# Question Type : Asked
# Used : We will do post order traversal and keep saving the nodes as string sequence
#        in hash table and comparing if already found before.
#        dupSubUtil(root):
#        subStr = ""
#        if root is None: return subStr + MARKER
#        lStr = dupSubUtil(root.left)
#        if lStr == subStr: return subStr
#        rStr = dupSubUtil(root.right)
#        if rStr == subStr: return subStr
#        subStr += root.data + lStr + rStr
#        if len(subStr) > 3 and subStr in subTrees: return ""
#        subTrees.add(subStr)
#        return subStr
#        if subStr is "", then we found the subtree.
# Complexity : O(n)

MARKER = '$'
subTrees = set()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dupSubUtil(root):
    global subTrees
    subStr = ""
    if root is None:
        return subStr + MARKER

    lStr = dupSubUtil(root.left)
    if lStr == subStr:
        return subStr

    rStr = dupSubUtil(root.right)
    if rStr == subStr:
        return subStr

    subStr += root.data + lStr + rStr
    # Note that size of a serialized tree with single node is 3 as it has two marker nodes.
    if len(subStr) > 3 and subStr in subTrees:
        # print subStr
        return ""

    subTrees.add(subStr)
    return subStr


if __name__ == "__main__":
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('B')
    root.right.right.right = Node('E')
    root.right.right.left = Node('D')

    if dupSubUtil(root) == "":
        print("yes")
    else:
        print("no")
