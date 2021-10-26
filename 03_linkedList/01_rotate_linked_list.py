# Question : Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
# Where k is a given positive integer. For example, if the given linked list is 10->20->30
# ->40->50->60 and k is 4, the list should be modified to 50->60->10->20->30->40. Assume
# that k is smaller than the count of nodes in linked list.
#
# Question Type : Easy
# Used : loop till k-1th node, make last.next to head, head to k-1.next, k-1.next to None
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            print(temp.data, end=" ")
            temp = temp.next

    def rotateK(self, k):
        if self.head is None:
            return
        last = self.head
        n = 1
        while last.next is not None:
            last = last.next
            n += 1
        if k > n:
            return

        count = 0
        first = self.head
        while count < k-1:
            first = first.next
            count += 1

        last.next = self.head
        self.head = first.next
        first.next = None


if __name__ == "__main__":
    linkedList = LinkedList()
    data = [10, 20, 30, 40, 50, 60]
    for item in data:
        linkedList.push(item)
    linkedList.printList()
    print('')
    linkedList.rotateK(4)
    linkedList.printList()

