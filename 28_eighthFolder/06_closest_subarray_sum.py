# https://www.geeksforgeeks.org/subarray-whose-sum-is-closest-to-k/
# Question : Given an array of positive and negative integers and an integer K. The task is
# to find the subarray which has its sum closest to k. In case of multiple answers,
# print anyone. Closest here means abs(sum-k) should be minimal.
#
# Input: a = [-5, 12, -3, 4, -15, 6, 1 ], K = 2
# Output: 1
# The subarray [-3, 4] or [1] has sum = 1 which is the closest to K.
#
# Question Type : Asked
# Used : Sort the given array
#        Use two pointers, start and end set at 0.
#        If sum is less than target, increment start.
#        If sum is more than target, increment end.
#        Maintain min diff : abs(curr_sum - k)
# Complexity : O(n log n)


def subarray_closest_sum(arr, k):
    n = len(arr)
    # Initialize start and end pointers, current sum, and minimum difference
    start = 0
    end = 0
    arr_1 = sorted(arr)
    curr_sum = arr_1[0]
    min_diff = float('inf')
    # Initialize the minimum difference between the subarray sum and K
    min_diff = abs(curr_sum - k)

    closest_sum = curr_sum
    # Traverse through the array
    while end < n - 1 and start < n - 1:
        # If the current sum is less than K, move the end pointer to the right
        if curr_sum < k:
            end += 1
            curr_sum += arr_1[end]
        # If the current sum is greater than or equal to K, move the start pointer to the right
        else:
            curr_sum -= arr_1[start]
            start += 1

        # Update the minimum difference between the subarray sum and K
        if abs(curr_sum - k) < min_diff:
            min_diff = abs(curr_sum - k)
            closest_sum = curr_sum

    return closest_sum


if __name__ == "__main__":
    arr = [-5, 12, -3, 4, -15, 6, 1]
    k = 2
    print(subarray_closest_sum(arr, k))

    arr = [-46, 44, -90]
    k = -90
    print(subarray_closest_sum(arr, k))
