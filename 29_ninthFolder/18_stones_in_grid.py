# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/
# https://leetcode.com/discuss/interview-question/3847380/microsoft-ot
# Question : You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number
# of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a
# single cell. In one move, you can move a single stone from its current cell to any other cell if the
# two cells share a side. Return the minimum number of moves required to place one stone in each cell.
#
# Example : Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
# Output: 3
# Explanation: One possible sequence of moves to place one stone in each cell is:
# 1- Move one stone from cell (2,1) to cell (2,2).
# 2- Move one stone from cell (2,2) to cell (1,2).
# 3- Move one stone from cell (1,2) to cell (0,2).
# In total, it takes 3 moves to place one stone in each cell of the grid.
# It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
#
# TODO :: add used

import sys


def find_min_moves(inp_matrix):
    min_moves = sys.maxsize

    def dfs(x, y, candidate_res):
        nonlocal min_moves
        if candidate_res >= min_moves:
            return

        if y >= 3:
            dfs(x + 1, 0, candidate_res)
            return

        if x >= 3:
            min_moves = candidate_res
            return

        if inp_matrix[x][y] > 0:
            dfs(x, y + 1, candidate_res)
        else:
            for i in range(3):
                for j in range(3):
                    if inp_matrix[i][j] > 1:
                        inp_matrix[i][j] -= 1
                        inp_matrix[x][y] += 1
                        manhattan_dist = abs(x - i) + abs(y - j)
                        dfs(x, y + 1, candidate_res + manhattan_dist)
                        inp_matrix[x][y] -= 1
                        inp_matrix[i][j] += 1

    may = 0
    dfs(0, 0, may)
    return min_moves


if __name__ == "__main__":
    inp_matrix = [[2, 0, 2],
                  [1, 0, 0],
                  [2, 1, 1]]
    print(find_min_moves(inp_matrix))

    inp_matrix = [[1, 3, 0],
                  [1, 0, 0],
                  [1, 0, 3]]
    print(find_min_moves(inp_matrix))

    inp_matrix = [[1, 0, 1],
                  [1, 3, 0],
                  [2, 0, 1]]
    print(find_min_moves(inp_matrix))

    inp_matrix = [[0, 6, 0],
                  [2, 0, 0],
                  [0, 1, 0]]
    print(find_min_moves(inp_matrix))

