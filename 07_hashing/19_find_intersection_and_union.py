# https://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/
# Question : Given two Linked Lists, create union and intersection lists that contain union and intersection
# of the elements present in the given lists. Order of elements in output lists doesn't matter.
#
# Input:
#    List1: 10->15->4->20
#    List2:  8->4->2->10
# Output:
#    Intersection List: 4->10
#    Union List: 2->8->20->4->15->10
#
# Question Type : Easy
# Used : Union (list1, list2) : Initialize the result list as NULL and create an empty hash table. Traverse both lists
#        one by one, for each element being visited, look the element in hash table. If the element is not present,
#        then insert the element to result list. If the element is present, then ignore it.
#        Intersection (list1, list2): Initialize the result list as NULL and create an empty hash table. Traverse list1.
#        For each element being visited in list1, insert the element in hash table. Traverse list2, for each element
#        being visited in list2, look the element in hash table. If the element is present, then insert the element to
#        result list. If the element is not present, then ignore it.
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


def getIntersection(lList1, lList2):
    hashSet = set()
    insersectionLinkedList = LinkedList()

    temp = lList1.head
    while temp:
        hashSet.add(temp.data)
        temp = temp.next

    temp = lList2.head
    while temp:
        if temp.data in hashSet:
            insersectionLinkedList.push(temp.data)
        temp = temp.next

    return insersectionLinkedList

def getUnion(lList1, lList2):
    hashSet = set()
    unionLinkedList = LinkedList()

    temp = lList1.head
    while temp:
        hashSet.add(temp.data)
        unionLinkedList.push(temp.data)
        temp = temp.next

    temp = lList2.head
    while temp:
        if temp.data not in hashSet:
            unionLinkedList.push(temp.data)
        temp = temp.next

    return unionLinkedList


if __name__ == "__main__":
    lList1 = LinkedList()
    lList1.push(20)
    lList1.push(4)
    lList1.push(15)
    lList1.push(10)
    print("list 1:",end=" ")
    lList1.printList()


    lList2 = LinkedList()
    lList2.push(10)
    lList2.push(2)
    lList2.push(4)
    lList2.push(8)
    print("list 2:",end=" ")
    lList2.printList()

    insersectionLinkedList = getIntersection(lList1, lList2)
    print("intersection:",end=" ")
    insersectionLinkedList.printList()

    unionLinkedList = getUnion(lList1, lList2)
    print("union:",end=" ")
    unionLinkedList.printList()
