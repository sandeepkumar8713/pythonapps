# Similar : https://www.geeksforgeeks.org/pair-with-largest-sum-which-is-less-than-k-in-the-array/
# https://www.geeksforgeeks.org/find-pair-given-sum-sorted-singly-linked-without-extra-space/
# Question : Given a sorted singly linked list and a value x, the task is to find pair whose sum is equal to x.
# We are not allowed to use any extra space and expected time complexity is O(n).
#
# Used : We need to convert single linked list to double linked list. Loop through the linkedList and replace next value
#        with XOR(prev, next). Once this is done take two pointer at left and right of linkedList and find pair sum.
# Complexity : O(n)

memoryMap = {}


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
            print (temp.data),
            temp = temp.next
        print ("")

    def convertPointer(self):
        temp = self.head
        prev = None
        memoryMap[id(prev)] = prev
        while temp:
            nextNode = temp.next
            a = id(nextNode)
            b = id(prev)
            xorValue = a ^ b
            temp.next = xorValue
            memoryMap[id(temp)] = temp
            prev = temp
            temp = nextNode

    def printUsingXor(self):
        temp = self.head
        prev = id(None)
        while temp:
            print temp.data,
            xorValue = temp.next ^ prev

            prev = id(temp)
            temp = memoryMap[xorValue]
        print ""

    def findPair(self, targetSum):
        left = self.head
        temp = self.head

        prev = id(None)
        while temp:
            right = temp
            xorValue = temp.next ^ prev

            prev = id(temp)
            temp = memoryMap[xorValue]

        found = False
        prev = id(None)
        nextNode = id(None)
        while left.data < right.data:
            if left.data + right.data == targetSum:
                print left.data, right.data
                found = True

                # move both left and right forward
                temp = left
                xorValue = left.next ^ prev
                left = memoryMap[xorValue]
                prev = id(temp)

                temp = right
                xorValue = right.next ^ nextNode
                right = memoryMap[xorValue]
                nextNode = id(temp)

            elif left.data + right.data < targetSum:
                temp = left
                xorValue = left.next ^ prev
                left = memoryMap[xorValue]
                prev = id(temp)
            else:
                temp = right
                xorValue = right.next ^ nextNode
                right = memoryMap[xorValue]
                nextNode = id(temp)

        return found


if __name__ == "__main__":
    lList = LinkedList()
    lList.push(11)
    lList.push(10)
    lList.push(9)
    lList.push(8)
    lList.push(7)
    lList.push(6)
    lList.push(3)

    lList.printList()
    lList.convertPointer()
    # lList.printUsingXor()
    if not lList.findPair(17):
        print "not found"
