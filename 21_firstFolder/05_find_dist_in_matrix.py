# https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/
# Question : Given a matrix (m*n) filled with X and 0(zero). Calculate the distance from
# nearest 0 for all cells marked with X. The distance of four neighboring cells
# (top,bottom,right,left) will be 1. The distance is calculated as |i1 - i2| + |j1 - j2|,
# where i1, j1 are the row number and column number of the current cell and i2, j2 are the
# row number and column number of the nearest cell having value 1.
#
# For example
# Input:X X X
# X 0 X
# X X X
# Output:
# 2 1 2
# 1 0 1
# 2 1 2
#
# Question Type : Generic, SimilarAdded
# Used : Represent the matrix as 2 way connected graph. Push the nodes which have 0 in the queue.
#        Do BFS and traverse the graph and keep updating the distance of all the adjacent nodes for
#        the node which has been popped out.
#        of queue.
#        findMinDistance(mat):
#        dist = [9999] * (n*m+1)
#        visit = [0] * (n*m+1)
#        queue = [], k = 1
#        for i in range(0, n):
#           for j in range(0, m):
#               if mat[i][j] == 1:
#                   dist[k] = 0
#                   visit[k] = 1
#                   queue.append(k)
#                k += 1
#        graph.bfs(visit, dist, queue)
#        graph.printDist(dist)
#
#        bfs(self, visit, dist, queue):
#        while len(queue) != 0:
#           temp = queue[0]
#           del queue[0]
#           for i in range(0, len(self.g[temp])):
#               if visit[self.g[temp][i]] != 1:
#                   dist[self.g[temp][i]] = min(dist[self.g[temp][i]], dist[temp]+1)
#                   queue.append(self.g[temp][i])
#                   visit[self.g[temp][i]] = 1
# Complexity : O(n^2)


class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.g = []
        for i in range(0, m*n+1):
            self.g.append([])

    def createGraph(self):
        k = 1

        for i in range(1, self.n+1):
            for j in range(1, self.m+1):

                if i == self.n:
                    if j != self.m:      # If last row, then add edge on right side.
                        self.g[k].append(k+1)
                        self.g[k+1].append(k)

                elif j == self.m:        # If last column, then add edge toward down.
                    self.g[k].append(k+self.m)
                    self.g[k+self.m].append(k)

                else:                   # Else make edge in all four direction.
                    self.g[k].append(k+1)
                    self.g[k+1].append(k)
                    self.g[k].append(k+self.m)
                    self.g[k+self.m].append(k)

                k += 1


    def bfs(self, visit, dist, queue):
        while len(queue) != 0:
            temp = queue[0]
            del queue[0]

            for i in range(0, len(self.g[temp])):
                if visit[self.g[temp][i]] != 1:
                    #print dist[self.g[temp][i]],dist[temp]+1
                    dist[self.g[temp][i]] = min(dist[self.g[temp][i]], dist[temp]+1)

                    queue.append(self.g[temp][i])
                    visit[self.g[temp][i]] = 1

    def printDist(self, dist):
        c = 0
        resStr = ''
        for i in range(1, len(dist)):
            resStr += str(dist[i]) + ' '
            c += 1

            if c % self.m == 0:
                print(resStr)
                c = 0
                resStr = ''


def findMinDistance(mat):
    n = len(mat)
    m = len(mat[0])
    graph = Graph(n, m)
    graph.createGraph()

    dist = [9999] * (n*m+1)
    visit = [0] * (n*m+1)
    queue = []
    k = 1

    for i in range(0, n):
        for j in range(0, m):
            if mat[i][j] == 1:
                dist[k] = 0
                visit[k] = 1
                queue.append(k)
            k += 1

    graph.bfs(visit, dist, queue)
    graph.printDist(dist)


if __name__ == "__main__":
    mat = [[0, 0, 0, 1],
           [0, 0, 1, 1],
           [0, 1, 1, 0]]
    findMinDistance(mat)
