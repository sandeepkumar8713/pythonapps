# Question : Given two numbers represented by two linked lists, write a function that returns sum list. The sum list is
# linked list representation of addition of two input numbers. It is not allowed to modify the lists. Also, not
# allowed to use explicit extra space.
#
# Question Type : Generic
# Used : If the size of two linked list is same then it is easy. Recur till the end and come back subtracting.
#        If the size is different, move the current pointer of the larger list to the same size subtract like above.
#        Now do recur from head to current for larger list till ens and come back subtracting borrow.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, data):
        self.data = data

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next


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

    def getSize(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head


def subtractSameSize(head1, head2, borrow):
    if head1 is None:
        return None, 0

    resultNode = Node(0)
    resultNodeNext, borrow = subtractSameSize(head1.getNext(), head2.getNext(), borrow)
    difference = head1.data - head2.data - borrow
    if difference < 0:
        difference = (head1.data + 10) - head2.data - borrow
        borrow = 1
    else:
        borrow = 0
    # sum = head1.data + head2.data + borrow
    # borrow = sum / 10
    # sum = sum % 10

    resultNode.setData(difference)
    resultNode.setNext(resultNodeNext)
    return resultNode, borrow


def insertValues(root, inp):
    for item in inp:
        root.push(item)
    root.printList()


def subtractCarryToRemaining(head1, curr, borrow, resultNode):
    if head1 is not curr:
        resultNodeNext, borrow = subtractCarryToRemaining(head1.getNext(), curr, borrow, resultNode)

        difference = head1.data - borrow
        if difference < 0:
            difference = (head1.data + 10) - borrow
            borrow = 1
        else:
            borrow = 0

        # sum = head1.data + borrow
        # borrow = sum / 10
        # sum = sum % 10

        resultNode = Node(difference)
        resultNode.setNext(resultNodeNext)
        return resultNode, borrow
    else:
        return resultNode, borrow


def getDifference(firstList, secondList):
    size1 = firstList.getSize()
    size2 = secondList.getSize()
    head1 = firstList.getHead()
    head2 = secondList.getHead()
    borrow = 0
    sumList = LinkedList()
    if size1 == size2:
        sumHead, borrow = subtractSameSize(head1, head2, borrow)
    else:
        diff = abs(size1 - size2)
        if size1 < size2:
            head1, head2 = head2, head1
        curr = head1
        while diff > 0:
            curr = curr.getNext()
            diff -= 1
        borrow = 0
        sumHead, borrow = subtractSameSize(curr, head2, borrow)
        sumHead, borrow = subtractCarryToRemaining(head1, curr, borrow, sumHead)

    if borrow > 0:
        newNode = Node(borrow)
        newNode.setNext(sumHead)
        sumHead = newNode
    sumList.setHead(sumHead)
    return sumList


if __name__ == "__main__":
    firstList = LinkedList()
    arr = [1, 2, 3, 6, 2, 3, 4, 5]
    insertValues(firstList, arr)

    print('')
    secondList = LinkedList()
    arr = [5, 1, 1, 5, 6]
    insertValues(secondList, arr)
    print('')

    sumList = getDifference(firstList, secondList)
    sumList.printList()
