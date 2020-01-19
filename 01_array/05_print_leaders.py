# Question : Write a program to print all the LEADERS in the array. An element is leader if it is greater than
# all the elements to its right side. The rightmost element is always a leader.
# Follow up Given an array of integers, replace every element with the next greatest element (greatest element
# on the right side) in the array. Since there is no element next to the last element, replace it with -1.
# For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
#
# Question Type : ShouldSee
# Used : Scan all the elements from right to left in array and keep track of maximum till now. When maximum changes
#        it's value, print it.
# Complexity : O(n)


def printLeaders(arr, size):
    max_from_right = arr[size - 1]
    print(max_from_right)
    for i in range(size - 2, 0, -1):
        if max_from_right < arr[i]:
            print(arr[i])
            max_from_right = arr[i]


def nextGreatest(arr):
    size = len(arr)
    max_from_right = arr[size - 1]
    arr[size - 1] = -1

    for i in range(size - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_from_right

        if max_from_right < temp:
            max_from_right = temp


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    printLeaders(arr, len(arr))
    print("")
    nextGreatest(arr)
    print(arr)
