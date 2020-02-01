# https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/
# Question : Given a singly linked list, remove all the nodes which have a greater value on right side.
#
# Question Type : Generic
# Used : def removeNextGreater(self):
#        temp = self.head, prev = None
#        while temp.next:
#           if temp.data < temp.next.data:
#               if self.head == temp:
#                   self.head = temp.next
#                   del temp
#                   temp = self.head
#                   prev = None
#               else:
#                   prev.next = temp.next
#                   del temp
#                   temp = prev.next
#               else:
#                   prev = temp
#                   temp = temp.next
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

    def removeNextGreater(self):
        temp = self.head
        prev = None
        while temp.next:
            if temp.data < temp.next.data:
                if self.head == temp:
                    self.head = temp.next
                    del temp
                    temp = self.head
                    prev = None
                else:
                    prev.next = temp.next
                    del temp
                    temp = prev.next
            else:
                prev = temp
                temp = temp.next


if __name__ == "__main__":
    inpArr = [12, 15, 10, 11, 5, 6, 2, 3]
    lList = LinkedList()
    for i in range(len(inpArr) - 1, -1, -1):
        lList.push(inpArr[i])
    lList.printList()
    lList.removeNextGreater()
    lList.printList()
