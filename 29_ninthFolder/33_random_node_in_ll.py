# https://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/
# https://leetcode.com/problems/linked-list-random-node/
# Question : Given a singly linked list, select a random node from the linked list (the probability of picking
# a node should be 1/N if there are N nodes in the list).
#
# TODO :: add used

import random


# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # A reservoir sampling based function to print a
    # random node from a linked list
    def printRandom(self):

        # If list is empty
        if self.head is None:
            return
        if self.head and not self.head.next:
            print("Randomly selected key is %d" % (self.head.data))

        # Use a different seed value so that we don't get
        # same result each time we run this program
        random.seed()

        # Initialize result as first node
        result = self.head.data

        # Iterate from the (k+1)th element nth element
        # because we iterate from (k+1)th element, or
        # the first node will be picked more easily
        current = self.head.next
        n = 2
        while (current is not None):

            # change result with probability 1/n
            if random.randrange(n) == 0:
                result = current.data

            # Move to next node
            current = current.next
            n += 1

        print("Randomly selected key is %d" % (result))

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(5)
    llist.push(20)
    llist.push(4)
    llist.push(3)
    llist.push(30)
    llist.printRandom()
