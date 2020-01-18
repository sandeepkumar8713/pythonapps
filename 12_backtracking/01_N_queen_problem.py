# Question : The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens
# attack each other. Given an integer n, print all distinct solutions to the n-queens puzzle. If queen is placed
# in a cell, no other queen should be placed in that row,col or diagonal.
#
# Used : Make a board of size N*N and mark all as 0.
#        Make a call to recursive function solveNQUtil(board,col=0,N). If col >= N print board and return true.
#        Run a loop from 0 to n-1 for row, check if placing queen at board[i][col] is safe. (Check that row, col and
#           diagonal is clear or not) If true, board[i][col] = 1 and call solveNQUtil with col + 1. (Note that we are
#           running the loop row wise). While running the loop, atleast once solveNQUtil should return True.
#           res = solveNQUtil(board, col + 1, N) or res
#           board[i][col] = 0 (this is back tracking)
#        return res
# Complexity : T(n) = n*T(n-1) + O(n^2) = O(N!)

solutionCount = 0


def isSafe(board, row, col, N):
    for i in range(N):
        if board[row][i] == 1:
            return False

        if board[i][col] == 1:
            return False

        # Check all possible direction
        dI = [1, 1, -1, -1]
        dJ = [1, -1, 1, -1]

        for m in range(len(dI)):
            nextDirI = dI[m] + row
            nextDirJ = dJ[m] + col
            while 0 <= nextDirI < N and 0 <= nextDirJ < N:
                if board[nextDirI][nextDirJ] == 1:
                    return False

                nextDirI += dI[m]
                nextDirJ += dJ[m]

    return True


def solveNQUtil(board, col, N):
    global solutionCount
    if col >= N:
        solutionCount += 1
        for item in board:
            print (item)
        print ("")
        return True

    res = False
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1

            # Atleast one row should return True for solution to be feasible
            res = solveNQUtil(board, col + 1, N) or res
            board[i][col] = 0

    return res


def solveNQ(N):
    board = []
    for i in range(N):
        board.append([0] * N)

    if not solveNQUtil(board, 0, N):
        print ("Not Possible")


if __name__ == "__main__":
    N = 4  # 2 solution
    # N = 6 # 4 solution
    # N = 8  # 92 solution
    solveNQ(N)
    print ("Solution count : " + str(solutionCount))
