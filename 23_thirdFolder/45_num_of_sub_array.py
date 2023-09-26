# https://leetcode.com/discuss/interview-question/406148/Google-or-Phone-Screen-or-Number-of-Subarrays-That-Satisfy-Condition
# Question : Given an array A that is a permutation of n numbers [1-n]. Find the number
# of subarrarys S that meets the following condition max(S) - min(S) = length(S) - 1.
#
# Example : Input: [4, 3, 1, 2, 5]
# Output: 10
# Explanation: Sub arrays that meets the condition are
# [4], [3], [1], [2], [5], [4 3], [1 2]
# [3 1 2], [4 3 1 2], [4 3 1 2 5]
#
# Question Type : Generic
# Used : A few important observations:
#        Since the input array is a permutation from 1 to n, each number will only appear once.
#        For the sub sequence that meets this condition max(S) - min(S) = length(S) - 1, it will also have
#        to be a permutation.
#        Any sequence with a single number will meet the condition.
#        With these, the problem can be solved with divide and conquer. We break it into two sub problems:
#        Given an array, find results including the first number. This should be trivial O(N).
#        Given an array, find results without the first number. For this, we will break the rest of the numbers
#        into parts.
#        Each sub sequence will either be all bigger than the first number or be all smaller than the first
#        number. Otherwise, it won't be a result based on the 2nd observation above.
# Logic: def permutation_sequence(inpArr):
#        if len(inpArr) == 0: return 0
#        if len(inpArr) == 1: return 1
#        result = 1
#        min_s = inpArr[0]
#        max_s = inpArr[0]
#        count = 0
#        for i in range(1, len(inpArr)):
#           min_s = min(inpArr[i], min_s)
#           max_s = max(inpArr[i], max_s)
#           if max_s - min_s == i:
#               result += 1
#               count += 1
#        if count == len(inpArr):
#           result += len(inpArr) * (len(inpArr) - 1) / 2
#           return result
#        sub_array = []
#        for i in range(1, len(inpArr)):
#           if len(sub_array) != 0 and (sub_array[0] > inpArr[0]) != (inpArr[i] > inpArr[0]):
#               result += permutation_sequence(sub_array)
#               sub_array = []
#           sub_array.append(inpArr[i])
#        return result + permutation_sequence(sub_array)
# Complexity : O(n log n)


def permutation_sequence(inpArr):
    if len(inpArr) == 0:
        return 0
    if len(inpArr) == 1:
        return 1

    result = 1

    # Assume that we will keep the first number
    min_s = inpArr[0]
    max_s = inpArr[0]
    count = 0
    for i in range(1, len(inpArr)):
        min_s = min(inpArr[i], min_s)
        max_s = max(inpArr[i], max_s)
        if max_s - min_s == i:
            result += 1
            count += 1

    if count == len(inpArr):
        result += len(inpArr) * (len(inpArr) - 1) / 2
        return result

    # Assume that we don't keep the first number
    sub_array = []
    for i in range(1, len(inpArr)):
        if len(sub_array) != 0 and (sub_array[0] > inpArr[0]) != (inpArr[i] > inpArr[0]):
            result += permutation_sequence(sub_array)
            sub_array = []
        sub_array.append(inpArr[i])

    return result + permutation_sequence(sub_array)


if __name__ == "__main__":
    print(permutation_sequence([4, 3, 1, 2, 5]))  # output 10
