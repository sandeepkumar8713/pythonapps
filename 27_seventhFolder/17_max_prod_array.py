# https://leetcode.com/problems/maximum-product-subarray/
# Question : Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product. The test cases are generated
# so that the answer will fit in a 32-bit integer. A subarray is a contiguous subsequence
# of the array.
#
# Question Type : Generic
# Used : It is a variance of Kadane's algorithm.
#        We should also maintain min check so far. As later on we can get a negative
#        value, which can turn it in positive.
# Logic: for i in range(1, n):
#           max_here_check = max_so_far * inpArr[i]
#           min_here_check = min_so_far * inpArr[i]
#           max_so_far = max(max_here_check, min_here_check, inpArr[i])
#           min_so_far = min(max_here_check, min_here_check, inpArr[i])
#           maxAns = max(maxAns, max_so_far)
#        return maxAns
# Complexity : O(n)

def maxProduct(inpArr):
    n = len(inpArr)
    maxAns = inpArr[0]
    max_so_far = inpArr[0]
    min_so_far = inpArr[0]

    for i in range(1, n):
        max_here_check = max_so_far * inpArr[i]
        min_here_check = min_so_far * inpArr[i]

        max_so_far = max(max_here_check, min_here_check, inpArr[i])
        min_so_far = min(max_here_check, min_here_check, inpArr[i])
        maxAns = max(maxAns, max_so_far)

    return maxAns


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))
