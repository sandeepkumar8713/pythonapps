# Question : Given a connected and undirected graph, a spanning tree of that graph is a sub graph that is a tree
# and connects all the vertices together. A single graph can have many different spanning trees. A minimum
# spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning
# tree with weight less than or equal to the weight of every other spanning tree.
#
# Question Type : Generic
# Used : Kruskal's Minimum Spanning Tree Algorithm
#        Sort the given edges. Make a list of result, parent and rank. Result is empty.
#        set parent as parent[i] = i and rank as rank[1 to n] = 0
#        Loop over the given edges. For the given edge, get it parents of its vertices. If parents are
#           not same, that means by considering this edge won't create a cycle. Add this edge in result
#           list and call union function to update rank of parent vertex if required.
#        print result array.
#        Logic :
#        while e < self.V - 1:
#           u, v, w = self.graph[i]
#           i = i + 1
#           x = self.find(parent, u)
#           y = self.find(parent, v)
#           if x != y:
#               e = e + 1
#               result.append([u, v, w])
#               self.union(parent, rank, x, y)
#        return result
#        Find function(i) :
#        if parent[i] = i return i else
#           call recursive find(parent[i]) to get its root ancestor.
#        Union function(u,v):
#        find parent of u and v, let it be xRoot and yRoot. If rank of xRoot is higher make it as parent
#        else vice versa. If rank of both are same, then make one as root and increment its rank by 1.
# Complexity : O(E Log E + E Log V) so O(n log n)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot

        # If ranks are same, then make one as root and increment its rank by one
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def KruskalMST(self):
        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # g = Graph(3)
    # g.addEdge(0, 1, 5)
    # g.addEdge(1, 2, 3)
    # g.addEdge(0, 2, 1)

    MST = g.KruskalMST()
    for item in MST:
        print(item[0], "->", item[1], " ", item[2])
