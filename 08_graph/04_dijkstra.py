# https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
# Question : Given a graph and a source vertex in the graph, find shortest paths from source
# to all vertices in the given graph.
#
# Question Type : Generic
# Used : Maintain a minDist array with size v, initialize them with maxInt.
#        Maintain a shortest path tree(SPT) array with size v, initialize them with False.
#        Initialize minDist[src] as 0.
#        Loop over the vertices of the graph. Find the index of vertex whose distance from
#           source to vertex is min (minimum value in minDist array which is not yet added
#           in SPT) and include it in SPT.
#           Now use this newly found vertex, to check if via (lesser cost) path is possible,
#           by looping over all the vertices which are not yet included in SPT and update
#           minDist.
# Logic: def dijkstra(self, src):
#        dist = [sys.maxsize] * self.V
#        dist[src] = 0
#        sptSet = [False] * self.V
#        for i in range(self.V):
#           u = self.minDistance(dist, sptSet)
#           sptSet[u] = True
#        for v in range(self.V):
#           if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
#               dist[v] = dist[u] + self.graph[u][v]
#        self.printSolution(src, dist)
# Complexity : O(n^2)
#              If the input graph is represented using adjacency list, it can be reduced to O(E log V)
#              with the help of binary heap.

import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append([])

    def printSolution(self, src, dist):
        print("Vertex t Distance from Source")
        for node in range(self.V):
            print(src, "->", node, "distance", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] is False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for i in range(self.V):
            # Find the index of vertex whose distance from source to vertex is min and include in shortest path tree
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            # Use this newly found vertex, to check if via path is possible and update minDist.
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(src, dist)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    g.dijkstra(0)
