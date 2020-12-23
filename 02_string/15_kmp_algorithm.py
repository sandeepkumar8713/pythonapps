# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
# https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
# Question : Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[])
# that prints all occurrences of pat[] in txt[]. You may assume that n > m.
#
# Input:  txt[] = "THIS IS A TEST TEXT"
#         pat[] = "TEST"
# Output: Pattern found at index 10
#
# Explanation : In the next step, we compare next window of txt with pat.
# txt = "A|AAAA|BAAABA"
# pat =  "AAAA" [Pattern shifted one position]
# This is where KMP does optimization over Naive. In this second window, we only compare fourth A of pattern with
# fourth character of current window of text to decide whether current window matches or not. Since we know
# first three characters will anyway match, we skipped matching first three characters.
#
# Need of Preprocessing?
# An important question arises from above explanation, how to know how many characters to be skipped. To know this,
# we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be skipped.
# For each sub-pattern pat[0..i] where i = 0 to m-1, lps[i] stores length of the maximum matching proper prefix which
# is also a suffix of the sub-pattern pat[0..i].
#
# Question Type : Generic
# Used : Logic:
#        computeLPSArray(pat, M, lps) :
#        set i = 1, lps[0] = 0 and length = 0. Run a loop while i < N:
#        if pat[i] == pat[length]: (inc length assign it to lps[i] and inc i)
#           length += 1, lps[i] = length, i += 1
#        else:
#           if length != 0: (reduce length to match with previous pat[length])
#               length = lps[length - 1]
#        else:
#            lps[i] = 0, i += 1
#
#        KMPSearch(pat, txt):
#        Compute LPS for pat using the above function. Now loop while i < N:
#        if pat[j] == txt[i]: inc both i and j by 1
#        if j == M : print "pattern found at (i-j)"
#        elif i < N and pat[j] != txt[i] :  (if j is not at start, update j using lps else inc i)
#           if j != 0: j = lps[j - 1]
#           else: i += 1
#
# Complexity : O(n) if input txt is of length n


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # PreProcess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index ", str(i - j))
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    length = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example. AAACAAAA and i = 7. The idea is similar to search step.
            # For C we have to set lps[i] = 0, to do that we have keep reducing length to 0.
            if length != 0:
                length = lps[length - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"

    # txt = "AABAACAADAABAAABAA"
    # pat = "AABA"
    KMPSearch(pat, txt)
