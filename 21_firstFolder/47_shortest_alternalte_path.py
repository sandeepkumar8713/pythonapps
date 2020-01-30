# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Question : Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red
# or blue, and there could be self-edges or parallel edges. Each [i, j] in red_edges denotes a red directed edge
# from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
# Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node
# X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).
#
# Example : Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
#
# Example 2: Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
#
# Question Type : Generic
# Used : Do BFS, continue with path only if next colour is different than previous color on this path. When an unvisited
#        node is encountered, update its distance in the result array.
#        Logic : def shortestAlternatingPaths(n, red_edges, blue_edges):
#        graph = dict()
#        for i, j in red_edges:
#           if i not in graph: graph[i] = [('r', j)]
#           else: graph[i].append(('r', j))
#        for i, j in blue_edges:
#           if i not in graph: graph[i] = [('b', j)]
#           else: graph[i].append(('b', j))
#        res = [-1] * n
#        q = [(None, 0, 0)]
#        visited = set()
#        while q:
#           last_color, v, dist = q.pop(0)
#           visited.add((last_color, v))
#           if res[v] == -1:
#               res[v] = dist
#           if v not in graph:
#               continue
#           for color, child in graph[v]:
#               if color == last_color or (color, child) in visited:
#                   continue
#               q.append((color, child, dist + 1))
#        return res
# Complexity : O(n)


def shortestAlternatingPaths(n, red_edges, blue_edges):
    graph = dict()

    for i, j in red_edges:
        if i not in graph:
            graph[i] = [('r', j)]
        else:
            graph[i].append(('r', j))

    for i, j in blue_edges:
        if i not in graph:
            graph[i] = [('b', j)]
        else:
            graph[i].append(('b', j))

    res = [-1] * n

    # BFS
    q = [(None, 0, 0)]  # record (color, a_node, shortest dist from node 0 to a_node)
    visited = set()  # record (color, vertex) visited
    while q:
        # visit all nodes in q
        last_color, v, dist = q.pop(0)
        visited.add((last_color, v))

        # specify the distance if hasn't been specified
        if res[v] == -1:
            res[v] = dist

        if v not in graph:
            continue

        # traverse all child nodes
        for color, child in graph[v]:

            # skip visited edges and edges with the same color as last edge
            if color == last_color or (color, child) in visited:
                continue

            # add child nodes to a new queue
            q.append((color, child, dist + 1))

    return res


if __name__ == "__main__":
    n = 3
    red_edges = [[0, 1], [1, 2]]
    blue_edges = []
    print(shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 3
    red_edges = [[0, 1]]
    blue_edges = [[2, 1]]
    print(shortestAlternatingPaths(n, red_edges, blue_edges))
