# Question : Given an array, print all sub arrays in the array which has sum 0.
#
# Input:  arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
# Output:
# Sub array found from Index 2 to 4
# Sub array found from Index 2 to 6
# Sub array found from Index 5 to 6
# Sub array found from Index 6 to 9
# Sub array found from Index 0 to 10
#
# Question Type : Generic
# Used : Initialize the result which is list of dict(startIndex : endIndex). Initialize dict
#        hasDict(sumSoFar:[indexes where sum ends]).
#        Loop over the elements in the input array and keep adding the elements to the sumSoFar. If the
#           sumSoFar is 0 append {0:i} to the result. If sumSoFar is already in the hashDict then there
#           exists at-least one sub array ending at i with 0 sum. So take the list of indexes for this
#           sum from the hashDict. Now iterate over this list and keep appending {index + 1: i} to the result.
#           Now append i to list of sumSoFar in hashDict, i.e. hashDict[sumSoFar].append(i)
#        findSubArray(arr):
#        for i in range(len(arr)):
#           sumSoFar += arr[i]
#           if sumSoFar == 0:
#               result.append({0: i})
#           if sumSoFar in hashDict:
#               vc = hashDict[sumSoFar]
#               for index in vc:
#                   result.append({index+1: i})
#               hashDict[sumSoFar].append(i)
#           else:
#               hashDict[sumSoFar] = [i]
#        return result
# Complexity : O(n^2) worst


def findSubArray(arr):
    hashDict = dict()
    result = []
    sumSoFar = 0
    for i in range(len(arr)):
        sumSoFar += arr[i]
        if sumSoFar == 0:
            result.append({0: i})

        # If sum already exists in the map there exists at-least one sub array ending at index i with 0 sum
        if sumSoFar in hashDict:
            vc = hashDict[sumSoFar]
            for index in vc:
                # print sumSoFar, index
                result.append({index+1: i})

            hashDict[sumSoFar].append(i)
        else:
            hashDict[sumSoFar] = [i]

    return result


if __name__ == "__main__":
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    # arr = [0, 0, 5, 5, 0, 0]
    # arr = [6, -1, -34, -2, 2, 4, 6, -12, 7]
    print(findSubArray(arr))
