# CTCI : Q2_07_Intersection
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
# Question : There are two singly linked lists in a system. By some programming error, the end node of one of the
# linked list got linked to the second list, forming an inverted Y shaped list. Write a program to get the point
# where two linked list merge.
#
# TODO :: add code
# Question Type : Easy
# Used : count m and n. start from (m-n) in bigger list. Loop and after each iteration check if
#        left.next == right.next.
# Complexity : O(n)
