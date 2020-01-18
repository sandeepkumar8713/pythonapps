# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# Question : Given an array of n distinct elements, find the minimum number of swaps required to sort the array.
#
# Used : Make a indexDict for key(element): value(index) for the input array. Sort the input array. Maintain a boolean
#        array to take care of visited elements. Maintain a global res to count all the swap.
#        Loop through the sorted array. If the element is already visited or its index is same as value in
#           indexDict(already at correct place) skip it.
#           Else take j=i and run 1 more loop while visited[j] = False. (loop while the swapping takes place). Based on
#               current element change the value of j to its swapped elements's index j = indexDict[ele]. Count the no.
#               of times this loop ran. Keep marking element at index as visited.
#           Add this counter to the global res
#        return res
# Complexity : O(n log n)


def minSwaps(inpArr):
    indexDict = dict()
    res = 0
    for i in range(len(inpArr)):
        ele = inpArr[i]
        indexDict[ele] = i
    sortedArr = sorted(inpArr)
    print indexDict

    visited = [False] * len(inpArr)
    for i in range(len(sortedArr)):
        ele = sortedArr[i]
        if visited[i] or indexDict[ele] is i:
            continue

        # find out the number of node in this cycle and add in ans
        cycleSize = 0
        j = i
        while visited[j] is False:
            visited[j] = True
            # The swap happens here
            ele = sortedArr[j]
            j = indexDict[ele]
            cycleSize += 1

        # Subtract 1 to manage for extra loop above
        res += cycleSize - 1

    return res


if __name__ == "__main__":
    inpArr = [1, 5, 4, 3, 2]
    # inpArr = [2, 4, 5, 1, 3]
    print minSwaps(inpArr)
