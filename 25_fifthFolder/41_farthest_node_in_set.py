# Question : Given an undirected graph and a set of nodes A, write a function which
# returns all nodes in G furthest from any node a in A.
#
# Example : Input : graph: {a, b, c, d} nodes: {a, b}
#           edges : a -> c: 1, b -> c: 2, a -> d: 2, b -> d: 2
# output : {d}
#
# Question Type : Asked
# Used : For node in nodes list, run Dijkstras algo but for longest distance.
#        Using this we will get max dist array.
#        Check which is common in all the arrays and return that.
# Complexity : O(e + v log v)
#
# TODO :: add code
#
