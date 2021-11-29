# Question : Find a pair in given array whose sum is equal to the given number
#
# Question Type : Easy
# Two methods are given below
# quick sort
# hashing
# TODO :: add used


def quickSort(array, start, end):
    # (complexity : n log n)
    if start < end:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)


def partition(array, left, right):
    while left < right:
        if array[left] < array[right]:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
        left += 1

    return left


def findTwoElements(array,num):
    # (complexity : n)
    left=0
    right=len(array)-1
    while left<right:
        if array[left] + array[right] == num:
            print('The two elements are',array[left],'and',array[right])
            return
        elif array[left] + array[right] < num:
            left+=1
        else:
            right-=1

    print('Pair not found')


# It checks the presence of required element
# The elements should be of known numbers
def hashMap(array,num):
    # (complexity : n, space complexity: max integer)
    constantMax = 100000
    binMap = [0]*constantMax

    for i in range(0,len(array)):
        if binMap[num-array[i]] == 1:
            print('The two elements are',array[i],'and',num-array[i])
            return
        binMap[array[i]]=1

    print('Pair not found')


if __name__ == '__main__':
    array = [1, 4, 45, 6, 10, -8]
    num = 16

    #method 1
    quickSort(array, 0, len(array) - 1)
    findTwoElements(array,num)

    #method 2
    hashMap(array, num)
