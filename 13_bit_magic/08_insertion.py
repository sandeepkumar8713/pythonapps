# CTCI : Q5_01_Insertion
# Question : Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j(ith bit starting with
# zero). Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the
# bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
# fit between bit 3 and bit 2.
#
# Example :
# Input: N = 10000000001, M = 10011, i = 2, j = 6
# Output : 10001001101
#
# Question Type : Generic
# Used : Clear the bits j through i in N using a mask
#        Shift M so that it lines up with bits j through i
#        Merge M and N.
#
#        Mask : (~0 << j+1) | ((1 << i) - 1)
# Complexity : O(n)


def insert(N, M, i ,j):
    allOnes = ~0
    left = allOnes << (j + 1)
    right = (1 << i) - 1

    mask = left | right
    n_cleared = N & mask
    m_shifted = M << i

    return n_cleared | m_shifted


if __name__ == "__main__":
    N = 1025
    M = 19
    i = 2
    j = 6

    result = insert(N, M, i, j)
    print("N : " + bin(N))
    print("M : " + bin(M))
    print("Result : " + bin(result))
