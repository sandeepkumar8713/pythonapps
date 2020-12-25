# http://www.geeksforgeeks.org/next-greater-element/
# Question : Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an
# element x is the first greater element on the right side of x in array. Elements for which no greater element exist,
# consider next greater element as -1.
#
# Question Type : Asked
# Used : Stack, push the first element to stack
#        Now loop through the remaining elements, if the current element is larger than top of stack, pop from stack.
#           print(str(element) + " -- " + str(next)), Keep popping from stack unless current is less than top or empty.
#        if current is less than top, push current in stack.
#        When the array finishes, pop remaining elements from the stack and mark them as -1.
#        Other Approach : Start from right side, use min Heap to insert values, Use binary search to search next
#        greater value. Complexity : O(n * log n)
# Complexity : O(n ^ 2), Worst when elements are sorted in decreasing


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()


def printNGE(arr):
    s = createStack()
    element = 0
    next = 0
    push(s, arr[0])
    for i in range(1, len(arr), 1):
        next = arr[i]

        if isEmpty(s) is False:
            element = pop(s)
            while element < next:
                print(str(element) + " -- " + str(next))
                if isEmpty(s) is True:
                    break
                element = pop(s)

            if element > next:
                push(s, element)
        push(s, next)

    while isEmpty(s) is False:
        element = pop(s)
        next = -1
        print(str(element) + " -- " + str(next))


if __name__ == "__main__":
    arr = [11, 13, 21, 3]
    arr = [4, 5, 2, 25]
    printNGE(arr)
