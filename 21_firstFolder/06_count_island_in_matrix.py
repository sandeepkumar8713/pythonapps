# CTCI : Q16_19_Pond_Sizes
# https://www.geeksforgeeks.org/find-number-of-islands/
# http://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/
# https://leetcode.com/problems/number-of-islands/
# Similar : https://leetcode.com/problems/number-of-closed-islands/
# Program to count islands in boolean 2D matrix
# Question : Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
#
# For example, the below matrix contains 5 islands
# Input : mat[][] = {{1, 1, 0, 0, 0},
#                    {0, 1, 0, 0, 1},
#                    {1, 0, 0, 1, 1},
#                    {0, 0, 0, 0, 0},
#                    {1, 0, 1, 0, 1}
# Output : 5
#
# Question Type : Asked
# Used : Traverse the matrix as DFS till 1 is found and keep marking them as visited.
#        So keep track of non-visited cells and do DFS again. In doing so keep the count of DFS called.
#        While doing so also keep count of size of each island, to find max island size.
# Complexity : O(n^2)

import sys


class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.mat = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        return (0 <= i < self.ROW and 0 <= j < self.COL and
                not visited[i][j] and self.mat[i][j])

    # A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, nodeCount):
        # These arrays are used to get row and column numbers of 8 neighbours of a given cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True
        nodeCount[0] += 1

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited, nodeCount)

    # The main function that returns count of islands in a given boolean 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and traverse through the all cells of given matrix
        count = 0

        maxNodeCount = -sys.maxsize
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,then new island found
                if not visited[i][j] and self.mat[i][j] == 1:
                    # Visit all cells in this island and increment island count
                    nodeCount = [0]
                    self.DFS(i, j, visited, nodeCount)
                    count += 1

                    if nodeCount[0] > maxNodeCount:
                        maxNodeCount = nodeCount[0]

        return count, maxNodeCount


if __name__ == "__main__":
    mat = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1]]

    row = len(mat)
    col = len(mat[0])
    g = Graph(row, col, mat)
    count, maxNodeCount = g.countIslands()
    print("Number of islands is and largest island count : " + str(count) + ", " + str(maxNodeCount))
