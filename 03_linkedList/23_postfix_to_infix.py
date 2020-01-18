# https://www.geeksforgeeks.org/postfix-to-infix/
# Question : postfix-to-infix
# Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
# Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
# Input : abc++
# Output : (a + (b + c))
#
# Used : Maintain a stack. Loop over the input expression. If ch is operand push in stack else pop two values from
#           stack, do the operation over them and push it back to stack:
#                stack.push('(' + operand1 + ch + operand2 + ')')
#           Remember while pop, assign operand2 then operand1
#        After the loop ends pop the an element from stack and return: return stack.pop()
# Complexity : O(n)


def isOperand(ch):
    return ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z')


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

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data


def getInfix(postFixExp):
    stack = LinkedList()
    for ch in postFixExp:
        if isOperand(ch):
            stack.push(ch)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push('( ' + operand1 + ' ' + ch + ' ' + operand2 + ' )')

    return stack.pop()


if __name__ == "__main__":
    postFixExp = "ab*c+"
    # postFixExp = "abc++"
    print getInfix(postFixExp)
