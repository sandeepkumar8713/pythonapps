# https://www.geeksforgeeks.org/sort-linked-list-already-sorted-absolute-values/
# Question : Given a linked list which is sorted based on absolute values. Sort the list based on actual values.
#
# Input : 1 -> -2 -> -3 -> 4 -> -5
# output: -5 -> -3 -> -2 -> 1 -> 4
#
# Question Type : ShouldSee
# Used : Lets take 2 pointer prev = self.head and temp = self.head.next and loop till temp is not None.
#        if temp.data < prev.data: Remove temp and place it at head. and update temp : temp = prev
#           Else update prev = temp
#        temp = temp.next
#        After the loop we will get sorted list
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
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def sort(self):
        prev = self.head
        temp = self.head.next

        while temp:
            if temp.data < prev.data:
                prev.next = temp.next
                temp.next = self.head
                self.head = temp
                temp = prev
            else:
                prev = temp
            temp = temp.next


if __name__ == "__main__":
    lList = LinkedList()
    lList.push(-5)
    lList.push(5)
    lList.push(4)
    lList.push(3)
    lList.push(-2)
    lList.push(1)
    lList.push(0)

    lList.printList()
    lList.sort()
    lList.printList()
