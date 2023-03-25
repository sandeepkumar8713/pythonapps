# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
# Question : You are given an integer n. There is an undirected graph with n nodes,
# numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi]
# denotes that there exists an undirected edge connecting nodes ai and bi.
# Return the number of pairs of different nodes that are unreachable from each other.
#
# Example : Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
#
# Question Type : Generic
# Used : Run a loop over each node:
#           If not visited, find the count of nodes reachable from this node using DFS.
#           Find the count of pair reachable from this node and keep updating reachable_pair_count.
#        return total_pair_count - reachable_pair_count
# Complexity : O(n + m) n is node count and m is edge count


from collections import defaultdict


def countPairs(n, edges):
    # build adjacency list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # DFS traversal
    visited = set()
    def dfs(node):
        visited.add(node)
        count = 1
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                count += dfs(neighbor)
        return count

    # count unreachable pairs
    total_count = n * (n - 1) // 2
    reachable_count = 0
    for node in range(n):
        if node not in visited:
            count = dfs(node)
            reachable_count += count * (count - 1) // 2
    return total_count - reachable_count


if __name__ == "__main__":
    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    print (countPairs(n, edges))
