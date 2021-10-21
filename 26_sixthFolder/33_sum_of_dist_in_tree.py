# https://leetcode.com/problems/sum-of-distances-in-tree/
# Question : There is an undirected connected tree with n nodes labeled from 0 to n - 1 and
# n - 1 edges. You are given the integer n and the array edges where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the tree. Return an array
# answer of length n where answer[i] is the sum of the distances between the ith node
# in the tree and all other nodes.
#
# Example :
#      0
#    /  \
#   1    2
#      / | \
#     3  4  5
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
#
# Question Type : Generic
# Used : depth of node : how far it is from root
#        weight of node: how many nodes in subtree for given node (including self)
#        For root node sum of depth of all nodes is ans.
#        Now using this ans we will calculate ans for other nodes.
#        The answer for a node is the same as the answer for it's parent (w) except it is one unit distance
#        closer to all the members of its subtree (- weights[node]) and it is one unit farther away from
#        every node in the graph that is not in its subtree (+ N - weights[node]).
#        Logic :
#        def dfs(adjMap, weights, depths, node, parent, depth):
#        ans = 1
#        for neib in adjMap[node]:
#           if neib != parent:
#               ans += dfs(adjMap, weights, depths, neib, node, depth + 1)
#        weights[node] = ans
#        depths[node] = depth
#        return ans
#        def dfs2(adjMap, weights, ans, node, parent, w):
#        nodeCount = len(adjMap)
#        ans[node] = w
#        for neib in adjMap[node]:
#           if neib != parent:
#               dfs2(adjMap, weights, ans, neib, node, w + nodeCount - 2 * weights[neib])
#
#        dfs(adjMap, weights, depths, 0, -1, 0)
#        dfs2(adjMap, weights, ans, 0, -1, sum(depths))
# Complexity :


def dfs(adjMap, weights, depths, node, parent, depth):
    ans = 1
    for neib in adjMap[node]:
        if neib != parent:
            ans += dfs(adjMap, weights, depths, neib, node, depth + 1)
    weights[node] = ans
    depths[node] = depth
    return ans


def dfs2(adjMap, weights, ans, node, parent, w):
    nodeCount = len(adjMap)
    ans[node] = w
    for neib in adjMap[node]:
        if neib != parent:
            dfs2(adjMap, weights, ans, neib, node, w + nodeCount - 2 * weights[neib])


def sumOfDistancesInTree(nodeCount, edges):
    adjMap = dict()

    for i, j in edges:
        adjMap[i] = adjMap.get(i, set()) | {j}
        adjMap[j] = adjMap.get(j, set()) | {i}

    weights, depths, ans = [0] * nodeCount, [0] * nodeCount, [0] * nodeCount

    dfs(adjMap, weights, depths, 0, -1, 0)
    dfs2(adjMap, weights, ans, 0, -1, sum(depths))

    return ans


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(sumOfDistancesInTree(n, edges))

    n = 2
    edges = [[1, 0]]
    print(sumOfDistancesInTree(n, edges))

