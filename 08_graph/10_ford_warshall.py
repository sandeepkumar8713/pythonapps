# Question : The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to
# find shortest distances between every pair of vertices in a given edge weighted directed Graph.
#
# Question Type : Easy
# Used : For every pair (i, j) of the source and destination vertices respectively, there are two possible cases.
#       k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j]
#       as it is.
#       k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j]
#       as dist[i][k] + dist[k][j].
# Complexity : O(n^3)


import sys
INF = sys.maxsize


def floydWarshall(mat):
    V = len(mat)

    dist = []
    for i in range(V):
        row = []
        for j in range(V):
            row.append(mat[i][j])
        dist.append(row)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


if __name__ == "__main__":
    mat = [[0, 5, INF, 10],
           [INF, 0, 3, INF],
           [INF, INF, 0, 1],
           [INF, INF, INF, 0]]

    resultDist = floydWarshall(mat)
    for row in resultDist:
        print(row)
