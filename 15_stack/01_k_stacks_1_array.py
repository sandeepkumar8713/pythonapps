# CTCI : Q3_01_Three_in_One
# Question : https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/
# Create a data structure kStacks that represents k stacks. Implementation of kStacks should use only one array,
# i.e., k stacks should use the same array for storing elements. Following functions must be supported by kStacks.
# push(int x, int sn) : pushes x to stack number 'sn' where sn is from 0 to k-1
# pop(int sn) : pops an element from stack number 'sn' where sn is from 0 to k-1
#
# Question Type : ShouldSee
# Used : We use top of size k to save index of top element of each stack
#        We use one extra array next of size n to save index of next element (next[indexOf1] = indexOf2)
#        We use free variable which points to first available index for insertion
#        push() : insert_at = self.free
#                 self.free = self.next[self.free]
#                 self.arr[insert_at] = item
#                 self.next[insert_at] = self.top[sn]
#                 self.top[sn] = insert_at
#        pop() : topOfStackIndex = self.top[sn]
#                self.top[sn] = self.next[topOfStackIndex]
#                self.next[topOfStackIndex] = self.free
#                self.free = topOfStackIndex
#                return self.arr[topOfStackIndex]
#        Note : For both operations we have to update : arr, free, next, top
# Complexity : Push and pop : O(1), Space : O(2n)


class KStacks:
    def __init__(self, k, n):
        self.k = k  # Number of stacks.
        self.n = n  # Total size of array holding all the 'k' stacks.
        self.arr = [0] * self.n   # Array which holds 'k' stacks.
        self.top = [-1] * self.k  # Stores indexes of top elements in all stacks
        self.free = 0  # Top of the free stack.

        # Points to the next element in either
        # 1. One of the 'k' stacks or,
        # 2. The 'free' stack.
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    # Check whether given stack is empty.
    def isEmpty(self, sn):
        return self.top[sn] == -1

    # Check whether there is space left for pushing new elements or not.
    def isFull(self):
        return self.free == -1

    def push(self, item, sn):
        if self.isFull():
            print("Stack Overflow")
            return

        # Get the first free position to insert at.
        insert_at = self.free

        # Adjust the free position.
        self.free = self.next[self.free]

        # Insert the item at the free position we obtained above.
        self.arr[insert_at] = item

        # Adjust next to point to the old top of stack element.
        self.next[insert_at] = self.top[sn]

        # Set the new top of the stack.
        self.top[sn] = insert_at

    def pop(self, sn):
        if self.isEmpty(sn):
            return None

        # Get the item at the top of the stack.
        topOfStackIndex = self.top[sn]

        # Set new top of stack.
        self.top[sn] = self.next[topOfStackIndex]

        # Push the old top_of_stack to the 'free' stack.
        self.next[topOfStackIndex] = self.free
        self.free = topOfStackIndex

        return self.arr[topOfStackIndex]


if __name__ == "__main__":
    kstacks = KStacks(3, 10)

    kstacks.push(15, 2)
    kstacks.push(45, 2)

    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " + str(kstacks.pop(2)))
    print("Popped element from stack 1 is " + str(kstacks.pop(1)))
    print("Popped element from stack 0 is " + str(kstacks.pop(0)))
