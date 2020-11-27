# Question : Given two sorted arrays of size m and n respectively, you are tasked with finding the element
# that would be at the k'th position of the final sorted array.
#
# Input : Array 1 - 2 3 6 7 9
#         Array 2 - 1 4 8 10
#         k = 5
# Output : 6
# Explanation: The final sorted array would be -1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.
#
# Question Type : ShouldSee
# Used : We call a recursive function kthElement with input arr1,m,arr2,n,k.
#        If m > n, swap the input arrays and call again(Try to make n larger).
#        If k == 1, return min(arr1[0], arr2[0])
#        set i as min(m, k / 2), set j as j = min(n, k / 2)
#        If arr1[i - 1] > arr2[j - 1]: then search in arr1[0:m-1] and arr2[j:n-1], since we have found out the lowest j
#           else : search in arr1[i:m-1] and arr2[0:n-1], since we have found out the lowest i
#        kthElement(arr1, m, arr2, n, k):
#        if k > (m + n) or k < 1: return -1
#        if m > n:
#           return kthElement(arr2, n, arr1, m, k)
#        if m == 0:
#           return arr2[k - 1]
#        if k == 1:
#           return min(arr1[0], arr2[0])
#        i = min(m, k // 2)
#        j = min(n, k // 2)
#        if arr1[i - 1] > arr2[j - 1]: (all up and second half of down)
#           return kthElement(arr1, m, arr2[j:n-1], n - j, k - j)
#       else: (first half of up and all down)
#           return kthElement(arr1[i:m-1], m - i, arr2, n, k - i)
# Complexity : O(log k)


def kthElement(arr1, m, arr2, n, k):
    if k > (m + n) or k < 1:
        return -1

    if m > n:
        return kthElement(arr2, n, arr1, m, k)

    if m == 0:
        return arr2[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(m, k // 2)
    j = min(n, k // 2)

    if arr1[i - 1] > arr2[j - 1]:
        # Now we need to find only k - j th element since we have found out the lowest j
        return kthElement(arr1, m, arr2[j:n-1], n - j, k - j)
    else:
        # Now we need to find only k - ith element since we have found out the lowest i
        return kthElement(arr1[i:m-1], m - i, arr2, n, k - i)


if __name__ == "__main__":
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k = 5
    print("Kth element is:", kthElement(arr1, len(arr1), arr2, len(arr2), k))
