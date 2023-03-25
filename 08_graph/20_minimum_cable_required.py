# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
# Question : There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [ai, bi] represents a connection between
# computers ai and bi. Any computer can reach any other computer directly or indirectly through
# the network. You are given an initial computer network connections. You can extract certain
# cables between two directly connected computers, and place them between any pair of
# disconnected computers to make them directly connected. Return the minimum number of
# times you need to do this in order to make all the computers connected.
# If it is not possible, return -1.
#
# Example : Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
#
# Question Type : ShouldSee
# Used : Using DFS find count of connected component.
#        num_cables = len(connections), minimum_cables_required = n - 1
#        if num_cables < minimum_cables_required:
#           return -1
#        if num_components - 1 > num_cables:
#           return -1
#        return num_components - 1
# Complexity : O(n + m) n is node count and m is edge count

from collections import defaultdict


def makeConnected(n, connections):
    num_cables = len(connections)
    minimum_cables_required = n - 1
    if num_cables < minimum_cables_required:
        return -1

    # build adjacency list
    adj_list = defaultdict(list)
    for u, v in connections:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # DFS traversal
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # count connected components
    num_components = 0
    for node in range(n):
        if node not in visited:
            dfs(node)
            num_components += 1

    # calculate minimum number of cables needed
    if num_components - 1 > num_cables:
        return -1
    else:
        return num_components - 1


if __name__ == "__main__":
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
    print (makeConnected(n, connections))
