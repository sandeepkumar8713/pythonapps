# https://careercup.com/question?id=5067303612317696
# Question : Given a binary tree of numbers and a search number has given, find out first occurrence of that number
# and smallest distance from root node. if you have given k search numbers find their occurrence and nearest
# from root node in a single walk.
#
# Question Type : Generic
# Used : Use bfs/level order traversal while keeping track of a distance from a root. If the first occurrence of
#        each number of the given array is found, update the result array with the current distance.
# Complexity : time O(n) where n is the total number of nodes in a tree
#              space O(Math.max(k, n)) where k is the total number of elements in an array.
# TODO :: add code
# 