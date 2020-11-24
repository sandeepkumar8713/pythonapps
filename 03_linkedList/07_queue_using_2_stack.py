# Question : Implement a Queue using 2 stacks s1 and s2 .
#
# Question Type : Easy
# Used : In en-queue operation, the new element is entered at the top of stack1.
#        In de-queue operation, if stack2 is empty then all the elements are moved
#        to stack2 and finally top of stack2 is returned.
# Complexity : O(2n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enQueue(self, data):
        self.s1.push(data)

    def deQueue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                data = (self.s1.pop())
                self.s2.push(data)
        return self.s2.pop()


def insertValues(queue, inp):
    for item in inp:
        queue.enQueue(item)


if __name__ == "__main__":
    queue = Queue()
    arr = [1, 6, 2, 3, 4, 5]
    insertValues(queue, arr)

    print(queue.deQueue(),end = " ")
    print(queue.deQueue(),end = " ")
    print(queue.deQueue(),end = " ")
    queue.enQueue(14)
    print(queue.deQueue(),end = " ")
