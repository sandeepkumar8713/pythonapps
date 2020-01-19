# CTCI : Q3_02_Stack_Min
# Question : Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(),
# isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the
# SpecialStack. All these operations of SpecialStack must be O(1).
#
# Example :
# Consider the following SpecialStack
# 16  --> TOP
# 15
# 29
# 19
# 18
# When getMin() is called it should return 15, which is the minimum element in the current stack.
# If we do pop two times on stack, the stack becomes
# 29  --> TOP
# 19
# 18
# When getMin() is called, it should return 18 which is the minimum in the current stack
#
# Question Type : ShouldSee
# Used : Push()
#        If stack is not empty, compare x with minEle. Two cases arise:
#        If x is greater than or equal to minEle, simply insert x.
#        If x is less than minEle, insert (2*x - minEle) into the stack and make minEle equal to x.
#        Pop()
#        Remove element from top. Let the removed element be y. Two cases arise:
#        If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
#        If y is less than minEle, the minimum element now becomes (2*minEle - y), so update (minEle = 2*minEle - y)
# Complexity : O(n)


class MyStack:
    def __init__(self):
        self.stack = []
        self.minEle = 99999

    def getMin(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Minimum Element in the stack is: " + str(self.minEle))

    def peek(self):
        if not self.stack:
            print("Stack is empty")
            return None

        t = self.stack[-1]
        if t < self.minEle:
            return self.minEle
        else:
            return t

    def push(self,x):
        if not self.stack:
            self.minEle = x
            self.stack.append(x)
            return

        if x < self.minEle:
            self.stack.append(2 * x - self.minEle)
            self.minEle = x
        else:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None

        # t = self.stack[-1]
        # del self.stack[-1]
        t = self.stack.pop()

        if t < self.minEle:
            toBeRemoved = self.minEle
            self.minEle = 2 * self.minEle - t
            return toBeRemoved
        else:
            return t

    def printAll(self):
        for item in self.stack:
            print(item, end=" ")
        print('')


if __name__ == "__main__":
    s = MyStack()
    s.push(3)
    s.push(5)
    s.printAll()
    s.getMin()
    s.push(2)
    s.push(1)
    s.printAll()
    s.getMin()
    s.pop()
    s.getMin()
    s.pop()
    s.printAll()
    #print s.peek()
