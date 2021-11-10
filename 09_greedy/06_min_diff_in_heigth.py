# Question : Given heights of n towers and a value k. We need to either increase or decrease
# height of every tower by k (only once) where k > 0. The task is to minimize the difference
# between the heights of the longest and the shortest tower after modifications,
# and output this difference.
#
# Input  : arr[] = {1, 15, 10}, k = 6
# Output :  Maximum difference is 5.
# Explanation : We change 1 to 6, 15 to 9 and 10 to 4. Maximum difference is 5 (between 4 and 9).
#
# Question Type : ShouldSee
# Used : Sort the given input array. Set res as diff of first and last element.
#        Set largest as a[n] - k and smallest as a[0] + k. Swap if smallest is bigger.
#        Now loop over the input array from 0 to n-2. Try to choose each element as either
#           as smallest or largest by incrementing and decrementing by k. If subtracted value
#           is more than smallest or added value is lesser than largest then skip this element.
#           Else try to check whether choosing subtracted as smallest or added as largest,
#           which one gives smaller diff and update accordingly.
#       return min(res, largest - smallest)
# Complexity : O(n log n)


def getMinDiff(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    arr.sort()
    ans = arr[n - 1] - arr[0]
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    if smallest > largest:
        smallest, largest = largest, smallest

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k

        # This element should be lesser than small or bigger element than big else continue
        if subtract >= smallest or add <= largest:
            continue

        # Here we check which one gives lesser diff, subtract or small
        if largest - subtract <= add - smallest:
            smallest = subtract
        else:
            largest = add

    return min(ans, largest - smallest)


if __name__ == "__main__":
    # inpArr = [4, 6]
    # k = 10
    inpArr = [1, 5, 8, 10]
    k = 2
    # inpArr = [3, 9, 12, 16, 20]
    # k = 3
    # inpArr = [100, 150, 200, 250, 300, 400]
    # k = 4
    print("Maximum difference is:", getMinDiff(inpArr, k))
