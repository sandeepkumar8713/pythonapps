# https://leetcode.com/problems/bricks-falling-when-hit/
# Question : You are given an m x n binary grid, where each 1 represents a brick and 0 represents an
# empty space. A brick is stable if:
# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
# You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want
# to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will
# disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls,
# it is immediately erased from the grid (i.e., it does not land on other stable bricks).
# Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure
# is applied. Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.
#
# Example : Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
# [[1,0,0,0],
#  [0,0,0,0]]
# Hence the result is [2].
#
# Question Type : OddOne
# Used :
# Complexity :
#
# TODO ::
#
