# https://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/
# Question : Given a string 'str', check if it can be constructed by taking a substring of it and appending
# multiple copies of the substring together.
#
# Input: str = "abcabcabc"
# Output: true
# The given string is 3 times repetition of "abc"
#
# Question Type : Generic
# Used : 1) Find length of the longest proper prefix of 'str' which is also a suffix.
#           Let the length of the longest proper prefix suffix be 'len'. This can be
#           computed in O(n) time using pre-processing step of KMP string matching algorithm.
#        2) If value of 'n - len' divides n (or 'n % (n-len)' is 0), then return true,
#           else return false.
# Complexity : O(n)


# kmp
def computeLPSArray(pat, M, lps):
    length = 0  # length of the previous longest prefix suffix

    lps[0]
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def isRepeat(string):
    n = len(string)
    lps = [0] * n

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(string, n, lps)

    length = lps[n - 1]

    # repeats n/(n-len) times (Readers can print substring nd value of n/(n-len) for more clarity.
    if length > 0 and n % (n - length) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    txtList = ["ABCABC", "ABABAB", "ABCDABCD", "GEEKSFORGEEKS",
          "GEEKGEEK", "AAAACAAAAC", "ABCDABC", "abcabcabc"]
    for txt in txtList:
        print (txt),
        if isRepeat(txt):
            print("True")
        else:
            print("False")
