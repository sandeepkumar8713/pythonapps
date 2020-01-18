# https://leetcode.com/problems/redundant-connection/
# https://leetcode.com/problems/redundant-connection/discuss/418520/Easy-Python-Solution-(-Union-Find-)
# https://zhuhan0.blogspot.com/2017/07/leetcode-261-graph-valid-tree.html
# Question : In this problem, a tree is an undirected graph that is connected and has no cycles.
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one
# additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that
# already existed. The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v]
# with u < v, that represents an undirected edge connecting nodes u and v. Return an edge that can be removed so
# that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs
# last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
# Similar Question : Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of
# nodes), write a function to check whether these edges make up a valid tree.
# For example: Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0]and thus will not appear together in edges.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
#
# Used : Do union find on the edge, the one which is redundant will have same parent.
#        For the tree valid question: A tree is a graph that doesn't have a cycle. So we can use the same logic here.
#        There should not be redundant edges in tree.
#        Logic : def findRedundantConnection(edges):
#        def union(x, y):
#           xset = find(x)
#           yset = find(y)
#           if xset != yset:
#               parent[xset] = yset
#               return True
#           return False
#        def find(x):
#           if parent[x] == -1:
#               return x
#           return find(parent[x])
#        parent = [-1] * (len(edges) + 1)
#        for x, y in edges:
#           if not union(x, y):
#               return [x, y]
# Complexity : O(n)


def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """

    def union(x, y):
        xset = find(x)
        yset = find(y)
        if xset != yset:
            parent[xset] = yset
            return True
        return False

    def find(x):
        if parent[x] == -1:
            return x
        return find(parent[x])

    parent = [-1] * (len(edges) + 1)

    for x, y in edges:
        if not union(x, y):
            return [x, y]

    return None


if __name__ == "__main__":
    edges = [[1,2], [1,3], [2,3]]
    print findRedundantConnection(edges)

    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print findRedundantConnection(edges)

    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print findRedundantConnection(edges)

