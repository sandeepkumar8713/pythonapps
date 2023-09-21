# Find if all the chars in str_to_match is available on chars_list
# Number of occurrences also needs to be considered.
#
# Condition :
# 1. Every character in str_to_match should be in chars_list
# 2. No. of Occurrence also should match
# 3. chars_list can have more chars other than str_to_match
#
# Example1 :
# chars_list = 'H, F, B, A, C, L, K, G, V, C, B, I, U, K, F'
# str_to_match = 'BLACKBUCK'
#
# OUTPUT:
# Yes
#
# Explaination1:
# There should atleast be 2 B's, 2C's and 2 K's in chars_list because BLACKBUCK has recurring chars
#
# Example 2 :
# chars_list = 'H, F, U, D, Y, B, F'
# str_to_match = 'BUDDY'
#
# OUTPUT:
# NO
#
# Explaination2:
# all characters are present but only one D is present in chars_list
#
# """
#
# chars_list = 'H, F, B, A, C, L, K, G, V, C, B, I, U, K, F'
# str_to_match = 'BLACKBUCK'
import sys


# from collections import defaultdict
#
# def is_matching(chars_list, str_to_match):
#     char_dict = defaultdict(int)
#     chars = chars_list.split(", ")
#     for ch in chars:
#         char_dict[ch] += 1
#
#     str_dict = defaultdict(int)
#     for ch in str_to_match:
#         str_dict[ch] += 1
#
#     for key, str_value in str_dict.items():
#         if key in char_dict.keys():
#             if str_value > char_dict[key]:
#                 return "NO"
#         else:
#             return "NO"
#
#     return "YES"
#
#
# if __name__ == "__main__":
#     chars_list = 'H, F, U, D, Y, B, F'
#     str_to_match = 'BUDDY'
#     print(is_matching(chars_list, str_to_match))
#
#     chars_list = 'H, F, B, A, C, L, K, G, V, C, B, I, U, K, F, B, B, K, K'
#     str_to_match = 'BLACKBUCK'
#     print(is_matching(chars_list, str_to_match))
#
#
# #####
# # Employees, dept_emp, departments, salaries
#
#
# with cte as(
#     select
#         e.first_name,
#         s.salary,
#         e.emp_no,
#         de.dept_no,
#     from Employees as e join dept_emp as de
#         on e.emp_no == de.emp_no
#         join salaries as
#         on s.emp_no == e.emp_no
# )
#
# select dept_no, first_name, max(salary) over(partition by dept_no) from cte


# Given an unsorted integer array
# sums,
# return the
# smallest
# missing
# positive
# integer.
#
# Example
# 1:
#
# Input: nums = [1, 2, 0]
# Output: 3
# Explanation: The
# numbers in the
# range[1, 2]
# are
# all in the
# array.
# Example
# 2:
#
# Input: nums = [3, 4, -1, 1]
# Output: 2
# Explanation: 1 is in the
# array
# but
# 2 is missing.
# Example
# 3:
#
# Input: nums = [7, 8, 9, 11, 12]
# Output: 1
# Explanation: The
# smallest
# positive
# integer
# 1 is missing.

import sys

def find_missing_positive(nums):
    n = len(nums)
    i = 0

    # min_pos = sys.maxsize
    # for item in nums:
    #     if item >= 0:
    #         min_pos = min(min_pos, item)

    n = len(nums)
    i = 0
    while i < n:
        c = nums[i] - 1
        if nums[i] > 0 and c < n:
            if nums[i] != nums[c]:
                nums[c], nums[i] = nums[i], nums[c]
                continue
        i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    # nums = [7, 8, 9, 11, 12]
    # print(find_missing_positive(nums))
    #
    # nums = [1, 2, 0]
    # print(find_missing_positive(nums))
    # #
    # nums = [3, 4, -1, 1]
    # print(find_missing_positive(nums))
    item_list = [1, 2, 4, 10]
    x = [item for item in item_list if item > 5]
    y = [item if item > 5 else -1 for item in item_list]
    print (x)
    print (y)
