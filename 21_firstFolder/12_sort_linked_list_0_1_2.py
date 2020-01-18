# https://www.geeksforgeeks.org/sort-a-linked-list-of-0s-1s-or-2s/
# Question : Given a linked list of 0s, 1s and 2s, sort it.
#
# Used : Traverse the list and count the number of 0s, 1s and 2s. Let the counts be n1, n2 and n3 respectively.
#        Traverse the list again, fill the first n1 nodes with 0, then n2 nodes with 1 and finally n3 nodes
#        with 2.
# Complexity : O(n)


class LinkedList(object):
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def sortList(self):
        count = [0, 0, 0]
        ptr = self.head

        while ptr is not None:
            count[ptr.data] += 1
            ptr = ptr.next

        i = 0
        ptr = self.head
        while ptr is not None:
            if count[i] == 0:
                i += 1
            else:
                ptr.data = i
                count[i] -= 1
                ptr = ptr.next

    def printList(self):
        temp = self.head
        while temp is not None:
            print str(temp.data),
            temp = temp.next
        print ''


if __name__ == "__main__":
    # Drier program to test above functions
    lList = LinkedList()
    lList.push(0)
    lList.push(1)
    lList.push(0)
    lList.push(2)
    lList.push(1)
    lList.push(1)
    lList.push(2)
    lList.push(1)
    lList.push(2)

    print "Linked List before sorting :"
    lList.printList()
    lList.sortList()
    print "Linked List after sorting :"
    lList.printList()
