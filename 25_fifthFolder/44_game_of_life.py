# https://leetcode.com/problems/game-of-life/discuss/1512567/python-3-in-place-operation
# Question : The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors
# (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the
# current state, where births and deaths occur simultaneously. Given the current state of the m x n
# grid board, return the next state.
#
# Question Type : Generic
# Used : Loop over the given matrix, check for above mentioned conditions and mark the cell if it needs
#        to be changed(-1 or -2). Now loop over the matrix again and update marked cells
# Complexity : O(m*n)
#
# TODO :: add code
#

