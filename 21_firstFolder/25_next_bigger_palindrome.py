# https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/
# Question : Given a number, find the next smallest palindrome larger than this number. For example, if the
# input number is "2 3 5 4 5", the output should be "2 3 6 3 2". And if the input number is "9 9 9", the output
# should be "1 0 0 1".
#
# Question Type : Generic
# Used : If all the digits in number are 9. return 100001
#        Else call function generateNextPalindromeUtils(num).
#        In this function place i just before mid and j after mid. If n is odd, ignore mid
#        Now move i to left and j to right if the middle digits are same
#        if i < 0 or num[i] < num[j]: leftSmaller = True
#        while i >= 0 : Copy the mirror of left to right
#        if leftSmaller: set carry = 1 and i = mid - 1.
#           if there are odd digits, then increment the middle digit by carry and store the carry
#           while i >= 0: Add 1 to the rightmost digit of the left side, propagate the carry towards MSB digit and
#           simultaneously copying mirror of the left side to the right side.
#        After the function call gets over print num
# Complexity : O(m) where m is length of number


def generateNextPalindromeUtils(num):
    n = len(num)
    mid = n // 2
    leftSmaller = False
    i = mid - 1
    if n % 2 == 1:
        j = mid + 1
    else:
        j = mid

    # Initially, ignore the middle same digits
    while i >= 0 and j < n and num[i] == num[j]:
        i -= 1
        j += 1

    # Find if the middle digit(s) need to be incremented or not (or copying left side is not sufficient)
    if i < 0 or num[i] < num[j]:
        leftSmaller = True

    # Copy the mirror of left to right
    while i >= 0:
        num[j] = num[i]
        j += 1
        i -= 1

    # Handle the case where middle digit(s) must be incremented
    if leftSmaller:
        carry = 1
        i = mid - 1

        # if there are odd digits, then increment the middle digit and store the carry
        if n % 2 == 1:
            num[mid] += carry
            carry = num[mid] / 10
            num[mid] %= 10
            j = mid + 1
        else:
            j = mid

        # Add 1 to the rightmost digit of the left side, propagate the carry towards MSB digit and simultaneously
        # copying mirror of the left side to the right side.
        while i >= 0:
            num[i] += carry
            carry = num[i] / 10
            num[i] %= 10
            num[j] = num[i]
            j += 1
            i -= 1


def areAll9s(num):
    for digit in num:
        if digit != 9:
            return False
    return True


def generateNextPalindrome(num):
    if areAll9s(num):
        num = [0] * (len(num) + 1)
        num[0] = 1
        num[-1] = 1
        print(num)
    else:
        generateNextPalindromeUtils(num)
        print(num)


if __name__ == "__main__":
    num = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
    # num = [9, 9, 9, 9]
    generateNextPalindrome(num)
