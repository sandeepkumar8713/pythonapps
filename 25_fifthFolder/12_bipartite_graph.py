# https://www.geeksforgeeks.org/bipartite-graph/
# https://www.geeksforgeeks.org/amazon-interview-experience-for-internship-on-campus-2/
# Question : A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U.
# In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and
# v to U. We can also say that there is no edge that connects vertices of same set. A bipartite graph is possible
# if the graph coloring is possible using two colors such that vertices in a set are colored with the same color.
# Note that it is possible to color a cycle graph with even cycle using two colors.
# There is an ant colony with n ants. And there will be a total of m interactions between ants.
# So, ( a colony will be good only if all the interactions were between opposite genders). We have been giving
# the interactions between ants, and we have to find out whether this colony can be good or not. for eg:-
# Input:
# 3 3
# 1 2
# 2 3
# 1 3
# So there are a total of 3 ants and 3 interactions. ant 1 interact with ant 2, 2 with 3, and 1 with 3. we have to
# tell whether this colony can be good or not. So here this colony can’t be good, as 1 interact with 2 and 3,
# so the gender of 2 and 3 should be the same, but 2 and 3 also interact so there is no possible way for this
# colony to be good
#
# Question Type : Generic
# Used : Maintain a color array of size n with 2 colors. Take one node as source and assign
#        1 color to it. Push this node in the queue. Do BFS over the graph using the queue.
#        While doing so, assign color to adjacent nodes. If we get a adjacent node whose color
#        is same, the return False.
#        If we come out of the loop, return True.
# Complexity : O(n)

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)]

    def isBipartite(self, src):

        # Create a color array to store colors assigned to all veritces. Vertex
        # number is used as index in this array. The value '-1' of colorArr[i] is used to
        # indicate that no color is assigned to vertex 'i'. The value 1 is used to indicate
        # first color is assigned and value 0 indicates second color is assigned.
        colorArr = [-1] * self.V

        colorArr[src] = 1
        queue = []
        queue.append(src)
        while queue:
            u = queue.pop()

            if self.graph[u][u] == 1:
                return False

            for v in range(self.V):

                # An edge from u to v exists and destination v is not colored
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    # Assign alternate color to this adjacent v of u
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)

                # An edge from u to v exists and destination v is colored with same color as u
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True


if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]
    print(g.isBipartite(0))

    g = Graph(3)
    g.graph = [[0, 1, 1],
               [0, 0, 1],
               [0, 0, 0]]
    print(g.isBipartite(0))
