# https://www.geeksforgeeks.org/generate-bitonic-sequence-of-length-n-from-integers-in-a-given-range/
# Similar : 21_firstFolder/01_produce_inc_dec_pattern
# Question : Given integers N, L and R, the task is to generate a Bitonic Sequence of length N from the integers
# in the range [L, R] such that the first element is the maximum. If it is not possible to create such a sequence,
# then print “-1”. A Bitonic Sequence is a sequence that must be strictly increasing at first and then
# strictly decreasing.
#
# Question Type : ShouldSee, SimilarAdded
# Used : Here we are trying to add upper to lower in right side and upper to lower in left side in reverse.
#        If twice the difference of upper and lower plus 1 is less than N, than sequence is not possible.
#        bitonicSequence(num, lower, upper):
#        if num > (upper - lower) * 2 + 1:
#           print(-1)
#           return
#        ans = [], rng = min(upper - lower + 1, num - 1)
#        for i in range(rng):
#           ans.append(upper - i)
#        for i in range(num - len(ans)):
#           ans.insert(0, upper - i - 1)
#        return ans
# Complexity : O(n)

def bitonicSequence(num, lower, upper):
    # If sequence is not possible
    if num > (upper - lower) * 2 + 1:
        print(-1)
        return

    ans = []

    rng = min(upper - lower + 1, num - 1)
    for i in range(rng):
        ans.append(upper - i)

    # If size of deque < n
    for i in range(num - len(ans)):
        # Add elements from start
        ans.insert(0, upper - i - 1)

    # Print the stored in the list
    print(ans)


if __name__ == '__main__':
    N = 5
    L = 3
    R = 10

    bitonicSequence(N, L, R)
