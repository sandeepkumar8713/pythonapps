# CTCI : Q10_01_Sorted_Merge
# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/
# Question : Write a SortedMerge() function that takes two lists, each of which is sorted
# in increasing order, and merges the two together into one list which is in increasing order.
# SortedMerge() should return the new list. The new list should be made by splicing together
# the nodes of the first two lists.
#
# For example if the first linked list a is 5->10->15 and the other linked list b is
# 2->3->20, then SortedMerge() should return a pointer to the head node of the merged
# list 2->3->5->10->15->20.
#
# Question Type : Generic
# Used : Take the two lists, compare the data of each, return the lesser node and recursively
#        call and assign its return value to result->next.
#        merge(nodeA, nodeB):
#        if nodeA is None: return nodeB
#        if nodeB is None: return nodeA
#        result = None
#        if nodeA.data < nodeB.data:
#           result = nodeA
#           result.next = merge(nodeA.next, nodeB)
#        else:
#           result = nodeB
#           result.next = merge(nodeA, nodeB.next)
#        return result
# Complexity : O(n + m)


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


def insertValues(root, inp):
    for item in inp:
        root.push(item)
    root.printList()


if __name__ == "__main__":
    firstList = LinkedList()
    arr = [10, 20, 30, 40, 50]
    insertValues(firstList, arr)

    print('')
    secondList = LinkedList()
    arr = [5, 15, 18, 35, 60]
    insertValues(secondList, arr)

    print('')
    result = merge(firstList.getHead(), secondList.getHead())
    while result:
        print(result.data),
        result = result.next
