# Question : Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The order of nodes in DLL must be
# same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be
# head node of the DLL.
#
#            10
#          /    \
#        12      15
#       /  \    /
#      25  30  36
#
# Question Type : Generic, SimilarAdded
# Used : Do In order traversal and push the node in double linked list.
# Complexity : O(n)


class DDLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = DDLNode(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = DDLNode(data)
            temp.next.prev = temp

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderTraverse(root, dll):
    if root is None:
        return

    inOrderTraverse(root.left, dll)
    #print root.data,
    dll.push(root.data)
    inOrderTraverse(root.right, dll)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    dll = doubleLinkedList()
    inOrderTraverse(root, dll)
    dll.printList()
