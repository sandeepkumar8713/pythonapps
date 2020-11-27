# CTCI : Q3_05_Sort_Stack
# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/
# Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
# Question : Given a stack, sort it using recursion.
# Note : It can be solved using temp stack also : https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
#
# Question Type : Generic
# Used : Recursion. Pop top element, call sortStack(), then call sortedInsert(poppedElement)
#        sortedInsert(stack, item):
#        if stack.isEmpty() or item < stack.peek():
#           stack.push(item)
#           return
#        temp = stack.pop()
#        sortedInsert(stack, item)
#        stack.push(temp)
#
#        sortedStack(stack):
#        if not stack.isEmpty():
#           item = stack.pop()
#           sortedStack(stack)
#           sortedInsert(stack, item)
# Complexity : O(n^2)

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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def peek(self):
        if self.head is not None:
            return self.head.data
        return None


def sortedInsert(stack, item):
    if stack.isEmpty() or item < stack.peek():
        stack.push(item)
        return

    temp = stack.pop()
    sortedInsert(stack, item)
    stack.push(temp)


def sortedStack(stack):
    if not stack.isEmpty():
        item = stack.pop()
        sortedStack(stack)
        sortedInsert(stack, item)


if __name__ == "__main__":
    data = [30, -5, 18, 14, -3]
    stack = Stack()
    for item in data:
        stack.push(item)

    print("Before")
    stack.printList()
    sortedStack(stack)
    print("\nAfter")
    stack.printList()
