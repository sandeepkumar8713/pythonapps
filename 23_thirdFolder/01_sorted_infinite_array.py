# CTCI : Q10_04_Sorted_Search_No_Size
# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
# Question : Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
#
# Question Type : Easy
# Used : Set values as: l, h, val = 0, 1, arr[0]
#        while val < key:
#           l = h
#           h *= 2
#           val = arr[h]
#        Now we have the l and h between which key is. Do binary search over it.
# Complexity : O(log n)


def binary_search(arr,l,r,x):
    if r >= l:
        mid = l+(r-l) // 2
        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)

        return binary_search(arr,mid+1,r,x)

    return -1


def findPos(a, key):
    l, h, val = 0, 1, arr[0]

    while val < key:
        l = h		 # store previous high
        h *= 2		 # double high index
        val = arr[h]	 #update new val

    return binary_search(a, l, h, key)


if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    ans = findPos(arr,10)
    if ans == -1:
        print ("Element not found")
    else:
        print ("Element found at index : " + str(ans))
