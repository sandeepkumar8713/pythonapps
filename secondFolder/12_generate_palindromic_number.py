# https://www.geeksforgeeks.org/generate-palindromic-numbers-less-n/
# Question : Find all numbers less than n, which are palindromic. Numbers can be printed in any order.
#
# Used : Call createPalindrome(inp,isOdd). It would append the inp in reverse to inp itself. If isOdd that means that
#           we accepting and output of odd length. In such case, ignore the last digit doing by n = n/10, before
#           appending the reverse of it. After appending return the palindromic value.
#        We need to call createPalindrome() twice for even and odd. Call createPalindrome with input inp = 1 and keep
#           calling createPalindrome() (and doing inp++) in the loop until it returns value more than n
# Complexity : (n)


def createPalindrome(inp, isOdd):
    n = inp
    palin = inp

    # if odd then neglect the last digit of input in finding reverse as in case of odd number of digits middle element
    # occur once
    if isOdd:
        n = n / 10

    # Creates palindrome by just appending reverse of number to itself
    while n > 0:
        palin = palin * 10 + (n % 10)
        n = n / 10
    return palin


def generatePaldindromes(n):
    # Run two times for odd and even length palindromes
    for j in range(2):
        i = 1
        palindromicNum = createPalindrome(i, j % 2)
        while palindromicNum < n:
            print palindromicNum
            palindromicNum = createPalindrome(i, j % 2)
            i = i + 1


if __name__ == "__main__":
    n = 104
    generatePaldindromes(n)
