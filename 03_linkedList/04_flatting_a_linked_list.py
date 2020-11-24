# Question : Given a linked list where every node represents a linked list and contains two pointers of its type:
# (i) Pointer to next node in the main list (we call it 'right' pointer in below code)
# (ii) Pointer to a linked list where this node is head ('e call it 'down' pointer in below code).
# All linked lists are sorted.
#
# See the following example
#        5 -> 10 -> 19 -> 28
#        |    |     |     |
#        V    V     V     V
#        7    20    22    35
#        |          |     |
#        V          V     V
#        8          50    40
#        |                |
#        V                V
#        30               45
#
# Question Type : ShouldSee
# Used : We use merge() to merge lists one by one. We recursively merge() the current list with
#        already flattened list. The down pointer is used to link nodes of the flattened list.
#        flatten(rootHead):
#        if rootHead is None: return rootHead
#        if rootHead.right is None: return rootHead
#        return merge(rootHead, flatten(rootHead.right.getHead()))
# Complexity : O(kn log n)


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)

        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.down is not None:
                temp = temp.down
            temp.down = newNode

    def getHead(self):
        return self.head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.down

    def pushRight(self, linkedList):
        if self.head.right is None:
            self.head.right = linkedList
        else:
            self.head.right.pushRight(linkedList)

    def getRight(self):
        return self.head.right


def merge(nodeA, nodeB):
    if nodeA is None:
        return nodeB

    if nodeB is None:
        return nodeA

    result = None
    if nodeA.data < nodeB.data:
        result = nodeA
        result.down = merge(nodeA.down, nodeB)
    else:
        result = nodeB
        result.down = merge(nodeA, nodeB.down)

    return result


def flatten(rootHead):
    if rootHead is None:
        return rootHead

    if rootHead.right is None:
        return rootHead

    return merge(rootHead, flatten(rootHead.right.getHead()))


def insertValues(root, inp):
    for item in inp:
        root.push(item)
    root.printList()


if __name__ == "__main__":
    rootList = LinkedList()
    inp = [5, 7, 8, 30]
    insertValues(rootList, inp)

    print('')
    secondList = LinkedList()
    inp = [10, 20]
    insertValues(secondList, inp)
    rootList.pushRight(secondList)

    print('')
    thirdList = LinkedList()
    inp = [19, 22, 50]
    insertValues(thirdList, inp)
    rootList.pushRight(thirdList)

    print('')
    fourthList = LinkedList()
    inp = [28, 35, 40, 45]
    insertValues(fourthList, inp)
    rootList.pushRight(fourthList)

    print('')
    result = flatten(rootList.getHead())
    while result:
        print(result.data, end=" ")
        result = result.down
