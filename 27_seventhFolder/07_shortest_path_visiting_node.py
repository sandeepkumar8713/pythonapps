# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Question : You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You
# are given an array graph where graph[i] is a list of all the nodes connected with node i by
# an edge. Return the length of the shortest path that visits every node. You may start and
# stop at any node, you may revisit nodes multiple times, and you may reuse edges.
#
# Example : Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
#
# Question Type : Generic
# Used : We have to use BFS with special node. Here node is tuple of nodeIndex
#        and bit vector of visited nodes. Before running BFS, insert all nodes with cost 0
#        in queue. During loop, return cost, when target visit bit vector is reached.
# Logic: for i in range(n):
#           node = (i, (0 | 1 << i))
#           queue.append((0, node))
#           visited.add(node)
#        targetVisit = (1 << n) - 1
#        while queue:
#           cost, node = queue.pop(0)
#           nodeIndex = node[0]
#           visitedNodes = node[1]
#           if visitedNodes == targetVisit:
#               return cost
#           for neig in graph[nodeIndex]:
#               nextVisitedNodes = visitedNodes | (1 << neig)
#               newNode = (neig, nextVisitedNodes)
#               if newNode in visited:
#                   continue
#               queue.append((cost + 1, newNode))
#               visited.add(node)
# Complexity : O(2 * n) because each node will be visited at most twice

def shortestPathLength(graph):
    n = len(graph)
    if n == 0:
        return 0

    queue = []
    visited = set()

    for i in range(n):
        # nodeIndex, visitedMask
        node = (i, (0 | 1 << i))
        # cost, node
        queue.append((0, node))
        visited.add(node)

    targetVisit = (1 << n) - 1
    minCost = 0

    while queue:
        cost, node = queue.pop(0)
        nodeIndex = node[0]
        visitedNodes = node[1]

        if visitedNodes == targetVisit:
            return cost

        for neig in graph[nodeIndex]:
            nextVisitedNodes = visitedNodes | (1 << neig)
            newNode = (neig, nextVisitedNodes)
            if newNode in visited:
                continue

            queue.append((cost + 1, newNode))
            visited.add(node)

    return minCost


if __name__ == "__main__":
    graph = [[1, 2, 3], [0], [0], [0]]
    print(shortestPathLength(graph))

    graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(shortestPathLength(graph))
