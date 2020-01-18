# Question : Sorted subsequence from a given array of size 3
# find A[i]<A[j]<A[k] where i<j<k

import sys


def function(array):
    print array
    array_size = len(array)

    small = sys.maxint
    large = sys.maxint
    bigger_found = False

    #  it will search until it gets A[i] < A[j] where i<j
    for i in range(0, array_size):
        if array[i] <= small:
            small = array[i]
            print 'small =', small

        elif array[i] <= large:
            large = array[i]
            print 'large =', large

        else:
            print 'breaking'
            bigger_found = True
            break;

    if not bigger_found:
        print 'no triplet found'
        return

    # some times the small make move towards right of large, so to bring back small we do this
    for j in range(0, i + 1):
        if array[j] <= large:
            small = array[j]
            break;

    print small, large, array[i]


if __name__ == '__main__':
    # array=[12, 11, 10, 5, 2, 6, 30]
    array = [5, 7, 4, 8]
    array = [1, 2, 1, 1, 3]
    array = [1, 1, 3]
    array_size = len(array)
    function(array)
