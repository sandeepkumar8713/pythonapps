# https://www.geeksforgeeks.org/xor-subarray-xors/
# Question : Given an array of integers, we need to get total XOR of all subarray XORs where
# subarray XOR can be obtained by XORing all elements of it.
#
# Input : arr[] = [3, 5, 2, 4, 6]
# Output : 7
# Total XOR of all subarray XORs is,
# (3) ^ (5) ^ (2) ^ (4) ^ (6) ^
# (3^5) ^ (5^2) ^ (2^4) ^ (4^6) ^
# (3^5^2) ^ (5^2^4) ^ (2^4^6) ^
# (3^5^2^4) ^ (5^2^4^6) ^
# (3^5^2^4^6) = 7
#
# Question Type : ShouldSee
# Used : Remember that xor of same values give 0, So even occurrences will cancel out and we only
#        have to care about odd occurrences. Number at i-th index will have (i + 1) * (N - i) frequency.
#        set res = 0
#        So run a loop over the input array, calculate its freq.
#           freq = (i + 1) * (n - i)
#           If freq is odd, do xor with res : res ^= inpArr[i]
#        return res
# Complexity : O(n)


def getTotalXorOfSubarrayXors(inpArr):
    res = 0

    # remember that xor of same values give 0, So even occurrences will cancel out and we only have to care about odd
    # occurrences
    n = len(inpArr)
    for i in range(n):
        freq = (i + 1) * (n - i)

        if freq % 2 == 1:
            res = res ^ inpArr[i]

    return res


if __name__ == "__main__":
    inpArr = [3, 5, 2, 4, 6]
    print(getTotalXorOfSubarrayXors(inpArr))
