# CTCI Q1_01_Is_Unique
# Question : Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
#
# Input: str = "abcde"
# Output: true
#
# Question Type : Easy
# Used : Take checker = 0, loop over each char: left shift 1 by the ascii value of char.
#        If AND operation with checker is > 0 then return false
#        else do OR operation shifted integer with checker.
# Complexity : O(n)


def isUniqueChars(inputStr):
    if len(inputStr) > 26:  # Only 26 characters
        return False

    checker = 0
    for i in range(0, len(inputStr)):
        val = ord(inputStr[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


if __name__ == "__main__":
    words = ["abcde", "hello", "apple", "kite", "padle"]

    for word in words:
        print(word, isUniqueChars(word))
