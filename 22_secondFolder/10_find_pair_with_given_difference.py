# https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/
# Question : Given an unsorted array and a number n, find if there exists a pair of
# elements in the array whose difference is n.
#
# Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
# Output: Pair Found: (2, 80)
#
# Question Type : Easy
# Used : Sort the given input array.
#        Take 2 pointers i = 0 and j = 1.
#        Loop while i < n and j < n:
#           if i != j and arr[j] - arr[i] == diff: return True
#           Else if arr[j] - arr[i] < diff : j++
#           Else i++  (i.e. if calculated diff is less than target, increase right else left)
#        If we come out if loop, return False
# Complexity : O(n log n)


def findPair(arr, diff):
    n = len(arr)
    i = 0
    j = 1
    while i < n and j < n:
        if i != j and arr[j] - arr[i] == diff:
            print("Pair found", arr[i], arr[j])
            return True

        elif arr[j] - arr[i] < diff:
            j += 1
        else:
            i += 1
    print("No pair found")
    return False


if __name__ == "__main__":
    arr = [1, 8, 30, 40, 100]
    diff = 60
    findPair(sorted(arr), diff)

    arr = [5, 20, 3, 2, 50, 80]
    diff = 78
    findPair(sorted(arr), diff)
