# Question : Write a function to print the depth first traversal for a undirected graph from a given source s.
#
# Question Type : Easy
# Used : Make a class whose member graph is a dict of keys(vertices) whose value is list of vertices it is connected to.
#        Call a DFS(source) function whose input is source vertex. It maintains a list of boolean values to specify
#           whether the vertices is visited or not. It calls a recursive function DFSUtil which takes source and visited
#           as input. Mark the given vertex as visited and print it. Loop of the vertices which are connected to this
#           vertex. If this connected vertex is not yet visited call the recursive function DFSUtil again.
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

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, start):
        V = len(self.graph)
        visited = [False] * V
        self.DFSUtil(start, visited)

    def DFSAll(self):
        V = len(self.graph)
        visited = [False] * V

        for i in self.graph.keys():
            if visited[i] == False:
                self.DFSUtil(i, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal")
    g.DFS(0)
    # g.DFS(4)
    print("")
    g.DFSAll()
