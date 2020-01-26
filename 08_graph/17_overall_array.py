# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
# Question : Given various sub sequences of an array, print the overall array:
#
# Example:
# Input : [1, 3, 5], [1, 3, 9], [9, 5]
# Output : [1, 3, 9, 5]
#
# Question Type : ShouldSee
# Used : Insert the given arrays into the graph. Make sure it is a Direct Acyclic Graph (DAG).
#        Now do topological sort on the graph. It is similar to alien dictionary problem.
# Complexity : O(n)


class Graph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = []

        if v not in self.graph.keys():
            self.graph[v] = []

        if u in self.graph[v]:
            return

        if v not in self.graph[u]:
            self.graph[u].append(v)

    def DFSUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        stack = []
        visited = dict()
        for vertex in self.graph.keys():
            visited[vertex] = False

        for u in self.graph.keys():
            if visited[u] is False:
                self.DFSUtil(u, visited, stack)

        while stack:
            vertex = stack.pop()
            print(vertex, end=" ")


if __name__ == "__main__":
    g = Graph()
    arrayList = [[1, 3, 5], [1, 3, 9], [9, 5], [10]]

    for array in arrayList:
        if len(array) == 1:
            if not array[0] in g.graph.keys():
                g.graph[array[0]] = []
        else:
            for i in range(len(array) - 1):
                g.addEdge(array[i], array[i+1])

    print("Overall array :"),
    g.topologicalSort()
