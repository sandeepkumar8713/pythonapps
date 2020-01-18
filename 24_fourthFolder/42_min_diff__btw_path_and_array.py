# https://leetcode.com/discuss/interview-question/378687/google-onsite-min-diff-between-given-path-and-path-in-the-graph
# Question : Given a graph whose nodes are 3-letter words and an array of 3-letter words. Find a path in the graph
# such that the difference b/w words in the path and given array is minimum.
#
# Example : Input: G, arr = [AAA, BBB, CCC, DDD]
# Output: 2
# Explanation: The path [AAA, BBC, CCD, DDD] is closest to given array.
# In path, BBC differs from BBB by 1 and CCD differs from CCC by 1 hence answer is 1 + 1 = 2.
#
# Used : We are going to use bfs with min heap. While doing bfs, for each node in queue, we try to find next node,
#        which has the least difference from the node in given array. We return when resultant array length is equal
#        to given array length.
#        Logic : minDiffPath(G, path):
#        n, pq, seen = len(path), [], {}
#        for node in G.listAllNodes():
#           diff = getDiffBetweenNodes(node, path[0])
#           seen[(node, 1)] = diff
#           heappush(pq, (diff, -1, [node]))
#        while pq:
#           D, L, seq = heappop(pq)
#           L = -L
#           if L == n: return D, seq
#           if D > seen.get((seq[-1], L), sys.maxint): continue
#           for nb in G.getNeighbors(seq[-1]):
#               d = getDiffBetweenNodes(nb, path[L])
#               if D + d >= seen.get((nb, L + 1), sys.maxint): continue
#               seen[(nb, L + 1)] = D + d
#               heappush(pq, (D + d, -(L + 1), seq + [nb]))
# Complexity : O(n log n)


import sys
from heapq import heappush, heappop
from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.G = defaultdict(set)
        for a, b in edges:
            self.G[a].add(b)
            self.G[b].add(a)

    def getNeighbors(self, node):
        return self.G.get(node)

    def listAllNodes(self):
        return list(self.G.keys())


def getDiffBetweenNodes(Node1, Node2):
    diffCount = 0
    for char1, char2 in zip(Node1, Node2):
        if char1 != char2:
            diffCount += 1

    return diffCount


def minDiffPath(G, path):
    if not path:
        return 0

    # seen[(node, L)] = minimum diff so far for a length-L path ended with node

    n, pq, seen = len(path), [], {}
    for node in G.listAllNodes():
        diff = getDiffBetweenNodes(node, path[0])
        seen[(node, 1)] = diff
        # push (diff, minus length, partial path) so that smaller diff, longer path comes first
        heappush(pq, (diff, -1, [node]))

    while pq:
        # pop the partial path with smallest diff
        D, L, seq = heappop(pq)
        L = -L
        # if the partial path has same length with given path, return
        if L == n:
            return D, seq

        # if the parital path is already not optimal, skip it. Its like reaching the node seq[-1] from a different path.
        if D > seen.get((seq[-1], L), sys.maxint):
            continue

        # otherwise consider all next nodes, push to the heap
        for nb in G.getNeighbors(seq[-1]):
            d = getDiffBetweenNodes(nb, path[L])
            # if length-(L + 1) partial path ended with nb
            # has larger or equal diff than previous visited
            # path, ignore it
            if D + d >= seen.get((nb, L + 1), sys.maxint):
                continue

            # otherwise update the cache, push to the heap
            seen[(nb, L + 1)] = D + d
            heappush(pq, (D + d, -(L + 1), seq + [nb]))

    return -1, None


if __name__ == "__main__":
    edges = [('BBB', 'EDD'), ('BBB', 'AAA'), ('EDD', 'DDD'),
             ('AAA', 'DDD'), ('AAA', 'XXX'), ('AAA', 'BBC'),
             ('DDD', 'CCD'), ('BBC', 'CCD'), ('XXX', 'CCD')]

    G = Graph(edges)
    path1 = ['AAA', 'BBB', 'CCC', 'DDD']
    path2 = ['AAA', 'CCC', 'AAA', 'BBD']
    print(minDiffPath(G, path1))
    print(minDiffPath(G, path2))
