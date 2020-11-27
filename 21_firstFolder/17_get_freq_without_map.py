# https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
# Question : Given an unsorted array of n integers which can
# contain integers from 1 to n. Some elements can be repeated multiple times and some other elements can be
# absent from the array. Count frequency of all elements that are present and print the missing elements.
#
# Question Type : ShouldSee
# Used : Since we are sure that all values are <= n, use mode of n for each element to get the index,
#        and add n to it. It represents the count. To show the result divide each element by n
#        and index represent the corresponding number.
# Complexity : O(n)


def printFrequnecy(arr):
    # Every element should be range of 0 to n-1
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] - 1

    for i in range(n):
        arr[arr[i] % n] = arr[arr[i] % n] + n

    for i in range(n):
        print(i+1, ':', arr[i]/n)


if __name__ == "__main__":
    arr = [2, 3, 3, 2, 5]
    printFrequnecy(arr)
