# Question : Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace
# color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.
#
# Used : Given a matrix, start recursion from the given points, set the new pixel. After that recur for up, down, left,
#        right. Return condition: posX and posY should be within matrix. If current pixel is not old pixel return.
#        If new pixel is already set return.
# Complexity : O(n)


def floodFill(inputMat, posX, posY, oldPixel, newPixel):
    if posX < 0 or posX >= len(inputMat):
        return
    if posY < 0 or posY >= len(inputMat[0]):
        return
    if inputMat[posX][posY] != oldPixel:
        return
    if inputMat[posX][posY] == newPixel:
        return

    inputMat[posX][posY] = newPixel

    floodFill(inputMat, posX - 1, posY, oldPixel, newPixel)
    floodFill(inputMat, posX + 1, posY, oldPixel, newPixel)
    floodFill(inputMat, posX, posY - 1, oldPixel, newPixel)
    floodFill(inputMat, posX, posY + 1, oldPixel, newPixel)


if __name__ == "__main__":
    # inputMat = [[1, 2],
    #             [1, 2]]
    # posX = 1
    # posY = 1
    # newPixel = 3
    inputMat = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 1, 1],
                [1, 2, 2, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 2, 2, 0],
                [1, 1, 1, 1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1, 2, 2, 1]]
    posX = 4
    posY = 4
    newPixel = 3
    oldPixel = inputMat[posX][posY]
    floodFill(inputMat, posX, posY, oldPixel, newPixel)
    for item in inputMat:
        print item
