# CTCI : Q2_01_Remove_Dups
# Question : Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?
#
# Used : Approach 1 : we simply iterate through the linked list, adding each element to a hash table. When
#        we discover a duplicate element, we remove the element and continue iterating.
#        Approach 2 : We can iterate with two pointers: current which iterates through the linked list,
#        and runner which checks all subsequent nodes for duplicates.
# Complexity : O(n) and O(n^2)


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
            print temp.data,
            temp = temp.next

    def removeDuplicate(self):
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            runner = current.next
            previousRunner = current
            while runner is not None:
                if current.data == runner.data:
                    previousRunner.next = runner.next
                    runner = runner.next
                else:
                    previousRunner = runner
                    runner = runner.next
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    data = [50, 50, 20, 15, 4, 10, 50, 20, 30]
    for item in data:
        llist.push(item)

    print ("Before")
    llist.printList()
    llist.removeDuplicate()
    print ("\nAfter")
    llist.printList()
