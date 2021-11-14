# https://leetcode.com/discuss/interview-experience/343949/Google-or-L4-or-Bay-Area-or-July-2019
# Question : Given an array of intergers divide them into n subsets such that difference
# between sum of each subset is minimum.
#
# Example : input [1,1,4,2,8] and n=2
# output = [1,1,4,2] and [8]
#
# input [1,1,4,2,8] and n=3
# output = [1,1,2] and [4] and [8]
#
# Question Type : ShouldSee
# Used : sort input array . pull max out, push in set1, then pull max out, push in set2 and then pull max out,
#        push in set3. Now, pull max out, push in least sum set. Repeat this until input array is empty.
# Complexity : O(n log n + n)
# TODO : add code
#
