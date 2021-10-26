# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
# Question : Given a Linked List and a number n, write a function that returns the
# value at the n'th node from end of the Linked List.
#
# Question Type : Easy
# Used : Maintain two pointers : reference pointer and main pointer. Initialize both
#        reference and main pointers to head. First move reference pointer to n nodes from
#        head. Now move both pointers one by one until reference pointer reaches end.
#        Now main pointer will point to nth node from the end. Return main pointer.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print("")

    def printNthFromLast(self, n):
        if self.head is None:
            return

        mainPtr = self.head
        refPtr = self.head

        count = 0
        while count < n:
            if refPtr is None:
                print("%d is greater than the no. of odes in list" % (n))
                return

            refPtr = refPtr.next
            count += 1

        while refPtr is not None:
            mainPtr = mainPtr.next
            refPtr = refPtr.next

        print("Node no. %d from last is %d " % (n, mainPtr.data))


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)

    llist.printList()
    llist.printNthFromLast(4)
    llist.printNthFromLast(6)
