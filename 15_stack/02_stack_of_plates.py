# CTCI : Q3_03_Stack_of_Plates
# Question : Stack of Plates:
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
# we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
# SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack
# once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically
# to a single stack (that is, pop () should return the same values as it would if there were just a single stack).
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack
#
# Question Type : ShouldSee
# Used : Make a class of members : capacity and stacks. where capacity is max size of each sub stack
#        and stacks is a list of lists.
#        Push :
#        Find the last list from stack and append data in it. If it is already filled,
#        append one more list(with data) in stacks
#        Pop :
#        Find the last list from stack. pop the last element from the list. If this list becomes empty, pop this
#        list from the stacks
#        PopAt: Find the element from the given index, pop it and readjust remaining elements on right side.
#        Logic :
#        subStackIndex = index // self.capacity
#        innerIndex = index % self.capacity
#        subStack = self.stacks[subStackIndex]
#        subStack.pop(innerIndex)
#        while subStackIndex + 1 < len(self.stacks):
#           subStack = self.stacks[subStackIndex]
#           nextSubStack = self.stacks[subStackIndex + 1]
#           data = nextSubStack.pop(0)
#           subStack.append(data)
#           subStackIndex += 1
# Complexity : popAt(index) O(n)


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def getLastStack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def push(self, i):
        subtack = self.getLastStack()
        if subtack is None or len(subtack) == self.capacity:
            stack = [i]
            self.stacks.append(stack)
        else:
            subtack.append(i)

    def pop(self):
        subtack = self.getLastStack()
        if subtack is None:
            print("Stack empty")
            return
        subtack.pop(-1)
        if len(subtack) == 0:
            self.stacks.pop(-1)

    def printAll(self):
        for substack in self.stacks:
            print(substack)

    def popAt(self, index):
        subStackIndex = index // self.capacity
        innerIndex = index % self.capacity

        subStack = self.stacks[subStackIndex]
        subStack.pop(innerIndex)

        while subStackIndex + 1 < len(self.stacks):
            subStack = self.stacks[subStackIndex]
            nextSubStack = self.stacks[subStackIndex + 1]
            data = nextSubStack.pop(0)
            subStack.append(data)
            subStackIndex += 1


if __name__ == "__main__":
    capacityPerSubStack = 5
    setOfStacks = SetOfStacks(capacityPerSubStack)
    for i in range(35):
        setOfStacks.push(i)

    for i in range(10):
        setOfStacks.pop()

    setOfStacks.printAll()
    setOfStacks.popAt(7)
    setOfStacks.popAt(0)
    setOfStacks.printAll()
