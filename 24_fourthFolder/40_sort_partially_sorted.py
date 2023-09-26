# https://leetcode.com/discuss/interview-question/378774/
# Question : Given an array of positive integers (possibly with duplicates) such that the numbers
# have been sorted only by 28 most significant bits. Sort the array completely.
#
# Example : Input: [0, 15, 12, 17, 18, 19, 33, 32]
# Output: [0, 12, 15, 17, 18, 19, 32, 33]
#
# Question Type : ShouldSee
# Used : Used bucket sort. Since the array is already sorted, we can just move from left to right
#        as long as the first 28 bits are the same. Once we enter a different 28 bit set,
#        we can dump what we have in our 16 buckets into the result and reset.
# Logic: sortPartialSorted28B(inpArr):
#        mask = ~0 << 4
#        curr_28b = inpArr[0] & mask (first 28bits)
#        buckets = [0] * 16 , results = list()
#        for num in inpArr:
#           if (num & mask) != curr_28b: # start sort
#               for bucket, occurrence in enumerate(buckets):
#                   for i in range(occurrence): results.append(curr_28b | bucket)
#               curr_28b = num & mask  # set to next 28 bit group
#               buckets = [0] * 16
#           buckets[num & 15] += 1
# Complexity : O(n)


def sortPartialSorted28B(inpArr):
    if len(inpArr) == 0:
        return inpArr

    mask = ~0 << 4
    curr_28b = inpArr[0] & mask
    buckets = [0] * 16  # 16 buckets -> n occurrence
    results = list()

    for num in inpArr:
        if (num & mask) != curr_28b:    # start sort
            for bucket, occurrence in enumerate(buckets):
                for i in range(occurrence):
                    results.append(curr_28b | bucket)

            curr_28b = num & mask  # set to next 28 bit group
            buckets = [0] * 16     # reset
        # add to buckets
        buckets[num & 15] += 1

    for bucket, occurrence in enumerate(buckets):
        for i in range(occurrence):
            results.append(curr_28b | bucket)

    return results


if __name__ == "__main__":
    nums = [0, 15, 12, 17, 18, 19, 33, 32]
    print(sortPartialSorted28B(nums))
