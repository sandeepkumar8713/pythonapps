# https://leetcode.com/problems/integer-break/
# Question : Given an integer n, break it into the sum of k positive integers, where k >= 2,
# and maximize the product of those integers. Return the maximum product you can get.
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
# n = 1 => we get max value only when we divide 1 into 0 and 1
# n = 2 => we get max value only when we divide 2 into 1 and 1
# n = 3 => we get max value only when we divide 3 into 1 and 2
# n = 4 => we get max value only when we divide 4 into 2 and 2
# n = 5 => we get max value only when we divide 5 into 2 and 3
# n = 6 => we get max value only when we divide 6 into 3 and 3
# n = 7 => we get max value only when we divide 7 into 4 and 3
# n = 8 => we get max value only when we divide 8 into 2, 3 and 3
# n = 9 => we get max value only when we divide 9 into 3, 3 and 3
# n = 10 => we get max value only when we divide 10 into 4, 3 and 3
#
# Question Type : Easy
# Used : As seen from the above pattern. Value above 4, should be multiplied by 3
# Logic : def find_max_product(n):
#         if n == 2 or n == 3: return n - 1
#         result = 1
#         while n > 4:
#           n -= 3
#           result *= 3
#         return result * n
# Complexity : O(n)

def find_max_product(n):
    if n == 2 or n == 3:
        return n - 1
    result = 1
    while n > 4:
        n -= 3
        result *= 3

    return result * n


if __name__ == "__main__":
    n = 10
    print(find_max_product(n))
