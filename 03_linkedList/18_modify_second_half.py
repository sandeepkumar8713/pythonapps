# Question : Given a Singly Linked list, Update the second half of the list such
# that nth element becomes sum(1st + nth) element, (n - 1)st element becomes
# sum(2nd + n - 1st) element and so on.
#
# Eg: 2->3->4->5->7 = > 2->3->(4 + 4)->(5 + 3)->(7 + 2)
# Eg: 2->3->6->10->5->7  = > 2->3->6->(10 + 6)->(5 + 3)->(7 + 2)
#
# Question Type : Easy
# Used : Find n, size of given linked list.
#        If n is odd: midPoint = halfSize + 1
#        else : midPoint = halfSize. Also keep a marker for odd or even.
#        Find midPointer using midPoint and add that node's data twice if n is odd.
#        Now reverse the second half.
#        midPointer.next = reverse(head, midPointer.next, halfSize)
#        Run a loop using first and second pointer for halfSize.
#        Sum corresponding data and save in second list.
#        Now reverse the second half again.
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print("")

    def findSize(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def getMidPointer(self, midPoint, isOdd):
        count = 1
        temp = self.head
        while count < midPoint:
            count += 1
            temp = temp.next

        if isOdd:
            temp.data += temp.data
        return temp

    def reverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        return prev

    def addTwoHalves(self, midPointer, halfSize):
        count = 0
        firstHalf = self.head
        secondHalf = midPointer
        while count < halfSize:
            secondHalf.data += firstHalf.data
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
            count += 1

    def addSecondHalf(self):
        n = self.findSize()
        halfSize = n // 2

        if n % 2 == 1:
            midPoint = halfSize + 1
            isOdd = True
        else:
            midPoint = halfSize
            isOdd = False

        midPointer = self.getMidPointer(midPoint, isOdd)
        # midPointer is at 4 for input 2->3->4->5->7
        # midPointer is at 6 for input 2->3->6->10->5->7
        midPointer.next = self.reverse(midPointer.next, halfSize)
        self.addTwoHalves(midPointer.next, halfSize)
        midPointer.next = self.reverse(midPointer.next, halfSize)


if __name__ == "__main__":
    lList = LinkedList()
    lList.push(7)
    lList.push(5)
    lList.push(4)
    lList.push(3)
    lList.push(2)

    # lList.push(7)
    # lList.push(5)
    # lList.push(10)
    # lList.push(6)
    # lList.push(3)
    # lList.push(2)

    print("Given linked list:")
    lList.printList()
    lList.addSecondHalf()
    print("Modified:")
    lList.printList()
