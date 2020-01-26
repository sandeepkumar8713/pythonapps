# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
# Question : A graph has N vertices numbered from 1 to N. We have two lists. One list M consisted of edges
# between vertices. The other list K consists of restricted paths. We have to add edges one by one from M and
# check whether the addition of the particular edge leads to a path between the restricted edges given in K.
# If it creates a path, we have to discard the edge.
#
# Example: N = 4; K = {(1, 4)}; M = {(1, 2), (2, 3), (3, 4)}.
# Here, addition of edge (3, 4) will create a path between 1 and 4. Hence we discard edge (3, 4)
#
# Question Type : Generic
# Used : For the given edgeList, Loop over it.
#        Add the edge in graph, find connected components,
#        If restricted path edges are there in connect component, remove the edge from graph
# Complexity : O(E * E * V * (V+E)) where E is edge count V is vertex count


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = dict()  # default dictionary to store graph
        for i in range(vertices):
            self.graph[i] = []

    # We assume this is undirected graph
    def addEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def removeEdge(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.graph[v]:
            if visited[i] is False:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] is False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


if __name__ == "__main__":
    g = Graph(4)
    restrictedPaths = [[0, 3]]
    edgeList = [(0, 1), (1, 2), (2, 3)]

    for edge in edgeList:
        g.addEdge(edge[0], edge[1])
        connectedComponents = g.connectedComponents()

        for restrictedPath in restrictedPaths:
            for connectedComponent in connectedComponents:
                if restrictedPath[0] in connectedComponent and restrictedPath[1] in connectedComponent:
                    g.removeEdge(edge[0], edge[1])
                    print("Removed this edge : %s, %s " % (edge[0], edge[1]))
                    break

    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
