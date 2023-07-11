# https://leetcode.com/problems/single-number-ii/description/
# Question : Given an integer array nums where every element appears three times
# except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
# Example : [2,2,2,3,4,4,4]
# binary form :- 010
# 010
# 010
# 011
# 100
# 100
# 100
# Total :- 3 4 1
# So, 3 is divisible by 3 hence "0" but four is not divisible "1" and same with "1".
# The final answer will be "011" = 3.
#
# Question Type : Generic
# Used : Loop through each bit of items in array. Count the number of occurrence of set bit for each digit.
#        The remainder of mod 3 will filter out the odd element.
# Logic : for i in range(32):
#           count = 0
#           for n in nums:
#               temp = n >> i
#               temp = temp & 1
#               count += temp
#           rem = count % 3
#           if i == 31 and rem:  # must handle the negative case
#               res -= 1 << 31
#           else:
#               res |= rem << i
#         return res
# Complexity : O(n)


def singleNumber(nums):
    res = 0
    for i in range(32):
        count = 0
        for n in nums:
            temp = n >> i
            temp = temp & 1
            count += temp
        rem = count % 3
        if i == 31 and rem:  # must handle the negative case
            res -= 1 << 31
        else:
            res |= rem << i
    return res


if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    print(singleNumber(nums))

    nums = [0, 1, 0, 1, 0, 1, 99]
    print(singleNumber(nums))
