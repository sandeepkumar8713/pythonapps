# https://en.wikipedia.org/wiki/Radix_sort
# Question : MSD radix sorts use lexicographic order, which is suitable for sorting strings, such as words, or
# fixed-length integer representations. A sequence such as "b, c, d, e, f, g, h, i, j, ba" would be
# lexicographically sorted as "b, ba, c, d, e, f, g, h, i, j".
#
# Question Type : Generic
# Used : Call recursive function radixSort(inpArr, index) with index 0.
#        Make a list of buckets of size 26. Loop over each of the input element.
#        If index in lesser than size of string send it to the appropriate bucket using char at index.
#        Else push the string in the inpArr.
#        Run a loop over all the buckets and call radixSort() of those buckets whose length is more than 0.
#        Merge these buckets into the input array.
# Complexity : O(w * n)


def radixSort(inpArr, index):
    buckets = []
    for i in range(26):
        buckets.append([])

    newStart = 0
    for ele in inpArr:
        if index <= len(ele)-1:
            char = ele[index]
            # Drop the number into the correct bucket
            buckets[ord(char) - ord('a')].append(ele)
        else:
            inpArr[newStart] = ele
            newStart += 1

    for bucket in buckets:
        if len(bucket) != 0:
            radixSort(bucket, index+1)

    i = 0
    for bucket in buckets:
        for ele in bucket:
            inpArr[newStart + i] = ele
            i += 1


if __name__ == "__main__":
    arr = ["sandeep", "suresh", "rohit", "kamlesh", "bhavin", "rajat"]
    radixSort(arr, 0)
    print(arr)

    arr = ["b", "c", "d", "e", "h", "g", "b", "f", "i", "j", "bc", "ba", "b"]
    radixSort(arr, 0)
    print(arr)
