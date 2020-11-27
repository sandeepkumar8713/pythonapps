# Question : Given a snake and ladder board, find the minimum number of dice throws required to reach the
# destination or last cell from source or 1st cell. Basically, the player has total control over outcome of dice
# throw and wants to find out minimum number of throws required to reach last cell.
#
# Question Type : Easy
# Used : Make a class Cell with attributes : position and diceThrowCount to reach this cell.
#        Make a list of all possible dice outcome : 1, 2, 3, 4, 5, 6.
#        Maintain a list of already visited cell.
#        Push the starting cell in queue and start a loop to do BFS over it. Loop while queue is empty or
#        target is reached. In loop pop a cell from queue. Now loop over all the possible moves it can make
#           from that cell. i.e. from 1 to 6. If the next pos is not yet visited, make a new cell(object) for
#           it, taking into consideration whether the next pos goes to snake or ladder or stays there.
#           Append this cell in the queue.
#        Once the queue gets empty, print the minimum dice throw count using the last popped cell.
# Complexity : O(N) no. of cells


class Cell(object):
    def __init__(self, pos, diceThrowCount):
        self.pos = pos
        self.diceThrowCount = diceThrowCount


def getMinDiceThrows(move, N):
    visited = [False] * N
    queue = []
    visited[0] = True

    # six possible ways
    possibleDiceValue = [1, 2, 3, 4, 5, 6]
    queue.append(Cell(0, 0))
    qe = queue[0]

    while queue:
        qe = queue.pop(0)
        pos = qe.pos

        # Destination reached
        if pos == N - 1:
            break

        for outcome in possibleDiceValue:
            nextPos = pos + outcome

            if nextPos < N and visited[nextPos] is False:
                nextDiceThrowCount = qe.diceThrowCount + 1
                visited[nextPos] = True
                if move[nextPos] != -1:
                    afterNextPos = move[nextPos]
                else:
                    afterNextPos = nextPos

                a = Cell(afterNextPos, nextDiceThrowCount)
                queue.append(a)

    return qe.diceThrowCount


if __name__ == "__main__":
    N = 30
    moves = [-1] * N

    # Ladders
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28

    # Snakes
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print("Min Dice throws required is:", getMinDiceThrows(moves, N))
