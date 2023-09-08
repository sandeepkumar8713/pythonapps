# https://leetcode.com/problems/sliding-window-maximum/
# Question : You are given an array of integers nums, there is a sliding window of size k which
# is moving from the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example : Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
#
# Question : Asked
# Used : Sliding window
#        We will try to maintain a max queue, it should be sorted in descending order.
#        While inserting in the max queue, we should keep popping lesser values.
# Logic: for i in range(len(nums)):
#           left = i - k
#           if len(max_q_index) > 0 and max_q_index[0] == left:
#               max_q_index.pop(0)
#           while len(max_q_index) > 0 and nums[max_q_index[-1]] < nums[i]:
#               max_q_index.pop(-1)
#           max_q_index.append(i)
#           if i >= k - 1:
#               top_ele = nums[max_q_index[0]]
#               ans.append(top_ele)
#        return ans
# Complexity : O(n * k)
# Using Binary search will give O(n * log k)

def print_max_q(nums, max_q_index):
    res = [nums[index] for index in max_q_index]
    print(res)


def binary_search(max_q_index, nums, target):
    res = [nums[index] for index in max_q_index]
    left = 0
    right = len(res)
    cut = 0
    while left < right:
        mid = left + (right - left) // 2
        if res[mid] < target:
            cut = mid
            right = mid - 1
        else:
            left = mid + 1
    return cut


def get_max_window(nums, k):
    max_q_index = []
    ans = []
    for i in range(len(nums)):
        # print_max_q(nums, max_q_index)
        left = i - k
        if len(max_q_index) > 0 and max_q_index[0] == left:
            max_q_index.pop(0)

        # Since we are removing lesser previous values before inserting current value,
        # we only need to check if top of queue when removing left index value.
        # [1, 3, 5, 2] k = 3
        # For above input we will never have [5, 3, 2] in max_q_index
        while len(max_q_index) > 0 and nums[max_q_index[-1]] < nums[i]:
            max_q_index.pop(-1)

        max_q_index.append(i)
        if i >= k - 1:
            top_ele = nums[max_q_index[0]]
            ans.append(top_ele)

    return ans


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(get_max_window(nums, k))

    nums = [1, 3, 5, 2, 1, -1]
    k = 3
    print(get_max_window(nums, k))
