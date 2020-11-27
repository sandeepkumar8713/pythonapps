# Question : There are some glasses with equal capacity as 1 litre. This is Pascal triangle.
# The glasses are kept as follows:
#                    1
#                  2   3
#               4    5    6
#             7    8    9   10
#
# You can put water to only top glass. If you put more than 1 litre water to 1st glass, water overflows and fills
# equally in both 2nd and 3rd glasses. Glass 5 will get water from both 2nd glass and 3rd glass and so on. If you have
# X litre of water and you put that water in top glass, how much water will be contained by jth glass in ith row?
#
# Question Type : ShouldSee
# Used : Run 2 loops for rows and cols and distribute the water from first glass to the desired glass.
#        Return the amount in desired glass. If value is more than 1 then distribute the remaining water in
#        two half in 2 lower glasses.
#        findWater(i, j, K):
#        glass = [0] * ((i+1)*(i+2) // 2)
#        glass[0] = K, index = 0
#        for row in range(1, i+1, 1):
#           for col in range(1, row+1, 1):
#               X = glass[index]
#               if X > 1.0:
#                   glass[index] = 1.0
#                   X = X - 1.0
#               glass[index + row] += X/2
#               glass[index + row + 1] += X/2
#               index += 1
#        resIndex = i * (i - 1) // 2 + j - 1
#        print("resIndex: ", resIndex + 1)
#        return glass[resIndex]
# Complexity : O(m * n)


def findWater(i, j, K):
    glass = [0] * ((i+1)*(i+2) // 2)
    print(len(glass))
    glass[0] = K
    index = 0

    # Track the water flow
    for row in range(1, i+1, 1):
        for col in range(1, row+1, 1):
            X = glass[index]

            if X > 1.0:
                glass[index] = 1.0
                X = X - 1.0

            glass[index + row] += X/2
            glass[index + row + 1] += X/2
            index += 1

    resIndex = i * (i - 1) // 2 + j - 1
    print("resIndex: ", resIndex + 1)
    return glass[resIndex]


if __name__ == "__main__":
    i = 2
    j = 2
    K = 10.0
    print(findWater(i, j, K))
