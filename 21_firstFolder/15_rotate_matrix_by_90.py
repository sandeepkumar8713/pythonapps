# https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/
# Question : Rotate matrix by 90, 180 , 270 in anti clockwise.
#
# Used : Use transpose and reverse the columns for 90
#        Exchange i & row - i and j and col - j for 180
#        Use transpose and reverse the rows for 270
# Complexity : O(n^2)


# list is pass by reference
def transpose(mat):
    for i in range(0, len(mat)):
        for j in range(i, len(mat[0])):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp


def reverseColumns(mat):
    row = len(mat)
    col = len(mat[0])
    for j in range(0, col):
        for i in range(0, row/2):
            start = i
            end = row - start - 1
            if end < row:
                temp = mat[start][j]
                mat[start][j] = mat[end][j]
                mat[end][j] = temp


def reverseRows(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(0,row):
        for j in range(0,col/2):
            start = j
            end = col - start - 1
            if end < col:
                temp = mat[i][start]
                mat[i][start] = mat[i][end]
                mat[i][end] = temp


def rotate90(mat):
    transpose(mat)
    reverseColumns(mat)
    # if rotate 90 clockwise do revere row


def rotate180(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(0, row):
        for j in range(0, col/2):
            temp = mat[i][j]
            mat[i][j] = mat[row-i-1][col-j-1]
            mat[row-i-1][col-j-1] = temp


def rotate270(mat):
    transpose(mat)
    reverseRows(mat)


if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    rotate90(mat)
    # rotate180(mat)
    # rotate270(mat)
    for item in mat:
        print item
