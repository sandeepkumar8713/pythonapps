# https://www.geeksforgeeks.org/maximize-sum-of-given-array-by-rearranging-array-such-that-the-difference-between-adjacent-elements-is-atmost-1/
# Question : Given an array arr[] consisting of N positive integers, the task is to maximize the sum of
# the array element such that the first element of the array is 1 and the difference between the adjacent
# elements of the array is at most 1 after performing the following operations:
# Rearrange the array elements in any way.
# Reduce any element to any number that is at least 1.
#
# Examples: Input: arr[] = {3, 5, 1}
# Output: 6
# Explanation: One possible arrangement is {1, 2, 3} having maximum possible sum 6.
#
# Question Type : Generic
# Used : Make a freq count array of size n+1. It will store freq of each element of inpArr. If any
#        element is more than n, then its freq will be stored at n index of count array. Initialize
#        nextUniqNum as 0. Now loop over the count array, while its value is more than 0 and nextUniqNum
#        is less than current index i, keep incrementing the nextUniqNum and adding the same in ans, while
#        reducing its freq count. It might happen that nextUniqNum becomes equal or more than current index
#        i and count[i] > 1. Meaning more elements need to be added for given i, but we can increase nextUniqNum
#        as doing so might increase the last element value in the resultant array but we are just allowed
#        to reduce the values not increase it. So we just repeat with value with i. Add i * count[i] in ans.
#        maxSum(a, n):
#        count = [0] * (n + 1)
#        for i in range(0, n):
#           count[min(a[i], n)] += 1
#        nextUniqNum = 0, ans = 0
#        for i in range(1, n + 1):
#           while count[i] > 0 and nextUniqNum < i:
#               nextUniqNum += 1
#               ans += nextUniqNum
#               count[i] -= 1
#           ans += i * count[i]
#        return ans
# Complexity : O(n)

def maxSum(a, n):
    count = [0] * (n + 1)
    for i in range(0, n):
        count[min(a[i], n)] += 1
    nextUniqNum = 0
    ans = 0

    for i in range(1, n + 1):
        while count[i] > 0 and nextUniqNum < i:
            # nextUniqNum will be incremented only when it is less then current index i.
            nextUniqNum += 1
            ans += nextUniqNum
            count[i] -= 1
        # This line will run when, nextUniqNum will be equal or more than i.
        ans += i * count[i]
    return ans


if __name__ == '__main__':
    arr = [3, 5, 1]
    print(maxSum(arr, len(arr)))

    arr = [1, 2, 2, 2, 3, 4, 5]
    print(maxSum(arr, len(arr)))

    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5]
    print(maxSum(arr, len(arr)))
