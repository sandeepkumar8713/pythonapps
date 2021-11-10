# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
# Question : Given a directed graph, check whether the graph contains a cycle or not.
# Your function should return true if the given graph contains at least one cycle,
# else return false. For example, the following graph contains three
# cycles 0->2->0, 0->1->2->0 and 3->3, so your function must return true.
#
# Question Type : Generic
# Used : Recursion stack means the single depth while moving from first vertex to last vertex.
#        While in this stack if we get a previously visited vertex then we can say that we
#        have a cycle.
#        Visit the all the vertex of graph using DFS and also keep track of vertex in
#        current recStack.
#        If we find a already visited vertex which is already in current recursion stack
#        return True.
#        While exiting a stack (recursive func call), mark that vertex in recStack as false.
#        If we come out of above loop then return false. No cycle found.
#        Logic :
#        isCyclicUtils(self, v, visited, recStack):
#        visited[v] = True, recStack[v] = True
#        for i in self.graph[v]:
#           if visited[i] is False:
#               if self.isCyclicUtils(i, visited, recStack):
#                   return True
#               elif recStack[i] is True:
#                   return True
#        recStack[v] = False
#        return False
# Complexity : O(V+E) count of vertex and edges


class Graph:
    def __init__(self, n):
        # key : list
        self.graph = dict()
        for i in range(n):
            self.graph[i] = []

    def addEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def isCyclicUtils(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                if self.isCyclicUtils(i, visited, recStack):
                    return True
            elif recStack[i] is True:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        V = len(self.graph)
        visited = [False] * V
        recStack = [False] * V

        for i in self.graph.keys():
            if visited[i] is False:
                self.isCyclicUtils(i, visited, recStack)
            elif recStack[i] is True:
                return True

        return False


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print(g.isCyclic())
