# https://leetcode.com/discuss/interview-question/391195/
# Question : You play a game of Go. You are given a board with some stones placed on it (w is white stone,
# b is black stone, e is empty spot.), and you are given a new black stone to be placed on an empty spot.
# You have to return the number of enemy stones that this move will capture.
#
# Example : Input: board = [[e, e, e, e, b, b, b], row = 2, col = 5
# 			                [e, e, e, e, b, w, b]
# 			                [e, e, e, e, b, e, b],
# 			                [e, e, e, e, e, e, e]]
# Output: 1
# Explanation: If you place a black stone on (2, 5) then you capture 1 white stone from the enemy.
#
# Question Type : Generic
# Used : Do BFS, from the adjacent nodes of the given node. Also keep a set of visited whites.
#        While doing BFS, push only white enemy in nodes, skip the node if it is already
#        visited or black and break BFS if any empty slot is found.
#        Keep increasing count of white enemy found.
#        Logic : max_capture(board, row, col):
#        total_capture = 0, visited = set()
#        board[row][col] = 'b'
#        for x_offset, y_offset in dirs:
#           xx, yy = row + x_offset, col + y_offset
#           if isInsideBoard(board, xx, yy):
#               total_capture += bfs(board, visited, xx, yy)
#        return total_capture
#        Doing BFS for white only.
#        def bfs(board, visited, x, y):
#           capture = 0, que = [], que.append((x, y))
#           is_surrounded_by_black = True
#           while len(que) > 0:
#               cur_x, cur_y = que.pop(0)
#               if board[cur_x][cur_y] == 'e':
#                 is_surrounded_by_black = False
#                 break
#             elif (cur_x, cur_y) in visited or board[cur_x][cur_y] == 'b':
#                 continue
#             else:  # board[cur_x][cur_y] == 'w':
#                 capture += 1, visited.add((cur_x, cur_y))
#                 for x_offset, y_offset in dirs:
#                     xx, yy = cur_x + x_offset, cur_y + y_offset
#                     if isInsideBoard(board, xx, yy): que.append((xx, yy))
#           return capture if is_surrounded_by_black else 0
# Complexity : O(n)

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def max_capture(board, row, col):
    total_capture = 0

    visited = set() # store visited positions of "white" stones
    board[row][col] = 'b'
    for x_offset, y_offset in dirs:
        xx, yy = row + x_offset, col + y_offset
        if isInsideBoard(board, xx, yy):
            total_capture += bfs(board, visited, xx, yy)
    return total_capture


def bfs(board, visited, x, y): #  return the total number of white stones I can capture if I start searching from (x, y)
        que = []
        que.append((x, y))
        is_surrounded_by_black = True
        capture = 0

        while len(que) > 0:
            cur_x, cur_y = que.pop(0)

            if board[cur_x][cur_y] == 'e':   # Empty
                is_surrounded_by_black = False
                break
            elif (cur_x, cur_y) in visited or board[cur_x][cur_y] == 'b':
                continue
            else:  # board[cur_x][cur_y] == 'w':
                capture += 1
                visited.add((cur_x, cur_y))
                for x_offset, y_offset in dirs:
                    xx, yy = cur_x + x_offset, cur_y + y_offset
                    if isInsideBoard(board, xx, yy):
                        que.append((xx, yy))

        return capture if is_surrounded_by_black else 0


def isInsideBoard(board, x, y):
    m = len(board)
    n = 0 if m == 0 else len(board[0])
    if 0 <= x < m and 0 <= y < n:
        return True
    else:
        return False


if __name__ == "__main__":
    board = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
             ['e', 'e', 'e', 'e', 'b', 'w', 'b'],
             ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e']]

    # board = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
    #          ['e', 'e', 'e', 'b', 'w', 'w', 'b'],
    #          ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e']]
    #
    # board = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
    #          ['e', 'e', 'e', 'e', 'w', 'w', 'b'],
    #          ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e']]

    row = 2
    col = 5
    print(max_capture(board, row, col))

