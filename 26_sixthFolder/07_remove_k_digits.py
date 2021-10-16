# https://leetcode.com/problems/remove-k-digits/
# Question : Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
#
# Example : Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#
# Question Type : ShouldSee
# Used : Run a loop k times.
#           Run loop on digits array.
#               if we find a ele which is greater than right, remove it and break
#               else remove the last ele of array
#           Remove leading 0, if any from digits array
#           If digits array is empty return 0.
#        After k loop, return digit array.
#        Logic :
#        for i in range(k):
#           for i in range(len(digits)):
#               if (i == len(digits) - 1) or (int(digits[i]) > int(digits[i + 1])):
#                   digits.pop(i); break
#           while digits and (int(digits[0]) == 0):
#               digits.pop(0)
#           if len(digits) == 0: return "0"
#        return "".join(digits)
# Complexity : O(n * k) where n in number of digits


def removeKdigits(num, k):
    digits = list(num)

    for i in range(k):
        # remove first non-monotonic upward digit.
        for i in range(len(digits)):
            # remove last digit or remove the digit which is higher than right side digit
            if (i == len(digits) - 1) or (int(digits[i]) > int(digits[i + 1])):
                digits.pop(i)
                break

        while digits and (int(digits[0]) == 0):
            digits.pop(0)

        if len(digits) == 0:
            return "0"

    return "".join(digits)


if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(removeKdigits(num, k))

    num = "10200"
    k = 1
    print(removeKdigits(num, k))

    num = "10"
    k = 2
    print(removeKdigits(num, k))
