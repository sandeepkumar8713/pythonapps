# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers chosen from
# the range [1, n]. You may return the answer in any order.
#
# Example : Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#
# Question Type : Easy
# Used : Use a set. Call recursion with input k and set.
#        Loop over the elements in set.
#        Pick each element from set, call recur with k-1 until it becomes 0 and remove the element
#        from the set.
#        At the end of the function, place back the element in set.
# Complexity : O(n*k)
# TODO :: add code
#