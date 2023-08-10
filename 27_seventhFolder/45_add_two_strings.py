# https://leetcode.com/problems/add-strings/
# Question : Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large
# integers (such as BigInteger). You must also not convert the inputs to integers directly.
#
# Question Type : Easy
# Used : Find the bigger input and keep track of it.
#        Run a loop in reveres on both the input arrays.
#           Add the elements, take care of carry.
#           Save the sum in result array.
#        Check if bigger array has elements left, add them as well using the carry.
#        If carry is more than 1 add in the result array.
#        Now reverse the result array, join them to return it.
# Logic : i = m - 1, j = n - 1
#         result = [], carry = 0
#         while i >= 0 and j >= 0:
#           ele_1 = bigger[i], ele_2 = smaller[j]
#           res_ele = charToNum(ele_1) + charToNum(ele_2) + carry
#           result.append(NumToChar(res_ele % 10))
#           carry = res_ele // 10
#           i -= 1, j -= 1
#         while i >= 0:
#           ele_1 = bigger[i]
#           res_ele = charToNum(ele_1) + carry
#           result.append(NumToChar(res_ele % 10))
#           carry = res_ele // 10
#           i -= 1
#         if carry > 0:
#           result.append(NumToChar(carry))
#         result.reverse()
#         return "".join(result)
# Complexity : O(n)

def charToNum(ch):
    return ord(ch) - ord('0')


def NumToChar(i):
    return chr(i + ord('0'))


def add(num1, num2):
    m = len(num1)
    n = len(num2)

    if m >= n:
        bigger = num1
        smaller = num2
    else:
        bigger = num2
        smaller = num1
        m, n = n, m

    i = m - 1
    j = n - 1
    result = []
    carry = 0
    while i >= 0 and j >= 0:
        ele_1 = bigger[i]
        ele_2 = smaller[j]

        res_ele = charToNum(ele_1) + charToNum(ele_2) + carry
        result.append(NumToChar(res_ele % 10))
        carry = res_ele // 10

        i -= 1
        j -= 1

    while i >= 0:
        ele_1 = bigger[i]

        res_ele = charToNum(ele_1) + carry
        result.append(NumToChar(res_ele % 10))
        carry = res_ele // 10

        i -= 1

    if carry > 0:
        result.append(NumToChar(carry))

    result.reverse()
    return "".join(result)


if __name__ == "__main__":
    num1 = "11"
    num2 = "123"
    print(add(num1, num2))

    num1 = "0"
    num2 = "0"
    print(add(num1, num2))

    num1 = "1"
    num2 = "9"
    print(add(num1, num2))
