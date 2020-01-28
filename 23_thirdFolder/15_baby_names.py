# CTCI : Q17_07_Baby_Names
# Question : Each year, the government releases a list of the 10,000 most common baby names
# and their frequencies (the number of babies with that name). The only problem with this is that
# some names have multiple spellings. For example, "John" and ''.Jon" are essentially the same name
# but would be listed separately in the list. Given two lists, one of names/frequencies and the other
# of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each
# name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
# Johnny are synonyms. (It is both transitive and symmetric.) In the final list, any name can be used
# as the "real" name.
#
# Question Type : Generic
# Used : Make a class node of name and freq.
#        Add nodes to the graph
#        Add edges between the synonym node.
#        Run DFS on each of the node which will give the total freq. Call this func on each node:
#        getComponentFrequency(node, visitedDict):
#           if visitedDict[node.name] is True:
#               return 0
#           visitedDict[node.name] = True
#           totalFreq = node.freq
#           for childNode in node.neighbor:
#               totalFreq += getComponentFrequency(childNode, visitedDict)
#           return totalFreq
# Complexity : O(V+E) count of vertex and edges


class Node:
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
        self.neighbor = []


class Graph:
    def __init__(self):
        self.map = dict()

    def addNode(self, name, freq):
        node = Node(name, freq)
        self.map[name] = node

    def addEdge(self, start, end):
        startNode = self.map[start]
        endNode = self.map[end]
        startNode.neighbor.append(endNode)
        endNode.neighbor.append(startNode)


def makeGraph(names, synonyms):
    graph = Graph()
    for key in names.keys():
        graph.addNode(key, names[key])

    for pair in synonyms:
        graph.addEdge(pair[0], pair[1])
    return graph


def getComponentFrequency(node, visitedDict):
    if visitedDict[node.name] is True:
        return 0
    visitedDict[node.name] = True
    totalFreq = node.freq
    for childNode in node.neighbor:
        totalFreq += getComponentFrequency(childNode, visitedDict)
    return totalFreq


def getTrueFrequencies(graph):
    map = graph.map
    visitedDict = dict()
    for key in map.keys():
        visitedDict[key] = False

    rootNames = dict()
    for key in map.keys():
        if visitedDict[key] is False:
            frequency = getComponentFrequency(map[key], visitedDict)
            rootNames[key] = frequency

    return rootNames


if __name__ == "__main__":
    names = dict()

    names["John"] = 3
    names["Jonathan"] = 4
    names["Johnny"] = 5
    names["Chris"] = 1
    names["Kris"] = 3
    names["Brian"] = 2
    names["Bryan"] = 4
    names["Carleton"] = 4

    synonyms = [["John", "Jonathan"],
     ["Jonathan", "Johnny"],
     ["Chris", "Kris"],
     ["Brian", "Bryan"]]

    graph = makeGraph(names, synonyms)
    print(getTrueFrequencies(graph))
