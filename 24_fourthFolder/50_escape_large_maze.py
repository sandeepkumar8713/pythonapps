# https://blog.baozitraining.org/2019/05/leetcode-solution-1036-escape-large-maze.html
# Question : In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.
# We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally
# adjacent square in the grid that isn't in the given list of blocked squares. Return true if and only if it is
# possible to reach the target square through a sequence of moves.
#
# Question Type : Generic
# Used : Since we know that at max there can be only 200 blocks in the grid, If the distance between source and target
#        is more than 20000, we can say loop doesn't exist. If loop doesn't exist around source or target, we can say
#        that there is path between source and target. (See the figures in link to understand 20000).
#        Given such huge contrast between the block size (0,200) and the grid size (1M, 1M), all we need to do is
#        to check if there is any loops built by block on source and target b/w if there is a loop, we cannot
#        explore outside of the loop. However, notice if target and source are in the same loop, then we are fine.
# Logic: def isEscapePossible(blocked, source, target):
#        blockLookup = indexBlockedMatrixToSet(blocked)
#        if isLoopAroundPoint(source, target, blockLookup): return False
#        if isLoopAroundPoint(target, source, blockLookup): return False
#        return True
#
#        def isLoopAroundPoint(source, target, blockLookup):
#        count = 0, visited = set(), queue = []
#        queue.append((source[0], source[1]))
#        visited.add((source[0], source[1]))
#        while len(queue) > 0:
#           x, y = queue.pop(0)
#           if count >= MAX_COUNT_THRESHOLD: return False
#           if x == target[0] and y == target[1]: return False
#           for i in range(4):
#               nextX = x + xDirection[i]
#               nextY = y + yDirection[i]
#               if not (0 <= nextX < ONE_MILLION and 0 <= nextY < ONE_MILLION):
#                   continue
#               if (nextX, nextY) in blockLookup or (nextX, nextY) in visited:
#                   continue
#               count += 1
#               visited.add((nextX, nextY))
#               queue.append((nextX, nextY))
#        return True
# Complexity : O(20000) space O(20000)

xDirection = [1, 0, -1, 0]
yDirection = [0, -1, 0, 1]
ONE_MILLION = 1000000
MAX_COUNT_THRESHOLD = 20000


def indexBlockedMatrixToSet(blocked):
    lookup = set()
    for i in range(len(blocked)):
        x = blocked[i][0]
        y = blocked[i][1]
        lookup.add((x, y))
    return lookup


def isEscapePossible(blocked, source, target):
    if blocked is None or source is None or target is None:
        return False

    blockLookup = indexBlockedMatrixToSet(blocked)
    if isLoopAroundPoint(source, target, blockLookup):
        return False

    if isLoopAroundPoint(target, source, blockLookup):
        return False

    return True


def isLoopAroundPoint(source, target, blockLookup):
    count = 0
    visited = set()
    queue = []
    queue.append((source[0], source[1]))
    visited.add((source[0], source[1]))

    while len(queue) > 0:
        x, y = queue.pop(0)

        if count >= MAX_COUNT_THRESHOLD:
            return False

        if x == target[0] and y == target[1]:
            return False

        for i in range(4):
            nextX = x + xDirection[i]
            nextY = y + yDirection[i]

            if not (0 <= nextX < ONE_MILLION and 0 <= nextY < ONE_MILLION):
                continue

            if (nextX, nextY) in blockLookup or (nextX, nextY) in visited:
                continue

            count += 1
            visited.add((nextX, nextY))
            queue.append((nextX, nextY))

    return True


if __name__ == "__main__":
    blocked = [[0, 1], [1, 0]]
    source = [0, 0]
    target = [0, 2]
    print(isEscapePossible(blocked, source, target))

    blocked = []
    source = [0, 0]
    target = [999999, 999999]
    print(isEscapePossible(blocked, source, target))
