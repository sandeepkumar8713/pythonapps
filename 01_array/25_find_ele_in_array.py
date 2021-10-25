# https://www.geeksforgeeks.org/search-an-element-in-an-array-where-difference-between-adjacent-elements-is-1/
# Question : Given an array where difference between adjacent elements is 1, write an
# algorithm to search for an element in the array and return the position of the element
# (return the first occurrence).
#
# Let element to be searched be x
# Input: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}
#        x = 3
# Output: Element 3 found at index 7
#
# Question Type : Easy
# Used : The idea is to start comparing from the leftmost element and find the
#        difference between current array element and x. Let this difference be 'diff'.
#        From the given property of array, we always know that x must be at-least 'diff'
#        away, so instead of searching one by one, we jump 'diff'.
# Complexity : O(n) worst


def search(arr, n, x):
    i = 0
    while i < n:
        if arr[i] == x:
            return i

        # Jump the difference between current array element and x
        i = i + abs(arr[i] - x)

    print("number is not present!")
    return -1


if __name__ == "__main__":
    arr = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
    n = len(arr)
    x = 3
    print("Element", x, " is present at index ", search(arr, n, 3))
