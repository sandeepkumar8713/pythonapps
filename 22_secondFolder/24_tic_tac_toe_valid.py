# CTCI : Q16_04_Tic_Tac_Win
# https://www.geeksforgeeks.org/validity-of-a-given-tic-tac-toe-board-configuration/
# Question : A Tic-Tac-Toe board is given after some moves are played. Find out if the given
# board is valid, i.e., is it possible to reach this board position after some moves or not.
#
# Since we know that the game starts with X, a given grid of Tic-Tac-Toe game would be definitely
# invalid if following two conditions meet
# a) countX != countO AND
# b) countX != countO + 1
#
# Question Type : ShouldSee
# Used : Make a list of list of 8 * 3. Which contains wining position.
#        Count the number of X and O in the board.
#        Check if xCount == oCount or xCount == oCount + 1: else return False
#        Check if O win:
#             if x win: return False
#             return xCount == oCount
#        Check if xWin and xCount != oCount + 1: return False
#        return True (O is not winner)
# Complexity : O(n)


win = [[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6]]


def isCWin(board, symbol):
    for i in range(len(win)):
        if board[win[i][0]] == symbol and board[win[i][1]] == symbol and board[win[i][2]] == symbol:
                return True
    return False


def isValid(board):
    xCount = 0
    oCount = 0
    for symbol in board:
        if symbol == 'X':
            xCount += 1
        elif symbol == 'O':
            oCount += 1

    if not (xCount == oCount or xCount == oCount + 1):
        return False

    oWin = isCWin(board, 'O')
    xWin = isCWin(board, 'X')
    if oWin:
        if xWin:
            return False    # both can't be winner

        return xCount == oCount  # as O will finish the game

    if xWin and xCount != oCount + 1:
        return False

    # If 'O' is not winner, then return true
    return True


if __name__ == "__main__":
    board = ['X', 'X', 'O',
             'O', 'O', 'X',
             'X', 'O', 'X']

    # board = ['X', 'X', 'X',
    #          'O', 'O', 'O',
    #          'X', 'O', 'X']
    print(isValid(board))
