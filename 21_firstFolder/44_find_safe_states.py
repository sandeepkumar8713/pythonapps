# https://leetcode.com/problems/find-eventual-safe-states/
# Question : In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If
# we reach a node that is terminal (that is, it has no outgoing directed edges), we stop. Now, say our starting node
# is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a
# natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less
# than K steps. Which nodes are eventually safe?  Return them as an array in sorted order. The directed graph has N
# nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form:
# graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.
#
# Example: Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
#
# Used : Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually. This is a classic
#        "white-gray-black" DFS algorithm that would be part of any textbook on DFS. We mark a node gray on entry,
#        and black on exit. If we see a gray node during our DFS, it must be part of a cycle. In a naive view, we'll
#        clear the colors between each search.
#        Logic : color = [WHITE] * nodeCount
#        def dfs(node):
#        if color[node] != WHITE:
#           return color[node] == BLACK
#        color[node] = GRAY
#        for nei in graph[node]:
#           if color[nei] == BLACK:
#               continue
#           if color[nei] == GRAY or not dfs(nei):
#               return False
#        color[node] = BLACK
#        return True
# Complexity : O(V + E)


def eventualSafeNodes(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    nodeCount = len(graph)
    color = [WHITE] * nodeCount

    def dfs(node):
        if color[node] != WHITE:
            return color[node] == BLACK

        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == BLACK:
                continue
            if color[nei] == GRAY or not dfs(nei):
                return False
        color[node] = BLACK
        return True

    result = []
    for node in range(nodeCount):
        if dfs(node):
            result.append(node)

    return result


if __name__ == "__main__":
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print eventualSafeNodes(graph)
