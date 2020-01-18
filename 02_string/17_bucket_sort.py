# https://www.geeksforgeeks.org/bucket-sort-2/
# Question : Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider
# the following problem. Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are
# uniformly distributed across the range. How do we sort the numbers efficiently?
#
# Used : Make a list of buckets of size 10. Since the input is in range of 0.0 to 1.0, multiplying with 10 would give
#        values between 0 to 9. Use this value as index and distribute the elements of input array in these 10 buckets.
#        Sort each of the bucket individually.
#        index 0 bucket will contain value from 0.0 to 0.09, 1 -> 0.1 to 0.19, 2 -> 0.2 to 0.29
#        Merge these buckets into the input array.
# Complexity : O(10 * n * log n)


def bucketSort(arr, n):
    buckets = []
    bucketSize = 10
    for i in range(bucketSize):
        buckets.append([])

    for i in range(n):
        bucketIndex = int(bucketSize * arr[i])
        buckets[bucketIndex].append(arr[i])

    for bucket in buckets:
        bucket.sort()

    index = 0
    for bucket in buckets:
        for ele in bucket:
            arr[index] = ele
            index += 1


if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucketSort(arr, len(arr))
    print arr
