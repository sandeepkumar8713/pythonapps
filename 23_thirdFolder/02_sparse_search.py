# CTCI : Q10_05_Sparse_Search
# https://www.geeksforgeeks.org/sparse-search/
# Question : Given a sorted array of strings which is interspersed with empty strings,
# write a method to find the location of a given string.
#
# Used : We will use binary search with one difference. If mid == "", we will move mid closest non empty string which
#        can either on left or right side.
# Complexity : O(n) worst case


def sparseSearch(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) / 2
    if arr[mid] == '':
        left = mid - 1
        right = mid + 1

        while True:
            if left < low and right > high:
                return -1

            elif right <= high and arr[right] != '':
                mid = right
                break

            elif left >= low and arr[left] != '':
                mid = left
                break

            left -= 1
            right += 1

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return sparseSearch(arr, key, low, mid - 1)
    elif arr[mid] < key:
        return sparseSearch(arr, key, mid + 1, high)


if __name__ == '__main__':
    arr = ["for", "geeks", "", "", "", "", "ide", "practice", "", "", "", "quiz"]
    # arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    key = 'geeks'
    # key = 'ds'
    # key = "ball"
    low = 0
    high = len(arr) - 1
    print ("Found at : " + str(sparseSearch(arr, key, low, high)))
