# https://www.geeksforgeeks.org/number-subsequences-form-ai-bj-ck/
# Question : Given a string, count number of subsequences of the form aibjck, i.e., it consists of i 'a' characters,
# followed by j 'b' characters, followed by k 'c' characters where i >= 1, j >=1 and k >= 1.
#
# Input  : aaabc
# Output : 7
# Subsequences are abc, abc, abc, aabc, aabc, aabc and aaabc
#
# Input  : abbc
# Output : 3
# Subsequences are abc, abc and abbc
#
# Input  : abcabc
# Output : 7
# Subsequences are abc, abc, abbc, aabc, abcc, abc and abc
#
# Used : Loop over each element in string:
#           if ch == 'a': aCount = (1 + 2 * aCount)
#           elif ch == 'b': bCount = aCount + 2 * bCount
#           elif ch == 'c': cCount = bCount + 2 * cCount
#        return cCount
# Complexity : O(n)


def countSubsequences(inpStr):
    aCount = 0
    bCount = 0
    cCount = 0

    for ch in inpStr:
#    If current  character is 'a', then
#    there are following possibilities :
#    a) Current character begins a new subsequence.
#    b) Current character is part of aCount subsequences.
#    c) Current character is not part of aCount subsequences.
        if ch == 'a':
            aCount = (1 + 2 * aCount)
        elif ch == 'b':
            bCount = aCount + 2 * bCount
        elif ch == 'c':
            cCount = bCount + 2 * cCount

    return cCount


if __name__ == "__main__":
    inpStr = "abbc"
    inpStr = "abcabc"
    inpStr = "aaabc"
    print(countSubsequences(inpStr))



