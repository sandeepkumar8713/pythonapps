# https://leetcode.com/problems/different-ways-to-add-parentheses/
# https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/414110/Clean-Python-Solution-(Divide-and-Conquer)
# https://leetcode.com/playground/9WPVeH84
# Question : Given a string of numbers and operators, return all possible results from computing all the different
# possible ways to group numbers and operators. The valid operators are +, - and *.
# Given an array of n integers, return the result of all possible equations you can generate by adding the following
# operators in-between the numbers: +, -, *, /, () (for prioritization).
#
# Question Type : Generic
# Used : We will use divide and conquer. For every operator, divide in into left and right sub expression. Solve them
#        first by calling the function again. It will return a list of possible results. Now use the earlier found
#        operator in combination of all the possible results.
# Logic: def calculate(operator, n1, n2):
#        if operator=="+": return n1+n2
#        elif operator=='-': return n1-n2
#        elif operator=='*': return n1*n2
#        elif operator == '/':
#           if n2 != 0: return n1 * n2
#        else: return None
#        def diffWaysToCompute(S):
#        if S.isdigit(): return [int(S)]
#        opt = []
#        for i in xrange(len(S)):
#           if S[i]=='+' or S[i]=='-' or S[i]=='*' or S[i]=='/':
#               left = diffWaysToCompute(S[:i])
#               right = diffWaysToCompute(S[i+1:])
#               for n1 in left:
#                   for n2 in right:
#                       res = calculate(S[i], n1, n2)
#                       if res is not None:
#                           opt.append(res)
#        return opt
# Complexity : O(n log n)


def calculate(operator, n1, n2):
    if operator=="+":
        return n1+n2
    elif operator=='-':
        return n1-n2
    elif operator=='*':
        return n1*n2
    elif operator == '/':
        if n2 != 0:
            return n1 * n2
    else:
        return None


def diffWaysToCompute(S):
    if S.isdigit(): return [int(S)]

    opt = []
    for i in range(len(S)):
        # For second question, skip this check, run for all possible operators.
        if S[i]=='+' or S[i]=='-' or S[i]=='*' or S[i]=='/':
            left = diffWaysToCompute(S[:i])
            right = diffWaysToCompute(S[i+1:])
            for n1 in left:
                for n2 in right:
                    res = calculate(S[i], n1, n2)
                    if res is not None:
                        opt.append(res)
    return opt


if __name__ == "__main__":
    inpStr = "2-1-1"
    print(diffWaysToCompute(inpStr))

    inpStr = "2*3-4*5"
    print(diffWaysToCompute(inpStr))
