# https://linlaw0229.github.io/2019/03/02/489-Robot-Room-Cleaner/
# https://www.cnblogs.com/grandyang/p/9988250.html
# Question : Given a robot cleaner in a room modeled as a grid.
# Each cell in the grid can be empty or blocked.
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }

# Example: Input:
# room = [[1,1,1,1,1,0,1,1],
#         [1,1,1,1,1,0,1,1],
#         [1,0,1,1,1,1,1,1],
#         [0,0,0,1,0,0,0,0],
#         [1,1,1,1,1,1,1,1]],
# row = 1,
# col = 3
#
# Used : We will use DFS(with 4 direction), with use of arrow and backtracking.
#        Logic : def dfs(robot, visited, x, y, arrow):
#        path = str(x) + "-" + str(y)
#        if path in visited: return
#        visited.add(path)
#        robot.clean()
#        for i in range(len(dirs)):
#           if robot.move():
#               nextX = x + dirs[arrow][0]
#               nextY = y + dirs[arrow][1]
#               dfs(robot, visited, nextX, nextY, arrow)
#               # trace back
#               robot.turnRight()
#               robot.turnRight()
#               robot.move()
#               robot.turnRight()
#               robot.turnRight()
#           robot.turnRight()
#           arrow = (arrow + 1) % 4
# Complexity : O(V + E)

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(robot, visited, x, y, arrow):
    path = str(x) + "-" + str(y)
    if path in visited:
        return
    visited.add(path)
    robot.clean()

    for i in range(len(dirs)):
        if robot.move():
            # go all the way till cannot move, then back one step
            nextX = x + dirs[arrow][0]
            nextY = y + dirs[arrow][1]

            dfs(robot, visited, nextX, nextY, arrow)
            # trace back
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        robot.turnRight()
        arrow = (arrow + 1) % 4


def cleanRoom(robot):
    visited = set()
    dfs(robot, visited, 0, 0, 0)
