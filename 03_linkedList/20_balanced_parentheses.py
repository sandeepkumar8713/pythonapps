# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
# Question : Given an expression string exp , write a program to examine whether the pairs and the orders of
# {,},(,),[,] are correct in exp.
#
# For example, the program should print true for exp = "[()]{}{[()()]()}" and false for exp = "[(])"
#
# Question Type : Generic
# Used : Declare a character stack S.
#        Now traverse the expression string exp.
#        If the current character is a starting bracket (( or { or [) then push it to stack.
#        Maintain a dict of opening and opening and closing bracket.
#        If the current character is a closing bracket () or } or ]) then pop from stack and if the popped character is
#           the matching starting bracket then fine else parenthesis are not balanced.
#        After complete traversal, if there is some starting bracket left in stack then "not balanced"
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

    def findSize(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


def checkIfBalanced(expression):
    parenthesesDict = {'[': ']', '(': ')', '{': '}'}

    lList = LinkedList()
    for bracket in expression:
        if bracket in parenthesesDict.keys():
            lList.push(bracket)
        elif bracket in parenthesesDict.values():
            openingBracket = lList.pop()
            if parenthesesDict[openingBracket] != bracket:
                return False

    if lList.findSize() != 0:
        return False

    return True


if __name__ == "__main__":
    expression = "[()]{}{[()()]()}"
    # expression = "[(])"
    print(checkIfBalanced(expression))
