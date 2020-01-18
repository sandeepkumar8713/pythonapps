# CTCI : Q16_24_Pairs_With_Sum
# Similar : https://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
# https://www.geeksforgeeks.org/count-pairs-with-given-sum/
# Question : Given an array of integers, and a number 'sum', find the number of pairs of integers in the array
# whose sum is equal to 'sum'.
# 
# Input  :  arr[] = {1, 5, 7, -1},
#           sum = 6
# Output :  2
#
# Used : map, subtract each value from sum and see if it is present
# Complexity : O(n)


def getPairsCount(arr,sum):
    map = dict()
    for i in range(0, len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    twice_count = 0
    for i in range(0, len(arr)):
        if sum-arr[i] in map:
            print arr[i], sum-arr[i]
            twice_count += map[sum-arr[i]]
        # ignore same value
        if sum-arr[i] == arr[i]:
            twice_count -= 1

    # divide since every pair is counted two times
    return twice_count/2


if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    sum = 6

    # arr = [1, 4, 45, 6, 10, -8]
    # sum = 16
    print ('count = %s' % getPairsCount(arr, sum))
