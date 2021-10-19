# https://leetcode.com/problems/beautiful-arrangement-ii/
# Question : Given two integers n and k, construct a list answer that contains n different positive
# integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|,
# ... , |an-1 - an|] has exactly k distinct integers.
# Return the list answer. If there multiple valid answers, return any of them.
#
# Example : Input: n = 3, k = 2
# Output: [1,3,2]
# Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has
# exactly 2 distinct integers: 1 and 2.
#
# Question Type : ShouldSee
# Used : For k = 7, we need at least 8 elements to create 7 distinct diff.
#        Pick first k + 1 from the sorted array.
#        Place the first half at the even indices and reversely place
#        the second half at the gaps.
#        Return the array.
#        Logic :
#        temp = [i+1 for i in range(n)]
#        k += 1
#        ans = temp[::]
#        i = 0
#        while i < (k + 1)//2:
#           ans[i * 2] = temp[i]
#            i += 1
#        j = 0, i = k - 1
#        while i >= (k + 1)//2 and (j * 2 + 1) < n:
#           ans[j * 2 + 1] = temp[i]
#           i -= 1, j += 1
#        return ans
# Complexity : O(n)


# Take first k + 1 elements from the ascendingly sorted array
# Place the first half at the even indices, and reversely place
# the second half at the gaps.

def constructArray(n, k):
        temp = [i+1 for i in range(n)]
        k += 1

        ans = temp[::]
        i = 0
        while i < (k + 1)//2:
            ans[i * 2] = temp[i]
            i += 1

        j = 0
        i = k - 1
        while i >= (k + 1)//2 and (j * 2 + 1) < n:
            ans[j * 2 + 1] = temp[i]
            i -= 1
            j += 1

        return ans


if __name__ == "__main__":
    n = 3
    k = 2
    print(constructArray(n, k))

    n = 5
    k = 2
    print(constructArray(n, k))

    n = 3
    k = 1
    print(constructArray(n, k))
