# https://leetcode.com/discuss/interview-question/349612
# Question : Given an integer array nums containing positive elements and an int maxValue.
# Find the value of x such that the sum of the elements of the array is maximum and is less
# than the given maxValue. x is defined as: if the current value is greater than x,
# then x is used as the new value, otherwise keep the original value
# nums[i] = min(x, nums[i]).
#
# Example : Input: nums = [10, 5, 20, 30], maxValue = 40
# Output: 12
# Explanation:
# If x = 10, the array would be nums = [10, 5, 10, 10] and the sum of the array elements would be 35.
# If x = 12, the array would be nums = [10, 5, 12, 12] and the sum of the elements would be 39 which is the
# maximum sum close to given maxValue which is 40.
# So the answer would be 12.
#
# Question Type : ShouldSee
# Used : Find min and max of input array.
#        Do binary search in this range, see mid which satisfy the condition.
#        Logic : def max_value(nums, val):
#        l = min(nums), r = max(nums)+1
#        while l < r:
#           mid = l + (r - l) // 2
#           total = 0
#           for n in nums:
#               total += min(n, mid)
#           if total == val:
#               return mid
#           elif total < val:
#               l = mid + 1
#           else:
#               r = mid
#        return mid
# Complexity : O(n log n)


def max_value(nums, val):
    l = min(nums)
    r = max(nums)+1

    while l < r:
        mid = l + (r - l) // 2
        total = 0
        for n in nums: # O(N)
            total += min(n, mid)

        if total == val:
            return mid
        elif total < val:
            l = mid + 1
        else:
            r = mid
    return mid


if __name__ == "__main__":
    print(max_value([10, 5, 20, 30], 40),"shoud be 12")
    print(max_value([100, 200, 300, 400], 800),"shoud be 250")
