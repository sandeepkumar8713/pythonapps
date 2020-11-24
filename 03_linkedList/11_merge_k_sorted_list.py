# https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
# Question : Given K sorted linked lists of size N each, merge them and print the sorted output.
# merge k sorted list
#
# Question Type : Easy
# Used : We already know that merging of two linked lists can be done in O(n) time and
#       O(1) space (For arrays O(n)space is required). The idea is to pair up K lists and merge
#       each pair in linear time using O(1) space. After first cycle, K/2 lists are left each of
#       size 2*N. After second cycle, K/4 lists are left each of size 4*N and so on. We repeat the
#       procedure until we have only one list left.
# Complexity : O(k * n * log K)


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

    def setHead(self,node):
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


if __name__ == "__main__":
    firstList = LinkedList()
    arr = [1, 3, 5, 7]
    insertValues(firstList, arr)

    print('')
    secondList = LinkedList()
    arr = [2, 4, 6, 8]
    insertValues(secondList, arr)

    print('')
    thirdList = LinkedList()
    arr = [0, 9, 10, 11]
    insertValues(thirdList, arr)

    linkedListArray = [firstList, secondList, thirdList]
    result = mergeKlist(linkedListArray)

    print('')
    # result = merge(firstList.getHead(), secondList.getHead())
    while result:
        print(result.data,end=" ")
        result = result.next
