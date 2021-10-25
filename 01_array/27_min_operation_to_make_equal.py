# https://www.geeksforgeeks.org/minimum-operation-make-elements-equal-array/
# Question : Given an array with n positive integers. We need to find the minimum number of
# operation to make all elements equal. We can perform addition, multiplication, subtraction or
# division with any element on an array element.
#
# Input : arr[] = {1, 2, 3, 4}
# Output : 3
# Since all elements are different, we need to perform at-least three operations to
# make them same. For example, we can make them all 1 by doing three subtractions.
# Or make them all 3 by doing three additions.
#
# Question Type : Easy
# Used : For making all elements equal you can select a target value and then you can
#        make all elements equal to that. Now, for converting a single element to target value
#        you can perform a single operation only once. In this manner you can achieve your task
#        in maximum of n operations but you have to minimize this number of operation
#        and for this your selection of target is very important because if you select a
#        target whose frequency in array is x then you have to perform only n-x more
#        operations as you have already x elements equal to your target value. So, finally
#        our task is reduced to finding element with maximum frequency.
#        return n - (maxFreq)
# Complexity : O(n)


def minOperation(arr, n):
    freqMap = dict()
    for ele in arr:
        if ele in freqMap.keys():
            freqMap[ele] += 1
        else:
            freqMap[ele] = 1

    maxFreq = 0
    for ch, freq in freqMap.items():
        if freq > maxFreq:
            maxFreq = freq

    return n - maxFreq


if __name__ == "__main__":
    arr = [1, 5, 2, 1, 3, 2, 1]
    n = len(arr)
    print(minOperation(arr, n))
