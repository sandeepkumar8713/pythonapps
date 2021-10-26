# CTCI : Q3_04_Queue_via_Stacks
# Question : Implement a Stack using 2 queue q1 and q2
#
# Question Type : Easy
# Used : In push operation, the new element is always enqueued to q1.
#        In pop() operation, if q2 is empty then all the elements except the last,
#        are moved to q2.
#        Finally the last element is dequeued from q1 and returned.
# Complexity : O(2n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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

    def getSize(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        self.q1.push(data)

    def pop(self):
        size = self.q1.getSize()
        while size > 1:
            data = self.q1.pop()
            self.q2.push(data)
            size -= 1
        if size == 1:
            data = self.q1.pop()
            self.q1, self.q2 = self.q2, self.q1
            return data
        return None


def insertValues(root, inp):
    for item in inp:
        root.push(item)


if __name__ == "__main__":
    stack = Stack()
    arr = [1, 6, 2, 3, 4, 5]
    insertValues(stack, arr)

    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    stack.push(14)
    print(stack.pop(), end=" ")
