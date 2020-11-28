# Question : We are given an array consisting of n elements. At each operation you can select any one element and
# increase rest of n-1 elements by 1. You have to make all elements equal performing such operation as many
# times you wish. Find the minimum number of operations needed for this.
#
# Input : arr[] = {1, 2, 3}
# Output : Minimum Operation = 3
# Explanation :
# operation | increased elements | after increment
#     1     |    1, 2            | 2, 3, 3
#     2     |    1, 2            | 3, 4, 3
#     3     |    1, 3            | 4, 4, 4
#
# Question Type : Easy, SimilarAdded
# Used :  If we took a closer look at each operation as well problem statement we will find that increasing
#         all n-1 element except the largest one is similar to decreasing the largest element only. So,
#         the smallest elements need not to decrease any more and rest of elements will got decremented
#         up to smallest one. In this way the total number of operation required for making all elements
#         equal will be arraySum - n * (smallestElement).
# Complexity :O(n)
# Take example of bar chart, where in each round the max bar is decremented by 1, till all are equal to min
# Since all should be equal to small, subtract small from each element and sum the result.


def minOp(arr):
    n = len(arr)
    arrSum = sum(arr)
    small = min(arr)

    return arrSum - (n * small)


if __name__ == "__main__":
    arr = [5, 6, 2, 4, 3]
    print(minOp(arr))
