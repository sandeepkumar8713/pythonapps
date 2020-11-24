# https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
# Question : The Postfix notation is used to represent algebraic expressions. The expressions written in postfix form
# are evaluated faster compared to infix notation as parenthesis are not required in postfix
#
# Question Type : Easy
# Used : Maintain a stack. Loop over the input expression. If ch is digit push in stack else
#           pop two values from stack, do the operation over them and push it back to stack:
#           stack.push(str(eval(val1 + ch + val2))).
#           Remember while pop, assign val2 then val1
#        After the loop ends pop the an element from stack and return: return int(stack.pop())
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

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data


def evaluate(exp):
    stack = LinkedList()
    for ch in exp:
        if ch.isdigit():
            stack.push(ch)
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            stack.push(str(eval(val1 + ch + val2)))

    return int(stack.pop())


if __name__ == "__main__":
    exp = "231*+9-"
    print(evaluate(exp))
