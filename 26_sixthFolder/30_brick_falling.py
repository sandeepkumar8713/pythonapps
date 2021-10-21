# https://leetcode.com/problems/bricks-falling-when-hit/
# Question : You are given an m x n binary grid, where each 1 represents a brick and 0 represents an
# empty space. A brick is stable if:
# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
# You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want
# to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will
# disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls,
# it is immediately erased from the grid (i.e., it does not land on other stable bricks).
# Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure
# is applied. Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.
#
# Example : Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to
# another stable brick, so they will fall. The resulting grid is:
# [[1,0,0,0],
#  [0,0,0,0]]
# Hence the result is [2].
#
# Question Type : OddOne
# Used : Find parent and rank of each node with with respect to first row.
#        Now reverse the erase array, loop over it and do BFS.
#        While doing to keep track of rank difference b/w current and previous loop.
#        Append the difference in result array.
#        After BFS, return the result array in reverse.
# Complexity : O(k * m * n)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt:
            return False

        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt

        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


def hitBricks(grid, hits):
    m, n = len(grid), len(grid[0])  # dimensions

    seen = set()
    for i, j in hits:
        if grid[i][j]:
            seen.add((i, j))
            grid[i][j] = 0

    uf = UnionFind(m * n + 1)
    for i in range(m):
        for j in range(n):
            if i == 0 and grid[i][j]:
                uf.union(j, m * n)

            if grid[i][j]:
                for ii, jj in (i - 1, j), (i, j - 1):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]:
                        uf.union(i * n + j, ii * n + jj)

    ans = []
    prev = uf.rank[uf.find(m * n)]

    for i, j in reversed(hits):
        if (i, j) in seen:
            grid[i][j] = 1
            if i == 0:
                uf.union(j, m * n)

            for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]:
                    uf.union(i * n + j, ii * n + jj)

            rank = uf.rank[uf.find(m * n)]
            ans.append(max(0, rank - prev - 1))
            prev = rank
        else:
            ans.append(0)
    return ans[::-1]


if __name__ == "__main__":
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    print(hitBricks(grid, hits))
