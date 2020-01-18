# https://www.geeksforgeeks.org/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
# Question : Given a linked list and a value x, partition it such that all nodes less than x come first, then all nodes
# with value equal to x and finally nodes with value greater than or equal to x. The original relative order of the
# nodes in each of the three partitions should be preserved.
#
# Examples:
# Input : 1->4->3->2->5->2->3,
#         x = 3
# Output: 1->2->2->3->3->4->5
#
# Used : We should make 3 queues: first, middle, last. Loop through the given list and push in either of the queue.
#        Now merge the queue. Note that new nodes are not created. We play with next pointer.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertIntoQueue(pointers, node):
    head = pointers[0]
    tail = pointers[1]

    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

    pointers[0] = head
    pointers[1] = tail


def mergeTwoList(head1, head2):
    if head1 is None:
        return head2

    node = head1
    while node.next is not None:
        node = node.next

    node.next = head2
    return head1


def printQueue(pointer):
    head = pointer
    while head is not None:
        print (head.data),
        head = head.next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)

        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        temp = self.head
        while temp:
            print (temp.data),
            temp = temp.next

    def partition(self, xValue):
        firstPart = [None, None]
        middlePart = [None, None]
        lastPart = [None, None]

        node = self.head

        while node is not None:
            nextNode = node.next
            # Setting next to null
            node.next = None
            if node.data < xValue:
                insertIntoQueue(firstPart, node)
            elif node.data == xValue:
                insertIntoQueue(middlePart, node)
            else:
                insertIntoQueue(lastPart, node)
            node = nextNode

        firstAndMiddleHead = mergeTwoList(firstPart[0], middlePart[0])
        allHead = mergeTwoList(firstAndMiddleHead, lastPart[0])
        self.head = allHead


if __name__ == "__main__":
    llist = LinkedList()
    data = [1, 4, 3, 2, 5, 2, 3] # x = 3
    #data = [3, 5, 8, 5, 10, 2, 1] # x = 5
    #data = [10, 4, 20, 10, 3]  # x = 3
    #data = [1, 4, 2, 10] # x = 3
    xValue = 3
    for item in data:
        llist.push(item)

    print ("Before")
    llist.printList()
    llist.partition(xValue)
    print ("\nAfter")
    llist.printList()
