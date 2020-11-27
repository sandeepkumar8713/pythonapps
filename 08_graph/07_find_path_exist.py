# CTCI : Q8_02_Robot_in_a_Grid
# https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
# Question : Given N X N matrix filled with 1 , 0 , 2 , 3 . Find whether there is a path possible from source to
# destination, traversing through blank cells only. You can traverse up, down, right and left.
# A value of cell 1 means Source.
# A value of cell 2 means Destination.
# A value of cell 3 means Blank cell.
# A value of cell 0 means Blank Wall.
# Note : there is only single source and single destination(sink).
#
# Input : M[3][3] = {{ 0 , 3 , 2 },
#                    { 3 , 3 , 0 },
#                    { 1 , 3 , 0 }};
# Output : Yes
#
# Question Type : Generic, SimilarAdded
# Used : Make a graph of row*col nodes. Make array of all possible direction left, right, up and down.
#        Loop through the elements of matrix, if its not 0, then loop over all possible directions it
#           can go it. Check if next cell is within matrix and it is not a wall. If this condition is
#           satisfied then add an edge between this cell and next cell.
#           Also store source and destination cell number.
#        Call BFS over the graph with input source and destination. It should return true if path exist.
# Complexity : O(n*2)


class Graph:
    def __init__(self, n):
        # key : list
        self.graph = dict()
        for i in range(n):
            self.graph[i] = []

    def addEdge(self, u, v):
        # This takes care of undirected graph
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def BFSUtils(self, queue, visited, dest):
        while len(queue) != 0:
            vertex = queue.pop(0)

            for connectedVertex in self.graph[vertex]:
                if visited[connectedVertex] is False:
                    if connectedVertex is dest:
                        return True
                    visited[connectedVertex] = True
                    queue.append(connectedVertex)

        return False

    def BFS(self, start, dest):
        V = len(self.graph)
        visited = [False] * V
        queue = [start]
        visited[start] = True
        return self.BFSUtils(queue, visited, dest)


def isSafe(mat, i, j):
    row = len(mat)
    col = len(mat[0])
    if 0 <= i < row and 0 <= j < col:
        # next vertex should not be wall
        if mat[i][j] is not 0:
            return True
    return False


def findPath(mat):
    row = len(mat)
    col = len(mat[0])

    # Possible direction left, right, up, down
    dJ = [-1, 1, 0, 0]
    dI = [0, 0, -1, 1]
    nextVertex = [-1, 1, -col, col]
    g = Graph(row*col)

    vertexCount = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j] is 1:
                src = vertexCount

            if mat[i][j] is 2:
                dest = vertexCount

            if mat[i][j] is not 0:
                for k in range(len(nextVertex)):
                    if isSafe(mat, i + dI[k], j + dJ[k]):
                        g.addEdge(vertexCount, vertexCount+nextVertex[k])

            vertexCount += 1
    #print src, dest
    return g.BFS(src, dest)


if __name__ == "__main__":
    M = [[0, 3, 0, 1],
         [3, 0, 3, 3],
         [2, 3, 3, 3],
         [0, 3, 3, 3]]
    # M = [[0, 3, 0, 1],
    #      [3, 0, 3, 0],
    #      [2, 3, 3, 3],
    #      [0, 3, 3, 3]]
    print("Path exists:", findPath(M))
