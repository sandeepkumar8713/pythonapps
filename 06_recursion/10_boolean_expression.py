# CTCI : Q8_14_Boolean_Evaluation
# https://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/
# Question : Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
# (AND), I (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
# count the number of ways of parenthesizing the expression such that it evaluates to result.
# The expression should be fully parenthesized (e.g.,(0)^(1)) but not extraneously (e.g.,(((0))^(1))).
#
# Example :
# countEval("1^0|0|1", False) -> 2
# countEval("0&0&0&1^1|0", True)-> 10
#
# Question Type : ShouldSee
# Used : Call recursive function : countEval(exp, result)
#        if len(exp) == 0: return 0
#        if len(exp) == 1) return stringToBool(exp) == result ? 1 : 0
#        Loop over each operator in exp:
#           operator = exp[i]
#           leftOperand = exp[0:i]
#           rightOperand = exp[i+1:]
#           Now call countEval() on left and right operand with both true and false result
#           Depending on operator and result, calculate subway based on combination of
#           leftTrue, leftFalse, rightTrue and rightFalse
#           way += subWay
#        return way
#        Note : No. of parenthesis combination Catalan(n) where n is no. of operator. We can use
#        hash map to save substring result.
# Complexity : O(5^n) n is no. of operator and each function calls recur calls 4 times

resultMap = {}
count = 0


def stringToBool(c):
    if c == "1":
        return True
    else:
        return False


def countEval(exp, result):
    global resultMap, count
    count += 1
    if len(exp) == 0: return 0
    if len(exp) == 1:
        if stringToBool(exp) == result:
            return 1
        else:
            return 0

    if exp + str(result) in resultMap.keys():
         return resultMap[exp + str(result)]

    ways = 0

    for i in range(1, len(exp), 2):
        operator = exp[i]
        leftOperand = exp[0:i]
        rightOperand = exp[i+1:]

        leftTrue = countEval(leftOperand, True)
        leftFalse = countEval(leftOperand, False)
        rightTrue = countEval(rightOperand, True)
        rightFalse = countEval(rightOperand, False)

        subways = 0

        if operator == '^':  # required: one true and one false
            if result:
                subWays = leftTrue * rightFalse + leftFalse * rightTrue
            else:
                subWays = leftTrue * rightTrue + leftFalse * rightFalse
        elif operator == '&':  # required: both true
            if result:
                subWays = leftTrue * rightTrue
            else:
                subWays = leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
        elif operator == '|':  # required: anything but both false
            if result:
                subWays = leftTrue * rightFalse + leftFalse * rightTrue + leftTrue * rightTrue
            else:
                subWays = leftFalse * rightFalse
        ways += subWays

    resultMap[exp + str(result)] = ways
    return ways


if __name__ == "__main__":
    expression = "0&0&0&1^1|0"  # True
    # expression = "0&0&0&0&0&0&0&0&0"  # False
    # expression = "1^0|0|1"    # False
    result = True
    print(countEval(expression, result))
    # print (count)
