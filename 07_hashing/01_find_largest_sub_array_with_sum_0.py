# Question : Given an array having both positive an negative integers . Your task is to
# complete the function maxLen which returns the length of maximum sub array with 0 sum.
#
# Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
# Output: 5
# The largest sub array with 0 sum is -2, 2, -8, 1, 7
#
# Question Type : Generic
# Used : The idea is to iterate through the array and for every element arr[i], calculate
#        sum of elements form 0 to i. If the current sum has been seen before, then there
#        is a zero sum array. Hashing is used to store the sum values, so that we can
#        quickly store sum and find out whether the current sum is seen before or not.
# Complexity : O(n)


def maxLen(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if arr[i] is 0 and max_len is 0:
            max_len = 1
        if curr_sum is 0:
            max_len = i + 1
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i

    return max_len


if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 13]
    print("Length of the longest 0 sum sub array is %d" % maxLen(arr))
