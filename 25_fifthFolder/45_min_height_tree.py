# https://leetcode.com/problems/minimum-height-trees/
# Question : Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
# edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi
# in the tree, you can choose any node of the tree as the root. When you select a node x as the root,
# the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))
# are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# Example : Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
#
# Question Type : ShouldSee
# Used : We have to trim the nodes, starting from nodes with indegree 1.
#        The nodes which are trimmed at last are the nodes suitable to be root.
#        Do BFS over the given node, starting from nodes whose indegree is 1.
#        During BFS, pop element from queue, append the nodes to the result.
#        Loop over the node's neighbours and reduce their indegree.
#        If neighbour's indgree is 1, append it to temp.
#        After popping all nodes from queue, if temp list has element,
#        add it to queue and reset the result list
#        If temp is empty, then there nothing to process, come out of the loop
#        and return result.
#        Logic :
#        for edge in edges:
#           x = edge[0], y = edge[1]
#           inDegrees[x] += 1, inDegrees[y] += 1
#           map[x].add(y), map[y].add(x)
#        while queue:
#           tmp = []
#           for item in queue:
#               result.append(item)
#               for i in map[item]:
#                   inDegrees[i] -= 1
#                   if inDegrees[i] == 1: tmp.append(i)
#           queue = tmp
#           if len(tmp) > 0: result = []
#        return result
# Complexity :

def findMinHeightTree(n, edges):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    map, inDegrees = [set() for i in range(n)], [0] * n
    for edge in edges:
        x = edge[0]
        y = edge[1]
        inDegrees[x] += 1
        inDegrees[y] += 1
        map[x].add(y)
        map[y].add(x)

    queue, result = [], []
    for i in range(n):
        if inDegrees[i] == 1:
            queue.append(i)

    while queue:
        tmp = []
        for item in queue:
            result.append(item)
            for i in map[item]:
                inDegrees[i] -= 1
                if inDegrees[i] == 1:
                    tmp.append(i)
        queue = tmp
        if len(tmp) > 0:
            result = []

    return result


if __name__ == "__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(findMinHeightTree(n, edges))

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(findMinHeightTree(n, edges))

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(findMinHeightTree(n, edges))
