# https://leetcode.com/problems/magic-squares-in-grid/
# Question : A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such
# that each row, column, and both diagonals all have the same sum. Given a row x col grid of
# integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
#
# Question Type : Generic
# Used : Make a masks for 3 rows, 3 cols and 2 diagonals.
#        Loop over matrix.
#        For each cell, using the above mask check if 8 sums are same.
#        If yes, increment ans.
# Complexity : O(n^2)
#
# TODO :: add code
#
