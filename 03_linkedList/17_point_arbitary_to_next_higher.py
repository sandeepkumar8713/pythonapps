# https://www.geeksforgeeks.org/point-to-next-higher-value-node-in-a-linked-list-with-an-arbitrary-pointer/
# Question : Given singly linked list with every node having an additional "arbitrary" pointer that currently points
# to NULL. Need to make the "arbitrary" pointer point to the next higher value node.
#
# Question Type : Asked
# Used : Traverse input list and copy next pointer to arbitrary pointer for every node.
#        Do Merge Sort for the linked list formed by arbitrary pointers and update head accordingly.
# MergeSort() : Call recursive function mergeSort() head = mergeSort(first, n)
#               If n == 1: return first
#               Call divideLink() function which would set null at end of first and return second.
#                   second = divideLink(first, n)
#               firstLength = n/2   secondLength = n/2 if n%2 ==0 else n/2 + 1
#               call mergeSort on first and second:
#                   first = mergeSort(first, firstLength)
#                   second = mergeSort(second, secondLength)
#               return merge(first, second)
# Merge() : It is a recursive function which returns the head pointer to merged list
#           set result = None.
#           if first is None: return second     if second is None: return first
#           if first.data < second.data:
#               result = first
#               result.arbitrary = merge(first.arbitrary, second)
#           else: do same as above on second
#           return result
# Complexity : O(n + n log n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbitrary = None


def divideLink(first, n):
    second = first
    count = 0
    prev = None
    while count < n//2:
        prev = second
        second = second.arbitrary
        count += 1

    prev.arbitrary = None
    return second


def findLength(head):
    temp = head
    n = 0
    while temp:
        n += 1
        temp = temp.arbitrary
    return n


def merge(first, second):
    result = None
    if first is None:
        return second

    if second is None:
        return first

    if first.data < second.data:
        result = first
        result.arbitrary = merge(first.arbitrary, second)
    else:
        result = second
        result.arbitrary = merge(first, second.arbitrary)

    return result


def printAll(head, n):
    temp = head
    count = 0
    while temp and count < n:
        print(temp.data, end=" ")
        count += 1
        temp = temp.arbitrary
    print("")


# merge sort
def mergeSort(first, n):
    if n == 1:
        return first
    second = divideLink(first, n)
    firstLength = n//2
    if n % 2 == 0:
        secondLength = n//2
    else:
        secondLength = n//2 + 1

    first = mergeSort(first, firstLength)
    second = mergeSort(second, secondLength)
    return merge(first, second)


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    def printArbitraryList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.arbitrary

    def populateArbitrary(self):
        temp = self.head
        while temp:
            temp.arbitrary = temp.next
            temp = temp.next

        n = findLength(self.head)
        self.head = mergeSort(self.head, n)


if __name__ == "__main__":
    lList = LinkedList()
    # lList.push(3)
    # lList.push(2)
    # lList.push(10)
    # lList.push(5)

    lList.push(3)
    lList.push(2)
    lList.push(1)
    lList.push(7)
    lList.push(6)
    lList.push(5)
    lList.push(4)

    print("Input:")
    lList.printList()
    lList.populateArbitrary()
    print("\nOutput:")
    lList.printArbitraryList()