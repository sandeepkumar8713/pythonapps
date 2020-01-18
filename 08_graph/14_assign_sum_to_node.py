# https://www.careercup.com/question?id=5691748142546944
# Question : Given a fully connected graph with n nodes and corresponding values. One node can interact with other
# node at a time, to replace/ignore/add its value to other node's value. Assuming this operation takes 1 unit of
# time, how much time would it take for all the nodes to have value equal to sum of all the nodes.
#
# Examples : Given a graph with values {1,2,3,4}, find total time it takes, such that all nodes have value as 10.
#
# Used : Since the graph is fully connected. The idea is to take a node, iterate over all its adjacent nodes through
#        recursion and keep adding its sum. Once the end is reached. Rollback while updating the previously travelled
#        nodes.
#        Call the recursive function distributeSum(node, totalSum, index, n).
#           n5.data = distributeSum(n5, n5.data, 0, len(n5.adjacentNodes))
#        In the function if index == n : return totalSum
#           Add the current value to totalSum: totalSum += node.adjacentNodes[index].data
#           Call the function on next node and assign its return value to current note data
#               node.adjacentNodes[index].data = distributeSum(node, totalSum, index + 1, n)
#           return current data value: return node.adjacentNodes[index].data
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.adjacentNodes = []

    def connect(self, adjacentNode):
        if adjacentNode in self.adjacentNodes:
            return
        self.adjacentNodes.append(adjacentNode)
        adjacentNode.connect(self)


def distributeSum(node, totalSum, index, n):
    if index is n:
        return totalSum

    totalSum += node.adjacentNodes[index].data
    node.adjacentNodes[index].data = distributeSum(node, totalSum, index + 1, n)
    return node.adjacentNodes[index].data


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.connect(n2)
    n1.connect(n3)
    n1.connect(n4)
    n1.connect(n5)

    n2.connect(n3)
    n2.connect(n4)
    n2.connect(n5)

    n3.connect(n4)
    n3.connect(n5)

    n4.connect(n5)

    n5.data = distributeSum(n5, n5.data, 0, len(n5.adjacentNodes))

    print n1.data,
    for adjacentNode in n1.adjacentNodes:
        print adjacentNode.data,
