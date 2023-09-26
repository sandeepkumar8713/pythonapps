# Question : On a 2D plane, we place stones at some integer coordinate points. Each coordinate point may have
# at most one stone. Now, a move consists of removing a stone that shares a column or row with another stone
# on the grid. What is the largest possible number of moves we can make?
#
# Example : Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# matrix : [x,x,0]
#          [x,0,x]
#          [0,x,x]
#
# Example : Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
#
# Question Type : Generic
# Used : We try to convert this to a graph problem. We assume rows and columns as nodes.
#        So for a element in matrix, we make a union of its row and column.
#        If 2 elements are on same row or col, they will have union and make a set.
#        Remember elements sharing common row and col would form a disjoint set. So there
#        might be multiple disjoint sets in the graph. When it comes to removing stones,
#        all stones except the last stone can be
#        removed from a set. So it comes down to counting number of disjoint sets.
# Logic: def removeStones(stones):
#        N = len(stones)
#        dsu = DSU(20000)
#        for x, y in stones:
#           dsu.union(x, y + 10000)
#        disJointSet = set()
#        for x, y in stones:
#           parent = dsu.find(x)
#           disJointSet.add(parent)
#        return N - len(disJointSet)
#        def find(self, x):
#        if self.p[x] != x:
#           self.p[x] = self.find(self.p[x])
#        return self.p[x]
#        def union(self, x, y):
#        xr = self.find(x)
#        yr = self.find(y)
#        self.p[xr] = yr
# Complexity : O(n log n)


class DSU:
    def __init__(self, N):
        self.p = []
        for i in range(N):
            self.p.append(i)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


def removeStones(stones):
    N = len(stones)
    dsu = DSU(20000)
    for x, y in stones:
        dsu.union(x, y + 10000)

    disJointSet = set()
    for x, y in stones:
        parent = dsu.find(x)
        disJointSet.add(parent)

    print("disjoint set count :", len(disJointSet))
    return N - len(disJointSet)


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2], [3, 3]]
    print(removeStones(stones))
