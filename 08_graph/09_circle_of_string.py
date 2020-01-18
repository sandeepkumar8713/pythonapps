# Question : Given an array of strings, find if the given strings can be chained to form a circle. A string X
# can be put before another string Y in circle if the last character of X is same as first character of Y.
#
# Input: arr[] = {"for", "geek", "rig", "kaf"}
# Output: Yes, the given strings can be chained.
# The strings can be chained as "for", "rig", "geek" and "kaf"
#
# Used : Create a directed graph g with number of vertices equal to the size of alphabet.
#        Loop over the strings in input array and do this:
#           Add an edge from first character to last character of the given graph.
#       If the created graph has Eulerian circuit, then return true, else return false.
#
#       Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path
#       which starts and ends on the same vertex. For that these two conditions must be met:
#       1) All vertices with nonzero degree belong to a single strongly connected component.
#       2) In degree and out degree of every vertex is same
#
#       For 1) Find the first vertex whose out degree is more than 0. Use DFS using the vertex. If DFS traversal doesn't
#       visit all vertices with non zero degree, then return false. Take a transpose graph(gr) of this graph. Do DFS
#       using the same previously used vertex. If DFS traversal doesn't visit all vertices of original graph with non
#       zero degree, then return false. If above conditions are passed then return True.
#       For 2) Maintain in and out degree of each vertex in the graph and check if they are same for each vertex.
# Complexity : O(V+E)

CHARS = 26


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = dict()  # default dictionary to store graph
        for i in range(vertices):
            self.graph[i] = []
        self.inDegree = [0] * vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.inDegree[v] += 1

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # Strongly Connected
    def isSC(self):
        visited = [False] * self.V

        n = 0
        for n in xrange(self.V):
            if len(self.graph[n]) > 0:
                break

        # Do DFS traversal starting from first non zero degree vertex.
        self.DFSUtil(n, visited)

        # If DFS traversal doesn't visit all vertices with non zero degree, then return false.
        for i in xrange(self.V):
            if len(self.graph[i]) > 0 and visited[i] is False:
                return False

        gr = self.getTranspose()

        for i in xrange(self.V):
            visited[i] = False

        gr.DFSUtil(n, visited)

        # If DFS traversal doesn't visit all vertices of original graph with non zero degree, then return false.
        for i in xrange(self.V):
            if len(self.graph[i]) > 0 and visited[i] is False:
                return False

        return True

    def isEulerianCycle(self):
        # Check if there exist only 1 strongly connected component, that include all vertices with non zero degree
        if self.isSC() is False:
            return False

        # Check if in degree and out degree of every vertex is same
        for i in xrange(self.V):
            if len(self.graph[i]) != self.inDegree[i]:
                return False

        return True


def canBeChained(inpArr):
    g = Graph(CHARS)
    for i in range(len(inpArr)):
        s = inpArr[i]
        g.addEdge(ord(s[0]) - ord('a'), ord(s[len(s) - 1]) - ord('a'))

    return g.isEulerianCycle()


if __name__ == "__main__":
    inpArr = ["for", "geek", "rig", "kaf"]
    # inpArr = ["aab", "abb"]
    if canBeChained(inpArr):
        print ("Can be chained")
    else:
        print ("Can't be chained")

