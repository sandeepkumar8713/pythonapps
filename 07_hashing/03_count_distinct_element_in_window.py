# Question : Given an array A[] of size n and an integer k, your task is to complete the
# function countDistinct which prints the count of distinct numbers in all windows of
# size k in the array A[].
#
# Input:  arr[] = {1, 2, 1, 3, 4, 2, 3};
#             k = 4
# Output:
# 3
# 4
# 4
# 3
#
# Question Type : Asked
# Used : Loop over the input array from 0 to k-1 and keep record of elements and there
#        frequency in dict.
#        Print the length of dict.
#        Now loop over the input array form k to n-1 and reduce the frequency of last element
#        removed from window and increase the frequency of new element inserted in window.
#        Remove the element whose frequency is 0. Print the length of dict.
# Complexity : O(n)


def countDistinct(inpArr, k):
    distinctCount = {}
    for i in range(0, k):
        if inpArr[i] in distinctCount.keys():
            distinctCount[inpArr[i]] += 1
        else:
            distinctCount[inpArr[i]] = 1
    print(len(distinctCount))

    for i in range(k, len(inpArr)):
        if inpArr[i] in distinctCount.keys():
            distinctCount[inpArr[i]] += 1
        else:
            distinctCount[inpArr[i]] = 1

        distinctCount[inpArr[i - k]] -= 1
        if distinctCount[inpArr[i-k]] == 0:
            del distinctCount[inpArr[i-k]]

        print(len(distinctCount))


if __name__ == "__main__":
    inpArr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    countDistinct(inpArr, k)
