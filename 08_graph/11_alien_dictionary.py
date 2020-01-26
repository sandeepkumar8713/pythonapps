# CTCI : Q4_07_Build_Order (similar)
# http://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
# Question : Given a sorted dictionary (array of words) of an alien language of size n, find order of characters
# in the language.
#
# Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
# Output: Order of characters is 'b', 'd', 'a', 'c'
#
# Question Type : Generic
# Used : Create a graph g with number of vertices equal to the size of alphabet in the given alien language.
#        Loop over the elements of input array. Such that word1 = inpArr[i] and  word2 = inpArr[i+1]
#           One by one compare characters of both words and find the first mismatching characters.
#           Create an edge in g from mismatching character of word1 to that of word2.
#           break
#       Print topological sorting of the above created graph.
#
#       Topological sorting : Maintain an empty stack. Loop over the vertices of the graph and call recursive function
#       DFSUtils for unvisited vertices.
#           In DFSUtils loop over the connected vertices and again call DFSUtils over each
#           of them. After the loop got over push this input vertex in stack.
#       Once DFSUtils is call over all the unvisited vertices. Pop elements from the stack and print it.
# Complexity : O(n + aplhaCount)


class Graph:
    def __init__(self, n):
        self.V = n
        # key : list
        self.graph = dict()
        for i in range(n):
            self.graph[i] = []

    def addEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def DFSUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if visited[i] is False:
                self.DFSUtil(i, visited, stack)

        while stack:
            vertex = stack.pop()
            print(chr(vertex + ord('a')),end=" ")


def getOrder(inpArr, alphaCount):
    g = Graph(alphaCount)

    for i in range(0, len(inpArr)-1):
        word1 = inpArr[i]
        word2 = inpArr[i+1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                g.addEdge(ord(word1[j]) - ord('a'), ord(word2[j]) - ord('a'))
                break

    g.topologicalSort()


if __name__ == "__main__":
    # words = ["caa", "aaa", "aab"]
    # alphaCount = 3
    words = ["baa", "abcd", "abca", "cab", "cad"]
    alphaCount = 4
    getOrder(words, alphaCount)
