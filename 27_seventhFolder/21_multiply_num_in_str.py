# https://leetcode.com/problems/multiply-strings/
# Qeustion : Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
# Question Type : Asked
# Used : Reverse the two strings.
#        Run 2 loops to iterate over the elements. The sum of indexes will index in result array where
#        multiplied digit.
#        needs to be placed. Also take care of carry.
#        After the loop, reverse the ans array and return.
# Logic: first_no = num1[::-1]
#        second_no = num2[::-1]
#        answer = [0] * (len(first_no) + len(second_no))
#        for i2, digit2 in enumerate(second_no):
#           for i1, digit1 in enumerate(first_no):
#               num_zeroes = i1 + i2
#               carry = answer[num_zeroes]
#               multiplication = (ord(digit1) - ord("0")) * (ord(digit2) - ord("0")) + carry
#               answer[num_zeroes] = multiplication % 10
#               answer[num_zeroes + 1] += multiplication // 10
#        if answer[-1] == 0: answer.pop()
#        return "".join(str(digits) for digits in reversed(answer))
# Complexity : O(m*n) where m and n are len of two array


def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    first_no = num1[::-1]
    second_no = num2[::-1]

    answer = [0] * (len(first_no) + len(second_no))

    for i2, digit2 in enumerate(second_no):
        for i1, digit1 in enumerate(first_no):
            num_zeroes = i1 + i2
            carry = answer[num_zeroes]
            multiplication = (ord(digit1) - ord("0")) * (ord(digit2) - ord("0")) + carry
            answer[num_zeroes] = multiplication % 10
            answer[num_zeroes + 1] += multiplication // 10

    if answer[-1] == 0:
        answer.pop()

    return "".join(str(digits) for digits in reversed(answer))


if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    print(multiply(num1, num2))
