# https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/
# Question : Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from
# topmost-leftmost cell. A cell in given maze has value -1 if it is a blockage or dead end, else 0.
#
# Question Type : Generic, SimilarAdded
# Used : Now maze will represent number of ways to reach this cell from maze[0][0].
#        Set 1 for first row and column of maze till you find -1, then break
#        Run loop from 1 to row-1, 1 to col - 1. if maze[i][j] == -1 : continue, else
#           if maze[i-1][j] > 0: maze[i][j] += maze[i-1][j] (Add the paths possible from up and left to current)
#           if maze[i][j-1] > 0: maze[i][j] += maze[i][j-1]
#        if maze[row-1][col-1] is not -1, return it else return 0.
# Complexity : O(m*n)


def countPaths(maze):
    row = len(maze)
    col = len(maze)

    # Now maze will represent number of ways to reach this cell from maze[0][0]
    for i in range(0, row):
        if maze[i][0] == 0:
            maze[i][0] = 1
        else:
            break

    for j in range(1, col):
        if maze[0][j] == 0:
            maze[0][j] = 1
        else:
            break

    for i in range(1, row):
        for j in range(1, col):
            if maze[i][j] == -1:
                continue

            # Can get here from up
            if maze[i-1][j] > 0:
                maze[i][j] += maze[i-1][j]

            # Can get here from left
            if maze[i][j-1] > 0:
                maze[i][j] += maze[i][j-1]

    if maze[row-1][col-1] != -1:
        return maze[row-1][col-1]
    else:
        return 0


if __name__ == "__main__":
    maze = [[0,  0, 0, 0],
            [0, -1, 0, 0],
            [-1, 0, 0, 0],
            [0,  0, 0, 0]]
    print("Possible path count:", countPaths(maze))
