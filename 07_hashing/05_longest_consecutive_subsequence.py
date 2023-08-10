# https://leetcode.com/problems/longest-consecutive-sequence/
# Question : Given an array of integers, find the length of the longest sub-sequence such
# that elements in the sub sequence are consecutive integers, the consecutive numbers
# can be in any order.
#
# Input: arr[] = {1, 9, 3, 10, 4, 20, 2};
# Output: 4
# The sub sequence 1, 3, 4, 2 is the longest sub sequence of consecutive elements
#
# Question Type : ShouldSee
# Used : Loop over the elements and add it to the set. So it will have unique values.
#        Loop over the elements, if its previous element arr[i] - 1 is not present in
#        set, then this might be the first element in our desired sub sequence. Now
#        keep incrementing this element j and keep checking if incremented value is
#        in set.
#        Once the loop gets over. Compare max value with j - arr[i] and update accordingly.
# Logic: findLongestConseqSubseq(arr):
#        for i in range(len(arr)):
#           if (arr[i] - 1) not in s:
#               j = arr[i]
#               while j in s:
#                   j += 1
#               ans = max(ans, j - arr[i])
#        return ans
# Complexity : O(n)


def findLongestConseqSubseq(arr):
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)

    for i in range(len(arr)):
        # If current element is the starting element of a sequence
        if (arr[i] - 1) not in s:
            # Then check for next elements in the sequence
            j = arr[i]
            while j in s:
                j += 1

            ans = max(ans, j - arr[i])
    return ans


if __name__ == '__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    # arr = [1, 3, 5, 7, 9, 11, 13]
    print("Length of the Longest contiguous sub sequence is ", findLongestConseqSubseq(arr))
