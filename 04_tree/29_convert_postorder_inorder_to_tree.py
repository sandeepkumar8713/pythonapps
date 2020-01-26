# https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/
# Question : Given Postorder and Inorder traversals, construct the tree.
#
# Input :
# in[]   = {4, 8, 2, 5, 1, 6, 3, 7}
# post[] = {8, 4, 5, 2, 6, 7, 3, 1}
# Output : Root of below tree
#           1
#        /     \
#      2        3
#    /    \   /   \
#   4     5   6    7
#     \
#       8
#
# Question Type : ShouldSee
# Used : Call a recursive function buildUtil(inOrder, postOrder, 0, n-1, [n-1])
#        if inStart > inEnd: return None
#        We first find the last node in post[]. The last node is "1", we know this value is root as root always appear
#        in the end of postorder traversal. So this the root. node = Node(postOrder[postIndex[0]])
#        Now decrement postIndex by -1.
#        if inStart == inEnd: return node (This is leaf node)
#        We search "1" in in[] to find left and right subtrees of root. Everything on left of "1" in in[] is in left
#        subtree and everything on right is in right subtree.
#        So we call the above function on right and left subtree with :
#           inStart and endStart: iIndex + 1, inEnd for right,   inStart and endStart: inStart, iIndex - 1 for left
#        Note that we are calling right first, because we reading node data from postOrder array.
#        return node
#        Logic : def buildUtil(inOrder, postOrder, inStart, inEnd, postIndex):
#        if inStart > inEnd: return None
#        node = Node(postOrder[postIndex[0]])
#        postIndex[0] -= 1
#        if inStart == inEnd:
#           return node
#        iIndex = inOrder.index(node.data)
#        node.right = buildUtil(inOrder, postOrder, iIndex + 1, inEnd, postIndex)
#        node.left = buildUtil(inOrder, postOrder, inStart, iIndex - 1, postIndex)
#        return node
# Complexity : O(n^2)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildUtil(inOrder, postOrder, inStart, inEnd, postIndex):
    if inStart > inEnd:
        return None

    # This will be root
    node = Node(postOrder[postIndex[0]])
    postIndex[0] -= 1

    # This is leaf node
    if inStart == inEnd:
        return node

    iIndex = inOrder.index(node.data)
    node.right = buildUtil(inOrder, postOrder, iIndex + 1, inEnd, postIndex)
    node.left = buildUtil(inOrder, postOrder, inStart, iIndex - 1, postIndex)

    return node


def buildTree(inOrder, postOrder):
    n = len(inOrder)
    return buildUtil(inOrder, postOrder, 0, n-1, [n-1])


def printPreorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)


if __name__ == "__main__":
    inOrder = [4, 8, 2, 5, 1, 6, 3, 7]
    postOrder = [8, 4, 5, 2, 6, 7, 3, 1]
    root = buildTree(inOrder, postOrder)
    printPreorder(root)
