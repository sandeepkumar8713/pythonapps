# CTCI : Q10_07_Missing_Int
# Question : Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
# this task. Follow up : What if you have only 1 O MB of memory? Assume that all the values are distinct
# and we now have no more than one billion non-negative integers.
#
# TODO :: add code
#
# Question Type : Easy
# Used : We have to use compact memory. make use of bit vector. 1 int have 32 bits.
#        If there 4 billion = 2^32 elements, we use 2^27 integers to represent whether
#        that element is present for not.
# Complexity : O(n)
