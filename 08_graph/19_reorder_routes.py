# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
# Question : There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
# only one way to travel between two different cities (this network form a tree). Last year,
# The ministry of transport decided to orient the roads in one direction because they are
# too narrow. Roads are represented by connections where connections[i] = [ai, bi] represents
# a road from city ai to city bi. This year, there will be a big event in the capital (city 0),
# and many people want to travel to this city. Your task consists of reorienting some roads
# such that each city can visit the city 0. Return the minimum number of edges changed.
# It's guaranteed that each city can reach city 0 after reorder.
#
# Example : Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
#
# Question Type : ShouldSee
# Used : Make adjacency list and reverse adjacency list.
#        Maintain a visited list.
#        Do BFS from node 0, traverse the adj_list, for each new node update changes + 1 and add node in queue
#           traverse the rev_adj_list, for each new node, add node in queue
# Complexity : O(n + m) n is node count and m is edge count

from collections import defaultdict, deque


def minReorder(n, connections):
    # build adjacency list and reverse adjacency list
    adj_list = defaultdict(list)
    rev_adj_list = defaultdict(list)
    for u, v in connections:
        adj_list[u].append(v)
        rev_adj_list[v].append(u)

    # BFS traversal
    visited = set()
    queue = deque([0])
    changes = 0
    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                changes += 1
        for neighbor in rev_adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return changes


if __name__ == "__main__":
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print (minReorder(n, connections))
