# https://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/
# Question : You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and
# length l. You task is to create a stack of boxes which is as tall as possible, but you can only stack a box on
# top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of
# the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base. It is also
# allowable to use multiple instances of the same type of box. You task is to complete the function
# maxHeight which returns the height of the highest possible stack so formed.
#
# longest incraesing subsequence
# Question Type : SimilarAdded
# Used : sort based on 2d area in decreasing order and then the problem becomes LIS
#        Logic : def boxStacking(array):
#        height, twoDPlane = cubeDimension(array)
#        height, twoDPlane = sortBasedOnArea(height, twoDPlane)
#        heightArray = []
#        for i in range(0, len(height)):
#           heightArray.append(height[i])
#        for i in range(0, len(height)):
#           for j in range(0, i):
#               if (compareDimension(twoDPlane[i], twoDPlane[j])):
#                   if heightArray[i] < heightArray[j] + height[i]:
#                     heightArray[i] = heightArray[j] + height[i]
#        return max(heightArray)
# Complexity : O(n^2)


def cubeDimension(array):
    height = [0]*len(array)*2
    twoDPlane = [[0]*2]*len(array)*2
    count = 0
    for i in range(0, len(array), 3):
        subarray = array[i:i+3]
        for j in range(0,3):
            height[i*2 + j*2] = subarray[(0+j)%3]
            height[i*2 + j*2 + 1] = subarray[(0 + j) % 3]

            twoDPlane[i*2 + j*2] = [subarray[(1 + j) % 3],subarray[(2 + j) % 3]]
            twoDPlane[i*2 + j*2 + 1] = [subarray[(2 + j) % 3], subarray[(1 + j) % 3]]
        count += 1

    showDimension(height, twoDPlane)
    return height,twoDPlane


def showDimension(height,twoDPlane):
    for i in range(len(height)):
        # print height[i],twoDPlane[i]
        pass


def showMatrix(matrix):
    for item in matrix:
        # print item
        pass


def compareDimension(pair1,pair2):
    if pair1[0]<pair2[0] and pair1[1]<pair2[1]:
        #print pair1, pair2
        return True
    return False


def sortBasedOnArea(height,twoDPlane):
    arrayTobeSorted = []
    for item in twoDPlane:
        arrayTobeSorted.append(item[0]*item[1])

    sortedIndices=[i[0] for i in sorted(enumerate(arrayTobeSorted), key=lambda x: x[1])]

    #decreasing value
    sortedtwoDplane = []
    sortedHeight = []
    for item in sortedIndices:
        sortedtwoDplane.insert(0,twoDPlane[item])
        sortedHeight.insert(0,height[item])

    return sortedHeight,sortedtwoDplane


def boxStacking(array):
    height,twoDPlane = cubeDimension(array)
    #print(twoDPlane)
    height, twoDPlane = sortBasedOnArea(height, twoDPlane)

    heightArray = []
    for i in range(0, len(height)):
        heightArray.append(height[i])

    for i in range(0, len(height)):
        for j in range(0, i):
            if (compareDimension(twoDPlane[i], twoDPlane[j])):
                if heightArray[i] < heightArray[j] + height[i]:
                    heightArray[i] = heightArray[j] + height[i]

    return max(heightArray)


if __name__ == "__main__":
    #dimension = [1,2,3,4,5,6,3,4,1]
    dimension = [4,6,7,1,2,3,4,5,6,10,12,32]
    #dimension = [1,2,3,4,5,6]
    #dimension = [1,2,3]
    #print(dimension)
    print(boxStacking(dimension))
