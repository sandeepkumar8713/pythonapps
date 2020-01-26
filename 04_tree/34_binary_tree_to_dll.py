# CTCI : Q17_12_BiNode
# Question : Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right
# pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order
# of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal
# (left most node in BT) must be head node of the DLL.
#
# Question Type : ShouldSee, SimilarAdded
# Used : Keep track of previous node while doing inorder traversal.
#        When this node comes, use previous node to update its right and update left of this node
#        def BinaryTree2DoubleLinkedList(root, head):
#           if root is None: return
#           BinaryTree2DoubleLinkedList(root.left, head)
#           if Static.staticPrev is None:
#               head[0] = root
#           else:
#               root.left = Static.staticPrev
#               Static.staticPrev.right = root
#           Static.staticPrev = root
#           BinaryTree2DoubleLinkedList(root.right, head)
# Complexity : O(n)


class Static:
    staticPrev = None


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BinaryTree2DoubleLinkedList(root, head):
    if root is None:
        return

    BinaryTree2DoubleLinkedList(root.left, head)

    if Static.staticPrev is None:
        head[0] = root
    else:
        root.left = Static.staticPrev
        Static.staticPrev.right = root
    Static.staticPrev = root

    BinaryTree2DoubleLinkedList(root.right, head)


def printList(head):
    while head != None:
        print(head.data, end=" ")
        head = head.right


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    root.right.right = Node(16)

    head = [None]
    BinaryTree2DoubleLinkedList(root, head)
    printList(head[0])
