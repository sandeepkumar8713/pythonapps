# https://www.geeksforgeeks.org/maximize-sum-possible-by-selecting-k-array-elements-followed-by-decrementing-them-by-1/
# Question : Given an array arr[] consisting of N positive integers and an integer K. In one operation,
# select an array element, add it to the sum and then decrement it by 1. The task is to print the
# maximum sum that can be obtained by performing the operation K times.
#
# Example : Input: arr[] = {2, 8, 4, 10, 6}, K = 2
# Output: 19
# Explanation:
# Perform the following operations to maximize the sum:
# Operation 1: Select 10, then reduce it so new array become {2, 8, 4, 9, 6}.
# Operation 2: Select 9, then reduce it so new array become {2, 8, 4, 8, 6}.
# Therefore, the maximum sum is 10 + 9 = 19.
#
# Question Type : Generic
# Used : We can use max heap here, and do the operation k times. Its complexity will be O(n log n).
#        Other option is use freq map, loop over it in reverse and pick the largest element,
#        add the same in answer and assign its freq to largest - 1 number in count map.
# Logic: getMaxSum(inpArr, k):
#        maxEle = max(inpArr)
#        count = [0] * (maxEle + 1)
#        ans = 0
#        for ele in inpArr:
#           count[ele] += 1
#        for i in range(maxEle, -1, -1):
#           if k >= count[i]:
#               ans += i * count[i]
#               k -= count[i]
#               count[i - 1] += count[i]
#           else:
#               ans += i * k
#               break
#     return ans
# Complexity : O(n)

def getMaxSum(inpArr, k):
    maxEle = max(inpArr)
    count = [0] * (maxEle + 1)
    ans = 0

    for ele in inpArr:
        count[ele] += 1

    for i in range(maxEle, -1, -1):
        if k >= count[i]:
            ans += i * count[i]
            k -= count[i]
            count[i - 1] += count[i]
        else:
            ans += i * k
            break
    return ans


if __name__ == "__main__":
    inpArr = [2, 5]
    k = 4
    print(getMaxSum(inpArr, k))

    inpArr = [2, 8, 4, 10, 6]
    k = 2
    print(getMaxSum(inpArr, k))
