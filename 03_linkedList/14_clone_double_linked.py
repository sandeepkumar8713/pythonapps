# http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/
# Question : You are given a Double Link List with one pointer of each node pointing to the next node just like in a
# single link list. The second pointer however CAN point to any node in the list and not just the previous node.
# Now write a program in O(n) time to duplicate(clone) this list.
#
# Used : Traverse the original linked list and make a copy of nodes.
#        Make a hash map of key value pair with original linked list node and copied linked list node.
#        Traverse the original linked list again and using the hash map adjust the next and random reference of
#           cloned linked list nodes
#        Do this while looping second time over the original linked list.
#           myMap[origCurrNode].next = myMap[origCurrNode.next]
#           myMap[origCurrNode].random = myMap[origCurrNode.random]
#        return new Linked list with head = myMap[head]
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


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
            print temp.data,   # temp.random
            temp = temp.next

    def clone(self):
        origCurrNode = self.head
        newCurrNode = None
        myMap = dict()
        # This is important, What if random points to None.
        myMap[None] = None

        while origCurrNode:
            newCurrNode = Node(origCurrNode.data)
            myMap[origCurrNode] = newCurrNode
            origCurrNode = origCurrNode.next

        origCurrNode = self.head

        while origCurrNode:
            myMap[origCurrNode].next = myMap[origCurrNode.next]
            myMap[origCurrNode].random = myMap[origCurrNode.random]
            origCurrNode = origCurrNode.next

        newList = LinkedList()
        newList.head = myMap[self.head]
        return newList


if __name__ == "__main__":
    myList = LinkedList()
    myList.push(5)
    myList.push(4)
    myList.push(3)
    myList.push(2)
    myList.push(1)

    myList.head.random = myList.head.next.next
    myList.head.next.random = myList.head.next.next.next
    myList.head.next.next.random = myList.head.next.next.next.next
    myList.head.next.next.next.random = myList.head.next.next.next.next.next
    myList.head.next.next.next.next.random = myList.head.next

    print "Original: "
    myList.printList()
    newList = myList.clone()
    print "\nCloned: "
    newList.printList()
