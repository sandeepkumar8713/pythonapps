# CTCI : Q10_09_Sorted_Matrix_Search
# https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
# Question : Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.
#
# Question Type : Generic
# Used : while i < n and j >= 0:
#         if mat[i][j] == x: print "found"
#         if mat[i][j] > x: j -= 1
#         elif mat[i][j] < x: i += 1
#         print "not found"
# Complexity : O(m + n)


def search(mat, m, n, x):
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if mat[i][j] == x:
            print("Found at : " + str(i) + ", " + str(j))
            return

        if mat[i][j] > x:
            j -= 1

        elif mat[i][j] < x:
            i += 1
    print("Element not found")


if __name__ == "__main__":
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    search(mat, 4, 4, 29)
