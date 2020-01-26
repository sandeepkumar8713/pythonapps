# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight
# Question : Given a square chessboard of N x N size, the position of Knight and position of a target is given.
# We need to find out minimum steps a Knight will take to reach the target position.
# This is similar (infinite chess with forbidden cells) : https://www.careercup.com/question?id=5711185563877376
#
# Question Type : Generic
# Used : Make a queue Push starting cell(x,y,distance) point in queue
#        Loop (until queue is empty)
# 	        Pop one cell from queue
# 	        Add all possible directions to it. If it is inside board and non visited push to queue
# 	        If target reached then return distance
# Complexity : O(N) no. of cells


class Cell(object):
    def __init__(self, posX, posY, steps):
        self.posX = posX
        self.posY = posY
        self.steps = steps


def isSafe(i, j, N, visited):
    if 0 <= i < N and 0 <= j < N:
        if visited[i * N + j] is False:
            return True
    return False


def getMinStep(N, knightPos, targetPos):
    visited = [False] * (N * N)
    queue = []
    visited[0] = True

    # eight possible ways
    dI = [-2, -1, 1, 2, -2, -1, 1, 2]
    dJ = [-1, -2, -2, -1, 1, 2, 2, 1]

    queue.append(Cell(knightPos[0], knightPos[1], 0))
    qe = queue[0]

    while queue:
        qe = queue.pop(0)
        # Destination reached
        if qe.posX is targetPos[0] and qe.posY is targetPos[1]:
            break

        for i in range(len(dI)):
            nextPosI = qe.posX + dI[i]
            nextPosJ = qe.posY + dJ[i]

            if isSafe(nextPosI, nextPosJ, N, visited):
                visited[nextPosI * N + nextPosJ] = True
                stepCount = qe.steps + 1
                queue.append(Cell(nextPosI, nextPosJ, stepCount))

    return qe.steps


if __name__ == "__main__":
    N = 30
    knightPos = [0, 0]
    targetPos = [29, 29]

    print("Min steps required is:", getMinStep(N, knightPos, targetPos))
