# Question : Write a function to print the breadth first traversal for a undirected graph from a given source s.
#
# Used : Make a class whose member graph is a dict of keys(vertices) whose value is list of vertices it is connected to.
#        Call a BFS(source) function whose input is source vertex. It maintains a list of boolean values to specify
#           whether the vertices is visited or not. It appends the source to the queue marks this vertex as visited.
#           It calls a function BFSUtil which takes queue and visited as input. It loops over queue until it is empty.
#               In loop it pops an vertex from queue and prints it. It loops over the vertices which are connected to
#               the poped out vertex. If this connected vertex is not visited before then push it in queue and mark it
#                as visited.
# Complexity : O(V+E) count of vertex and edges


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

    def BFSUtils(self, queue, visited):
        while len(queue) != 0:
            vertex = queue.pop(0)
            print vertex,

            for connectedVertex in self.graph[vertex]:
                if visited[connectedVertex] is False:
                    visited[connectedVertex] = True
                    queue.append(connectedVertex)

    def BFS(self, start):
        V = len(self.graph)
        visited = [False] * V
        queue = [start]
        visited[start] = True
        self.BFSUtils(queue, visited)

    def BFSAll(self):
        V = len(self.graph)
        visited = [False] * V
        queue = []

        for v in self.graph.keys():
            if visited[v] is False:
                queue.append(v)
                visited[v] = True
                self.BFSUtils(queue, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print "Following is Breadth First Traversal"
    g.BFS(2)
    # g.BFS(4)
    # g.BFSAll()
