# https://leetcode.com/problems/surrounded-regions/
# Question : Given an m x n matrix board containing 'X' and 'O', capture all regions that are
# 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in
# that surrounded region.
#
# Example : Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Question Type : Generic
# Used : Note that only the "0" cells which are at edge of matrix, can't be surrounded.
#        So we do DFS over such elements and mark them at T.
#        After the DFS, we mark the remaining "0" as "X" as they can be captured
#        Now revert back non-surrounded T to X
#        Logic :
#        def dfs(i, j, ch):
#           if board[i][j] == "O":
#               board[i][j] = ch
#               for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#                   if 0 <= a < len(board) and 0 <= b < len(board[0]):
#                       dfs(a, b, ch)
#
#        def solve(board):
#        for i in range(len(board)):
#           for j in range(len(board[0])):
#               if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
#                   dfs(i, j, "T")
#        for i in range(len(board)):
#           for j in range(len(board[0])):
#               if board[i][j] == "O":
#                   board[i][j] = "X"
#               if board[i][j] == "T":
#                   board[i][j] = "O"
# Complexity : O(m * n)

def solve(board):
    def dfs(i, j, ch):
        if board[i][j] == "O":
            board[i][j] = ch
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= a < len(board) and 0 <= b < len(board[0]):
                    dfs(a, b, ch)

    # Loop over edge cells
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                dfs(i, j, "T")

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                board[i][j] = "X"

            if board[i][j] == "T":
                board[i][j] = "O"


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solve(board)
    print(board)