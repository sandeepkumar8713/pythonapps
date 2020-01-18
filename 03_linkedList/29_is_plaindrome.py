# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
# CTCI : Q2_06_Palindrome
# Question : Given a singly linked list of characters, write a function that returns true if the given
# list is a palindrome, else false.
#
# Used : Recursion. Call a recursive function isPalindrome(node,len) which returns object Result(node, isEqual).
#        isEqual is True if next node to second last node is palindrome
#        node is the last node.
#        This function calls again isPalindrome(node.next, listSize-2). If subList is palindrome and first
#        and last node are same: return Result
#        Note : handle edge case like : listSize = 0,1 or node = None
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Result:
    def __init__(self, node, isEqual):
        self.node = node
        self.isEqual = isEqual


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
            print (temp.data),
            temp = temp.next

    def getSize(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count


def isPalindrome(node, listSize):
    if node is None or listSize <= 0:
        # Return true if we reached middle
        return Result(node, True)
    elif listSize is 1:
        return Result(node.next, True)

    nextResult = isPalindrome(node.next, listSize-2)

    if not nextResult.isEqual or nextResult.node is None:
        return nextResult

    nextResult.isEqual = (nextResult.node.data == node.data)
    nextResult.node = nextResult.node.next
    return nextResult


if __name__ == "__main__":
    llist = LinkedList()
    data = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
    #data = ['b', 'a', 'c', 'a', 'b', 'a']
    #data = ['a','a']
    for item in data:
        llist.push(item)

    llist.printList()
    result = isPalindrome(llist.head, llist.getSize())
    print ("\nIs palindrome : ")
    print (result.isEqual)
