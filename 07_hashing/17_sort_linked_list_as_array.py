# https://www.geeksforgeeks.org/sort-linked-list-order-elements-appearing-array/
# Question : Given an array of size N and a Linked List where elements will be from the array but can also be
# duplicated, sort the linked list in the order, elements are appearing in the array. It may be assumed that
# the array covers all elements of the linked list.
#
# Input : Linked list : 3 2 5 8 5 2 1
#         array : 5, 1, 3, 2, 8
# Output: Sorted Linked List : 5 5 1 3 2 2 8
#
# Question Type : ShouldSee
# Used : First, make a hash table that stores the frequencies of elements in linked list. Then, simply traverse array
#        and for each element of arr[i] check the frequency in the has table and modify the data of list by arr[i]
#        element up to its frequency and at last Print the list.
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
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def sortAsPerArray(self, inpArr):
        freqDict = dict()
        temp = self.head

        while temp:
            if temp.data in freqDict.keys():
                freqDict[temp.data] += 1
            else:
                freqDict[temp.data] = 1
            temp = temp.next

        temp = self.head
        for ele in inpArr:
            freq = freqDict[ele]
            for i in range(freq):
                temp.data = ele
                temp = temp.next


if __name__ == "__main__":
    inpArr = [5, 1, 3, 2, 8]
    lList = LinkedList()
    lList.push(1)
    lList.push(2)
    lList.push(5)
    lList.push(8)
    lList.push(5)
    lList.push(2)
    lList.push(3)

    lList.printList()
    lList.sortAsPerArray(inpArr)
    lList.printList()
