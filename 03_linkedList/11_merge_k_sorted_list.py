# https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
# https://leetcode.com/problems/merge-k-sorted-lists/
# https://leetcode.com/problems/merge-k-sorted-lists/solutions/368112/simple-python-heapq-with-custom-comparator-function/
# Question : Given K sorted linked lists of size N each, merge them and print the sorted output.
# merge k sorted list
#
# Question Type : Generic
# Used : We will use min heap.
#        Insert all the lists in the minheap using custom sort using setattr.
#        Now keep popping nodes from the minheap until it is empty.
# Logic: def merge_k_list(lists):
#        setattr(Node, "__lt__", lambda self, other: self.data <= other.data)
#        pq = []
#        for l in lists:
#           if l:
#               heapq.heappush(pq, l)
#        head = None, temp = None
#        while pq:
#           node = heapq.heappop(pq)
#           if head is None:
#               head = node
#               temp = node
#           else:
#               temp.next = node
#           temp = node
#           if node and node.next:
#               heapq.heappush(pq, node.next)
#        return head
# Complexity : O(k * n * log k)
# Space : O(k) heap size

import heapq


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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def getHead(self):
        return self.head

    def setHead(self, node):
        self.head = node


def merge(nodeA, nodeB):
    if nodeA is None:
        return nodeB

    if nodeB is None:
        return nodeA

    result = None
    if nodeA.data < nodeB.data:
        result = nodeA
        result.next = merge(nodeA.next, nodeB)
    else:
        result = nodeB
        result.next = merge(nodeA, nodeB.next)

    return result


def mergeKlist(linkedListArray):
    last = len(linkedListArray) - 1

    while last != 0:
        i = 0
        j = last

        while i < j:
            result = merge(linkedListArray[i].getHead(), linkedListArray[j].getHead())
            linkedListArray[i].setHead(result)

            i += 1
            j -= 1

            if i >= j:
                last = j

    return linkedListArray[0].getHead()


def insertValues(root, inp):
    for item in inp:
        root.push(item)
    root.printList()


def merge_k_list(lists):
    setattr(Node, "__lt__", lambda self, other: self.data <= other.data)
    pq = []
    for l in lists:
        if l:
            heapq.heappush(pq, l)

    head = None
    temp = None
    while pq:
        node = heapq.heappop(pq)
        if head is None:
            head = node
            temp = node
        else:
            temp.next = node
        temp = node
        if node and node.next:
            heapq.heappush(pq, node.next)

    return head


def insert_values(inp):
    head = None
    temp = None
    for data in inp:
        node = Node(data)
        if head is None:
            head = node
            temp = node
        else:
            temp.next = node
        temp = node

    return head


if __name__ == "__main__":
    arr = [1, 3, 5, 7]
    first_list = insert_values(arr)

    arr = [2, 4, 6, 8]
    second_list = insert_values(arr)

    arr = [0, 9, 10, 11]
    third_list = insert_values(arr)

    linkedListArray = [first_list, second_list, third_list]
    result = merge_k_list(linkedListArray)

    while result:
        print(result.data, end=" ")
        result = result.next
