# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Question : Nearly everyone has used the Multiplication Table. The multiplication table of size m x n
# is an integer matrix mat where mat[i][j] == i * j (1-indexed). Given three integers m, n, and k,
# return the kth smallest element in the m x n multiplication table.
#
# Example : Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.
#
# Question Type : Generic
# Used : We do binary search from 1 to m*n, for each mid value, calculate the number of elements
#        which are less than k.
#        Logic :
#        left = 1, right = m*n
#        while(left<right):
#           mid = (left+right)//2
#           if search(mid, m, n) < k:
#               left = mid+1
#           else:
#               right = mid
#        return left
#
#        def search(number, m, n):
#        ans = 0
#        for i in range(1, min(m, number) + 1):
#           ans += min(n, number // i)
#        return ans
# Complexity : O(m log(m*n))


# count the number elements that are lower than number
def search(number, m, n):
    ans = 0
    for i in range(1, min(m, number) + 1):
        ans += min(n, number // i)
    return ans


def findKthNumber(m, n, k):
    # swapping the value of m and n has no influence on the results, since the table is symmetric
    if m > n:
        m, n = n, m

    # binary search
    left = 1
    right = m * n
    while left < right:
        mid = (left + right) // 2
        if search(mid, m, n) < k:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    m = 3
    n = 3
    k = 5
    print(findKthNumber(m, n, k))
