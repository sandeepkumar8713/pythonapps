# https://leetcode.com/discuss/interview-question/311662/Google-or-Phone-screen-or-Closest-XY-pair-in-a-grid
# Question : Give a gird, and there are X and Y in this grid. find the shortest distance between X and Y.
#
# Example : Input:
# [[X,0,0],
#  [0,Y,0],
#  [X,Y,0]]
# Output: 1
#
# Used : We can solve this using BFS.
#        Push all 'X's into queue initially. Perform BFS and stop when the first 'Y' is encountered.
# Complexity : O(m * n)


def bfs(grid):
    from collections import deque
    q, visited = deque(), set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Insert all Xs into the queue
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                # (position, distance)
                q.append(((i, j), 0))
                visited.add((i, j))

    while q:
        for _ in range(len(q)):
            (row, col), dist = q.popleft()
            if grid[row][col] == 'Y':
                return dist

            for dir in dirs:
                new_pos = (new_r, new_c) = row + dir[0], col + dir[1]
                if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]) or new_pos in visited:
                    continue
                q.append((new_pos, dist + 1))
                visited.add(new_pos)

    # Can't reach Y
    return -1


if __name__ == "__main__":
    grid = [['X', '0', '0'],
            ['X', '0', '0'],
            ['0', 'Y', 'Y']]
    print(bfs(grid))
