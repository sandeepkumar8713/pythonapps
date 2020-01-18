# https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
# Question : Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from
# array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary
# representations of x and y. For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7
# is 111 ( first and last bits differ in two numbers).
#
# Example : Input:  arr[] = {1, 3, 5}
# Output: 8
# All pairs in array are (1, 1), (1, 3), (1, 5)
#                        (3, 1), (3, 3) (3, 5),
#                        (5, 1), (5, 3), (5, 5)
# Sum of bit differences =  0 + 1 + 1 +
#                           1 + 0 + 2 +
#                           1 + 2 + 0
#                        = 8
#
# Used : The idea is to count differences at individual bit positions. We traverse from 0 to 31 and count numbers
# with i'th bit set. Let this count be 'count'. There would be "n-count" numbers with i'th bit not set. So count of
# differences at i'th bit would be "count * (n-count) * 2", the reason for this formula is as every pair having one
# element which has set bit at i'th position and second element having unset bit at i'th position contributes exactly
# 1 to sum, therefore total permutation count will be count*(n-count) and multiply by 2 is due to one more repetition
# of all this type of pair as per given condition for making pair 1<=i,j<=N.
# Complexity : O(n)


def sumBitDifferences(arr):
    n = len(arr)
    ans = 0
    for i in range(0, 32):
        # count number of elements with i'th bit set
        count = 0
        for j in range(0, n):
            if arr[j] & (1 << i):
                count += 1
        ans += count * (n - count) * 2

    return ans


if __name__ == "__main__":
    arr = [1, 3, 5]
    print(sumBitDifferences(arr))
