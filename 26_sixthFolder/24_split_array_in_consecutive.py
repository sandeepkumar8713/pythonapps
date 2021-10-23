# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Question : You are given an integer array nums that is sorted in non-decreasing order.
# Determine if it is possible to split nums into one or more subsequences such that both of
# the following conditions are true:
# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more
# than the previous integer). All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.
#
# Example : Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
#
# Question Type : ShouldSee
# Used : To make the partition possible, freq[i] must be higher than all previous freq
#        Make a freq_dict and loop over it.
#        if freq[i] == 0; inc i and continue
#        For each freq[i], check if all the freq[i+1...n] ahead are higher and
#        decrement freq count. While doing so keep the counter updated.
#        if for freq[i], count < 3, return False
#        After the loop, return False
#        Logic :
#        start, end = min(freq_dict.keys()), max(freq_dict.keys())
#        while i < end + 1:
#           if freq_dict[i] == 0:
#               i += 1; continue
#           max_freq = freq_dict[i]
#           j = i; count = 0
#           while j < end + 1 and freq_dict[j] >= max_freq:
#               max_freq = max(freq_dict[j], max_freq)
#               freq_dict[j] -= 1
#               j += 1; count += 1
#           if count < 3: return False
#        return True
# Complexity : O(k^2) where k is number of unique numbers in array


def isPossible(inpArr):
    freq_dict = {}
    for ele in inpArr:
        freq_dict[ele] = freq_dict.get(ele, 0) + 1

    start = min(freq_dict.keys())
    end = max(freq_dict.keys())

    i = start
    while i < end + 1:
        if freq_dict[i] == 0:
            i += 1
            continue

        # current frequency should >= previous
        max_freq = freq_dict[i]
        j = i
        count = 0
        while j < end + 1 and freq_dict[j] >= max_freq:
            max_freq = max(freq_dict[j], max_freq)
            freq_dict[j] -= 1
            j += 1
            count += 1

        if count < 3:
            return False

    return True


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 4, 5, 5]
    print (isPossible(nums))

    nums = [1, 2, 3, 3, 4, 4, 4, 5, 5]
    print(isPossible(nums))