# https://www.geeksforgeeks.org/strongly-connected-components/
# Question : Given a graph with N nodes and M directed edges. Your task is to complete the function kosaraju which
# returns an integer denoting the no of strongly connected components in the graph. A directed graph is strongly
# connected if there is a path between all pairs of vertices. A strongly connected component (SCC) of a directed
# graph is a maximal strongly connected sub graph.
#
# Question Type : Generic
# Used : Kosaraju Algorithm
#        Create an empty stack 'S' and do DFS traversal of a graph. In DFS traversal, after calling recursive DFSUtils
#        for adjacent vertices of a vertex, push the vertex to stack.
#        Make one more graph, were the edge direction is reversed.
#        Now loop over the vertices popped from stack S and do DFS for it using the transposed graph if it is not yet
#           visited. Its DFS will give a group of strongly connected components.
# Complexity : O(V+E)


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = dict()  # default dictionary to store graph
        for i in range(vertices):
            self.graph[i] = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.fillOrder(i, visited, stack)
        stack.append(v)

    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):
        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] is False:
                self.fillOrder(i, visited, stack)

        gr = self.getTranspose()

        visited = [False] * self.V

        count = 0
        while stack:
            i = stack.pop()
            if visited[i] is False:
                gr.DFSUtil(i, visited)
                print("")
                count += 1
        print("count of SCCs : %s" % count)


if __name__ == "__main__":
    # g = Graph(5)
    # g.addEdge(1, 0)
    # g.addEdge(0, 2)
    # g.addEdge(2, 1)
    # g.addEdge(0, 3)
    # g.addEdge(3, 4)

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)

    print("Following are strongly connected components in given graph")
    g.printSCCs()
