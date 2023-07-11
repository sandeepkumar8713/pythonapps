# https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/
# https://leetcode.com/problems/reorder-list/
# Question : Given a singly linked list L0 -> L1 -> ... -> Ln-1 -> Ln. Rearrange the
# nodes in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...
#
# Input:  1 -> 2 -> 3 -> 4
# Output: 1 -> 4 -> 2 -> 3
#
# Question Type : Easy
# Used : Split the linked list in two halves using found middle point.
#        Reverse the second half.
#        Do alternate merge of first and second halves.
# Logic: mergeSecondHalf():
#        Calculate halfSize(n/2).
#        If n is odd: midPoint = halfSize + 1. else : midPoint = halfSize.
#        Call divideLink(first,midpoint) function which would set null at end of first
#        and return second.
#        Now reverse the second half : midPointer = reverse(midPointer, halfSize)
#        call recursive function merge. self.head = merge(head, midPointer)
#        Merge():
#        set result = None
#        if first is None: return second
#        if second is None: return first
#        result = first
#        result.next = merge(second, first.next) (Here we merge alternate lists)
#        return result
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

    def divideLink(self, midPoint):
        first = self.head
        second = first
        count = 1
        prev = None
        while count <= midPoint:
            prev = second
            second = second.next
            count += 1

        prev.next = None
        return second

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

    def mergeSecondHalf(self):
        n = self.findSize()
        halfSize = n / 2

        if n % 2 == 1:
            midPoint = halfSize + 1
        else:
            midPoint = halfSize

        midPointer = self.divideLink(midPoint)
        midPointer = self.reverse(midPointer, halfSize)
        self.head = merge(self.head, midPointer)


def merge(first, second):
    result = None
    if first is None:
        return second

    if second is None:
        return first

    result = first
    result.next = merge(second, first.next)

    return result


if __name__ == "__main__":
    inpArr = [5, 4, 3, 2, 1]
    # inpArr = [6, 5, 4, 3, 2, 1]
    lList = LinkedList()
    for ele in inpArr:
        lList.push(ele)
    print("original:")
    lList.printList()
    lList.mergeSecondHalf()
    print("modified:")
    lList.printList()
