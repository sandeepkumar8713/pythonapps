# https://leetcode.com/problems/count-of-range-sum/
# Question : Given an integer array nums and two integers lower and upper,return the number of
# range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of
# the elements in nums between indices i and j inclusive, where i <= j.
#
# Example : Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
#
# Question Type : ShouldSee
# Used : Make a cumulative array from the given nums array.
#        Do merge sort on cummArray. While doing merge, find range which satisfies the
#        lower and upper constraint. Keep track of length of such range and sum them.
#        Return sum after completing mergesort
#        Logic :
#        mergesort(cumArray, output, left, right, lower, upper):
#        mid = (left + right) // 2
#        left_arr = mergesort(cumArray, output, left, mid, lower, upper)
#        right_arr = mergesort(cumArray, output, mid + 1, right, lower, upper)
#        sorted_arr = []
#        i, j, k = 0, 0, 0
#        for prefix_left in left_arr:
#           while j < len(right_arr) and right_arr[j] - prefix_left <= upper:
#               j += 1
#           while i < len(right_arr) and right_arr[i] - prefix_left < lower:
#               i += 1
#           while k < len(right_arr) and right_arr[k] < prefix_left:
#               sorted_arr.append(right_arr[k])
#               k += 1
#           sorted_arr.append(prefix_left)
#           output[0] += j - i
#        sorted_arr += right_arr[k:]
#        return sorted_arr
# Complexity : O(n log n)


def mergesort(cumArray, output, left, right, lower, upper):
    if left == right:
        if lower <= cumArray[left] <= upper:
            output[0] += 1
        return [cumArray[left]]

    mid = (left + right) // 2
    left_arr = mergesort(cumArray, output, left, mid, lower, upper)
    right_arr = mergesort(cumArray, output, mid + 1, right, lower, upper)

    sorted_arr = []
    i, j, k = 0, 0, 0

    for prefix_left in left_arr:
        # Checking range sum b/w prefix_left and right_arr[j] is less than upper
        while j < len(right_arr) and right_arr[j] - prefix_left <= upper:
            j += 1

        # Checking range sum b/w prefix_left and right_arr[i] is higher than lower
        while i < len(right_arr) and right_arr[i] - prefix_left < lower:
            i += 1

        # Actual merge is happening here
        # if right_arr is less than prefix_left, add them to sorted_array.
        while k < len(right_arr) and right_arr[k] < prefix_left:
            sorted_arr.append(right_arr[k])
            k += 1

        # Add prefix left to sorted array
        sorted_arr.append(prefix_left)
        # This gives the range count which satisfies the lower and upper constraint
        output[0] += j - i

    sorted_arr += right_arr[k:]
    return sorted_arr


def countRangeSum(nums, lower, upper):
    cummArray = []
    cur = 0
    for n in nums:
        cur += n
        cummArray.append(cur)

    output = [0]
    mergesort(cummArray, output, 0, len(cummArray) - 1, lower, upper)

    return output[0]


if __name__ == "__main__":
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(countRangeSum(nums, lower, upper))
