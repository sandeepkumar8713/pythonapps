# https://leetcode.com/problems/bus-routes/
# Question : You are given an array routes representing bus routes where routes[i] is a bus
# route that the ith bus repeats forever.
# Example : if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence
# 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to
# go to the bus stop target. You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target. Return -1
# if it is not possible.
#
# Example : Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
#
# Question Type : Generic
# Used : Make a graph(dict), key is bus stop(node) and value is list of busId which stops at bus stand.
#        Now do BFS over busId.
#        For the given source, append all the busId's passing through that bus stop.
#        Keep looping while queue is not empty. Also keep count of busId's changed.
#        When target is reached, return change count.
#        Note : Here busId is treated as node while doing BFS, not bus stop.
#        Logic :
#        for i in range(len(routes)):
#           route = routes[i]
#           for node in route:
#               graph[node] = graph.get(node, []) + [i]
#        for busId in graph[source]:
#           que.append((busId, 1))
#           visited.add(busId)
#        while que:
#           busId, res = que.pop(0)
#           for node in routes[busId]:
#               if node == target: return res
#               if len(graph[node]) == 1: continue
#               for nxt in graph[node]:
#                   if nxt not in visited:
#                       visited.add(nxt)
#                       que.append((nxt, res + 1))
#        return -1
# Complexity : O(V+E) & O(V)


def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    graph = {}
    for i in range(len(routes)):
        route = routes[i]
        for node in route:
            graph[node] = graph.get(node, []) + [i]

    if target not in graph or source not in graph:
        return -1

    que = []
    visited = set()

    for busId in graph[source]:
        que.append((busId, 1))
        visited.add(busId)

    while que:
        busId, res = que.pop(0)
        for node in routes[busId]:
            if node == target:
                return res

            if len(graph[node]) == 1:
                continue

            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    que.append((nxt, res + 1))

    return -1


if __name__ == "__main__":
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    print(numBusesToDestination(routes, source, target))

    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12
    print(numBusesToDestination(routes, source, target))
