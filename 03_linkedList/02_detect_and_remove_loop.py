# Question : Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop
# is present then removes the loop and returns true. And if the list doesn't contain loop then returns false.
# Below diagram shows a linked list with a loop. detectAndRemoveLoop() must change the below list to
# 1->2->3->4->5->NULL.
# Similar Question : Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop(CTCI : Q2_08_Loop_Detection).
#
# Question Type : ShouldSee
# Used : Run a slow and fast pointer, if a loop exist they will be equal at some point.
#        After detecting the loop, if we start slow pointer from head and move both slow and
#        fast pointers at same speed until fast don't meet, they would meet at the
#        beginning of the loop.
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

    def detectAndRemoveLoop(self):
        if self.head is None or self.head.next is None:
            return
        slow = self.head.next
        fast = self.head.next.next

        while fast is not None:
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        # if loop exists
        if slow == fast:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            # Since fast.next is the looping point
            print("loop at :", fast.data)
            fast.next = None  # Remove loop

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    data = [50, 20, 15, 4, 10]
    for item in data:
        llist.push(item)

    # Create a loop for testing
    llist.head.next.next.next.next.next = llist.head.next.next
    llist.detectAndRemoveLoop()
    print("Linked List after removing loop")
    llist.printList()
