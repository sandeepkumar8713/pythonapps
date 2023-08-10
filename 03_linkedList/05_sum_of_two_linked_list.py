# https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
# Question : Given two numbers represented by two linked lists, write a function that
# returns sum list. The sum list is linked list representation of addition of two input
# numbers. It is not allowed to modify the lists. Also, not allowed to use explicit
# extra space.
#
# Question Type : Generic
# Used : If the size of two linked list is same then it is easy. Recur till the end
#        and come back adding. If the size is different, move the current pointer of
#        the larger list to the same size add like above.
#        Now do recur from head to current for larger list till end and come back
#        adding carry.
# Logic: def addSameSize(head1, head2, carry):
#        if head1 is None: return None, 0
#        resultNode = Node(0)
#        resultNodeNext, carry = addSameSize(head1.getNext(), head2.getNext(), carry)
#        sum = head1.data + head2.data + carry
#        carry = sum / 10
#        sum = sum % 10
#        resultNode.setData(sum)
#        resultNode.setNext(resultNodeNext)
#        return resultNode, carry
#
#        def addCarryToRemaining(head1, curr, carry, resultNode):
#        if head1 is not curr:
#           resultNodeNext, carry = addCarryToRemaining(head1.getNext(), curr, carry, resultNode)
#           sum = head1.data + carry
#           carry = sum / 10
#           sum = sum % 10
#           resultNode = Node(sum)
#           resultNode.setNext(resultNodeNext)
#           return resultNode, carry
#        else:
#           return resultNode, carry
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


def addSameSize(head1, head2, carry):
    if head1 is None:
        return None, 0

    resultNode = Node(0)
    resultNodeNext, carry = addSameSize(head1.getNext(), head2.getNext(), carry)
    sum = head1.data + head2.data + carry
    carry = sum / 10
    sum = sum % 10

    resultNode.setData(sum)
    resultNode.setNext(resultNodeNext)
    return resultNode, carry


def insertValues(root, inp):
    for item in inp:
        root.push(item)
    root.printList()


def addCarryToRemaining(head1, curr, carry, resultNode):
    if head1 is not curr:
        resultNodeNext, carry = addCarryToRemaining(head1.getNext(), curr, carry, resultNode)

        sum = head1.data + carry
        carry = sum / 10
        sum = sum % 10

        resultNode = Node(sum)
        resultNode.setNext(resultNodeNext)
        return resultNode, carry
    else:
        return resultNode, carry


def getSum(firstList, secondList):
    size1 = firstList.getSize()
    size2 = secondList.getSize()
    head1 = firstList.getHead()
    head2 = secondList.getHead()
    carry = 0
    sumList = LinkedList()
    if size1 == size2:
        sumHead, carry = addSameSize(head1, head2, carry)
    else:
        diff = abs(size1 - size2)
        if size1 < size2:
            head1, head2 = head2, head1
        curr = head1
        while diff > 0:
            curr = curr.getNext()
            diff -= 1
        carry = 0
        sumHead, carry = addSameSize(curr, head2, carry)
        sumHead, carry = addCarryToRemaining(head1, curr, carry, sumHead)

    if carry > 0:
        newNode = Node(carry)
        newNode.setNext(sumHead)
        sumHead = newNode
    sumList.setHead(sumHead)
    return sumList


if __name__ == "__main__":
    firstList = LinkedList()
    arr = [1, 6, 2, 3, 4, 5]
    insertValues(firstList, arr)

    print('')
    secondList = LinkedList()
    arr = [5, 1, 1, 5, 6]
    insertValues(secondList, arr)
    print('')

    sumList = getSum(firstList, secondList)
    sumList.printList()