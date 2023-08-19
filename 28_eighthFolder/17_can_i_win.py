# https://leetcode.com/problems/can-i-win/
# Question : In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10.
# The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without
# replacement until they reach a total >= 100.
# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can
# force a win, otherwise, return false. Assume both players play optimally.
#
# Example : Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation: No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
#
# Question Type : Generic
# Used : Dp with DFS
# Logic : def dfs(dp, desired_total, bit_vector):
#         if desired_total <= 0: return False
#         if bit_vector in dp.keys(): return dp.get(bit_vector)
#         allowed_numbers = binary_to_numbers(bit_vector)
#         for num in allowed_numbers:
#           if dfs(dp, desired_total - num, bit_vector & (~(1 << num))) is False:
#               dp[bit_vector] = True
#               return True
#         dp[bit_vector] = False
#         return False
# Complexity : O(2^max_choosable_integer)

def binary_to_numbers(bit_vector):
    # 6 = '0b110'
    binary_rep = bin(bit_vector)[2:]
    count = 0
    result = []
    for item in binary_rep[::-1]:
        if item == '1':
            result.append(count)
        count += 1
    return result


def dfs(dp, desired_total, bit_vector):
    if desired_total <= 0:
        return False

    if bit_vector in dp.keys():
        return dp.get(bit_vector)

    allowed_numbers = binary_to_numbers(bit_vector)
    for num in allowed_numbers:
        if dfs(dp, desired_total - num, bit_vector & (~(1 << num))) is False:
            dp[bit_vector] = True
            return True

    dp[bit_vector] = False
    return False


def can_i_win(max_choosable_integer, desired_total):
    allowed_integers = {i for i in range(1, max_choosable_integer + 1)}

    bit_vector = 0
    for i in range(1, max_choosable_integer + 1):
        bit_vector |= 1 << i

    current_total = 0
    dp = dict()

    if desired_total == 0:
        return True
    if sum(allowed_integers) < desired_total:
        return False

    return dfs(dp, desired_total, bit_vector)


if __name__ == "__main__":
    max_choosable_integer = 10
    desired_total = 11
    print(can_i_win(max_choosable_integer, desired_total))

    max_choosable_integer = 10
    desired_total = 1
    print(can_i_win(max_choosable_integer, desired_total))

    max_choosable_integer = 18
    desired_total = 79
    print(can_i_win(max_choosable_integer, desired_total))
