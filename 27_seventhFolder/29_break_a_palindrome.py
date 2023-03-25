# https://leetcode.com/problems/break-a-palindrome/
# Question : Given a palindromic string of lowercase English letters palindrome,
# replace exactly one character with any lowercase English letter so that the
# resulting string is not a palindrome and that it is the lexicographically
# smallest one possible. Return the resulting string. If there is no way
# to replace a character to make it not a palindrome, return an empty string.
#
# Example : Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as
# "zbccba", "aaccba", and "abacba". Of all the ways, "aaccba" is the lexicographically smallest.
#
# Question Type : Easy
# Used : Find first non a character and put a there. If it is not in middle index
#        If we are out of loop, put b at the last index. (All are a's or can't replace in middle)
#        Logic :
#        for i in range(n):
#           if palindrome[i] != 'a' and not (n % 2 != 0 and n // 2 == i):
#               return palindrome[:i] + 'a' + palindrome[i + 1:]
#        return palindrome[:n-1] + 'b'
# Complexity : O(n)

def break_palindrome(palindrome):
    n = len(palindrome)
    if n == 1:
        return ""

    for i in range(n):
        # Find first non-a character which should not be in middle of palindrome
        if palindrome[i] != 'a' and not (n % 2 != 0 and n // 2 == i):
            return palindrome[:i] + 'a' + palindrome[i + 1:]

    # If all are a's, put b at last character
    return palindrome[:n - 1] + 'b'


if __name__ == "__main__":
    palindrome = "abccba"
    print(break_palindrome(palindrome))

    palindrome = "aaaa"
    print(break_palindrome(palindrome))

    palindrome = "aabaa"
    print(break_palindrome(palindrome))
