# https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/
# Question : Given an array of integers and a number k, write a function that returns true if given array can
# be divided into pairs such that sum of every pair is divisible by k.
#
# Input: arr[] = {9, 7, 5, 3},
#            k = 6
# Output: True
# We can divide array into (9, 3) and (7, 5). Sum of both of these pairs is a multiple of 6.
#
# Question Type : Generic
# Used : Loop over the input array and make a dict of remainder(key) with its frequency as value.
#        If remainder 0 is present in dict, then there should be even(to make pair) number of 0's else
#           return false
#        If remainder k/2 is is in dict, then there should be even number of k/2's else return false
#        Now loop through the keys of dict, for each remainder in dict, there should also be remainder - k
#            in dict else return false. If remainder - k is present in dict, its freq must be equal to
#            freq of remainder in dict else
#            return false.
#        If all above cases are passed return true.
# Complexity : O(n)


def isPairPossible(arr, k):
    remFreq = {}
    for ele in arr:
        remainder = ele % k
        if remainder in remFreq.keys():
            remFreq[remainder] += 1
        else:
            remFreq[remainder] = 1

    if 0 in remFreq.keys():
        if remFreq[0] % 2 != 0:
            return False

    if k/2 in remFreq.keys():
        if remFreq[k/2] % 2 != 0:
            return False

    for remainder in remFreq.keys():
        if remainder == 0:
            continue
        if k - remainder in remFreq.keys():
            if remFreq[remainder] != remFreq[k - remainder]:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    arr = [92, 75, 65, 48, 45, 35]
    k = 10
    print(isPairPossible(arr, k))

    arr = {9, 7, 5, 3}
    k = 6
    print(isPairPossible(arr, k))
