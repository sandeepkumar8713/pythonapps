# https://leetcode.com/problems/ones-and-zeroes/
# Question : You are given an array of binary strings strs and two integers m and n. Return the
# size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
#
# Example : Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
#
# Question Type : ShouldSee
# Used : Make dp array where dp[i] = [count,zeros,ones], count 1 means inpArr[i] satisfy the condition.
#        zeros and ones are 0 and 1 count of inpArr[i].
#        Now make all possible pairs by running 2 loops. Check if pairs can be merged and if count
#        value can be increased. (like box stacking). While doing so keep track of max count.
#        After the loop, return maxCount
#        Logic :
#        for i in range(1, n):
#           for j in range(i):
#               rightEle = dp[i]
#               leftEle = dp[j]
#               if leftEle[1] + rightEle[1] <= n0 and leftEle[2] + rightEle[2] <= n1:
#                   if leftEle[0] + 1 > rightEle[0]:
#                       rightEle[0] = leftEle[0] + 1
#                       maxCount = max(maxCount, rightEle[0])
#        return maxCount
# Complexity : O(n^2) where n is number of elements in input array


def largestSubset(inpArr, n1, n0):
    n = len(inpArr)
    dp = []
    maxCount = 0

    for ele in inpArr:
        ones = 0
        zeros = 0
        for ch in ele:
            if ch == "1":
                ones += 1
            else:
                zeros += 1
        count = 0
        if zeros <= n0 and ones <= n1:
            count = 1
        dp.append([count, zeros, ones])

    for i in range(1, n):
        for j in range(i):
            rightEle = dp[i]
            leftEle = dp[j]
            if leftEle[1] + rightEle[1] <= n0 and leftEle[2] + rightEle[2] <= n1:
                if leftEle[0] + 1 > rightEle[0]:
                    rightEle[0] = leftEle[0] + 1
                    maxCount = max(maxCount, rightEle[0])

    return maxCount


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(largestSubset(strs, m, n))

    strs = ["10", "0", "1"]
    m = 1
    n = 1
    print(largestSubset(strs, m, n))
