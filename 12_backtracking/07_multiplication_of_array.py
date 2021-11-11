# https://www.careercup.com/question?id=5645649973346304
# Question : You are provided with 2D char array. You have to provide the 2D char array as response which contains the
# multiplication of the input array.
#
# For eg: input=> {{a,b},{c,d}}, output => {{a,c},{a,d},{b,c},{b,d}}
#
# Question Type : Easy
# Used : Call a recursive func multiplyArray(inpArr, outStr, i, rowSize) where i is the
#        row index of input matrix.
#        If i == rowSize: print outStr, return
#        Loop over all the character ch in this row.
#           Append ch to outStr.
#           Call multiplyArray again with i+1.
#           Now as the output string is already print, backtrack by removing the last appended ch.
#           outStr = outStr[:-1]
# Complexity : O(n^n)


def multiplyArray(inpArr, outStr, i, rowSize):
    if i == rowSize:
        print (outStr)
        return

    for ch in inpArr[i]:
        outStr += ch
        multiplyArray(inpArr, outStr, i+1, rowSize)
        # backtracking
        outStr = outStr[:-1]


if __name__ == "__main__":
    # inpMat = [['a', 'b'],
    #           ['c', 'd']]
    inpMat = [['a', 'b'],
              ['c', 'd', 'e'],
              ['f', 'g', 'h', 'i']]
    rowSize = len(inpMat)
    outStr = ""
    multiplyArray(inpMat, outStr, 0, rowSize)
