# https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
# Question : Given a linked list, write a function to reverse every k nodes
# (where k is an input to the function)
#
# Question Type : Asked
# Used : Call a recursive function reverse(head,k).
#           We need to reverse the k nodes first.
#           next = None, prev = None, count = 0
#           Run a loop while current is not None and count < k:
#               set next = current.next
#               set current.next = prev
#               set prev = current
#               set current = next
#               set count += 1
#           if still next is not None:  call reverse again.
#               head.next = self.reverse(next, k)
#           return prev (remember this prev becomes the new head of the list)
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)

        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    lList = LinkedList()
    lList.push(9)
    lList.push(8)
    lList.push(7)
    lList.push(6)
    lList.push(5)
    lList.push(4)
    lList.push(3)
    lList.push(2)
    lList.push(1)

    print("Given linked list")
    lList.printList()
    lList.head = lList.reverse(lList.head, 3)

    print("\nReversed Linked list")
    lList.printList()
