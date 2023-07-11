# https://leetcode.com/problems/clone-graph/
# Similar : 03_linkedList/14_clone_double_linked
# Question : Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# Question Type : SimilarAdded
# Used : Traverse the graph using DFS, while doing so make a map of key(int) and value(new Node)
#        Now traverse the neighbours, do dfs over on them and keep appending new nodes.
# Logic: dfs(node):
#        if node.val in nodeMap:
#           return nodeMap[node.val]
#        new_node = Node(node.val)
#        nodeMap[node.val] = new_node
#        for nei in node.neighbors:
#           new_node.neighbors.append(dfs(nei))
#        return new_node
# Complexity : O(n) where n is number of nodes


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


nodeMap = {}


def dfs(node):
    if node.val in nodeMap:
        return nodeMap[node.val]

    new_node = Node(node.val)
    nodeMap[node.val] = new_node

    for nei in node.neighbors:
        new_node.neighbors.append(dfs(nei))

    return new_node


def cloneGraph(node):
    if node:
        return dfs(node)
    else:
        None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors.append(node2)
    node1.neighbors.append(node4)

    node2.neighbors.append(node1)
    node2.neighbors.append(node3)

    node3.neighbors.append(node2)
    node3.neighbors.append(node4)

    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    print("old graph")
    print(node1.val)
    print(node1.neighbors[0].val)
    print(node1.neighbors[1].val)
    print(node1.neighbors[0].neighbors[1].val)

    newRoot = cloneGraph(node1)

    print("new graph")
    print(newRoot.val)
    print(newRoot.neighbors[0].val)
    print(newRoot.neighbors[1].val)
    print(newRoot.neighbors[0].neighbors[1].val)
