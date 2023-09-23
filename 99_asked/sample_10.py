# https://www.chegg.com/homework-help/questions-and-answers/need-soln-python-word-machine-system-performs-sequence-simple-operations-stack-integers-in-q87431322
# Question : A word machine is a system that performs a sequence of simple operations on a stack of integers.
# Initially the stack is empty. The sequence of operations is given as a string. Operations are separated by
# single spaces. The following operations may be specified:
# An integer X (from 0 to 220-1): the machine pushes X onto the stack;
# "POP": the machine removes the topmost number from the stack;
# "DUP": the machine pushes a duplicate of the topmost number onto the stack;
# "+": the machine pops the two topmost elements from the stack, adds them together
# and pushes the sum onto the stack;
# "-": the machine pops the two topmost elements from the stack, subtracts the second one
# from the first (topmost) one and pushes the difference onto the stack.
# After processing all the operations, the machine returns the topmost value from the stack.


import math


def solution(S):
    # Implement your solution here
    inp_arr = S.split(" ")
    stack = []
    for item in inp_arr:
        if item == "DUP":
            if len(stack) < 1:
                return -1

            stack.append(stack[-1])

        elif item == "POP":
            if len(stack) < 1:
                return -1

            stack.pop(-1)

        elif item in ["+", "-"]:
            if len(stack) < 2:
                return -1

            first = stack.pop(-1)
            second = stack.pop(-1)
            if item == "+":
                res = first + second
            else:
                res = first - second
            if 0 <= res <= math.pow(2, 20) - 1:
                stack.append(res)
            else:
                return -1

        elif item.isdigit():
            res = int(item)
            if 0 <= res <= math.pow(2, 20) - 1:
                stack.append(res)
            else:
                return -1

        else:
            return -1

    if len(stack) == 0:
        return -1

    return stack[-1]


if __name__ == "__main__":
    S = "4 5 6 - 7 +"
    assert solution(S) == 8

    S = "13 DUP 4 POP 5 DUP + DUP + -"
    assert solution(S) == 7

    S = "5 6 + -"
    assert solution(S) == -1

    S = "3 DUP 5 - -"
    assert solution(S) == -1

    S = "1048575 DUP +"
    assert solution(S) == -1

    S = "DUP"
    assert solution(S) == -1

    S = "1234567891011"
    assert solution(S) == -1
