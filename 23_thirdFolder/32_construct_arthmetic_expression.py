# https://leetcode.com/discuss/interview-question/351147/Google-or-Onsite-or-Arithmetic-Expression-to-Construct-a-Value
# Question : Given an array nums of positive and negative integers and an int target. You have +, -, *, / and ()
# operators. Find out if it's possible to build an expression that evaluates to the target value. Each operator
# can only be used once. Return any solution or an empty string if it's not possible.
#
# Example : Input: nums = [1, 2, 3, 8, 4], target = 44
# Output: "(3+8)*4"
#
# Question Type : OddOne
# Used : My idea is to build a directed "almost bipartite" graph, the reason why it is not bipartite is because
#        we have braces. Basically, we have two sets of nodes: value nodes and operator node, and two special
#        nodes: ( and ).
#        Value nodes corresponds to distinct numbers in the given array, each value node connects to all operator
#        nodes +, -, *, /, and the special node ).
#        Operator nodes are +, -, *, /, each operator node connects to all non-negative value nodes, and the special
#        node (.
#        Special node ( connects to all value nodes
#        Special node ) connects to all operator nodes
#        Then, this problem becomes to "Can we find a path in this directed graph, such that it is a valid expression
#        and equals to target?"
#        Now what you can do is run DFS starting from each value node, and the special node (, backtracking with a
#        global counter to store how many times you can visit a node.
# Complexity : O(n^5)

import collections


def arithmeticExpression(inpArr, target):
    operators = ['+', '-', '*', '/']
    parenthesis = ['(', ')']
    cnt = dict()
    for operand in inpArr + parenthesis + operators:
        cnt[operand] = 1

    # build the directed graph
    graph = dict()
    inpArrSet = set(inpArr)
    positiveInpArrSet = set(x for x in inpArr if x >= 0)

    for x in inpArrSet:
        graph[x] = set('+-*/)')

    for op in '+-*/':
        graph[op] = positiveInpArrSet | {'('}

    graph['('] = inpArrSet
    graph[')'] = set('+-*/')

    ans = []

    def helper(expr, node):
        # already found an answer, just return
        if len(ans) > 0:
            return True

        # the current node cannot be visited
        if cnt[node] == 0:
            return False

        # invalid brace, ) comes before (
        if node == ')' and cnt['('] == 1:
            return False

        # update expression
        expr, value = expr + str(node), None

        # check if the expression is valid
        valid = expr[-1] == ')' or (expr[-1].isdigit() and cnt['('] == 1)

        if valid:
            try:
                # replace float division to integer division
                value = eval(expr.replace('/', '//'))
                # print(expr, value)
            except:
                # handle divide zero case like 2 / (4 - 3 - 1)
                value = None

        if value == target:
            ans.append(expr)
            return True
        else:
            cnt[node] -= 1
            for nb in graph[node]:
                # prune +-*/ zero, since it is redandant
                if node in set('+-*/') and nb == 0:
                    continue
                # prune */ 1, since it is redandant
                if node in set('*/') and nb == 1:
                    continue

                if helper(expr, nb):
                    return True
            # backtracking
            cnt[node] += 1
            return False

    for node in inpArrSet | {'('}:
        if helper('', node):
            break

    return ans[0]


if __name__ == "__main__":
    nums = [1, 2, 3, 8, 4]
    target = 44
    print(arithmeticExpression(nums, target))

    nums = [2, 3, 4, 1, 9, 2]
    target = 21
    print(arithmeticExpression(nums, target))

    nums = [-2, 2]
    target = 4
    print(arithmeticExpression(nums, target))

    nums = [-2, 2]
    target = -4
    print(arithmeticExpression(nums, target))

    nums = [-2, 1, 3]
    target = -8
    print(arithmeticExpression(nums, target))