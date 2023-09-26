# https://leetcode.com/discuss/interview-experience/353556/Google-or-SWE-or-MTV-or-July-2019-Rejected
# Question : Tree related. find the longest AP series (increasing or decresing) in binary Tree
#
# Question Type : Generic
# Used : To pre-order traversal, keep pushing nodes in the queue. When a leaf node is found, call the longest
#        AP search on it(check previous question). When we backtrack, pop elements from queue and also from
#        indexMap.
# Complexity : O(n^3)
#
# TODO :: add code
#
