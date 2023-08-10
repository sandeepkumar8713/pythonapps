# https://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/
# https://leetcode.com/problems/is-subsequence/
# Question : Given 2 strings str1 and str2, Check if str2 is subsequence of str1
#
# example : str1 = "abcd"
# str2 = "ac"
# True
# Question Type : Asked

# Complexity : O(n)

def is_subsequnce(str_1, str_2):
    m = len(str_1)
    n = len(str_2)

    i = 0
    j = 0
    while i < m and j < n:
        if str_1[i] == str_2[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == n:
        return True
    return False


if __name__ == "__main__":
    str_1 = "abcd"
    str_2 = "ac"
    print(is_subsequnce(str_1, str_2))

    str_1 = "abcd"
    str_2 = "ae"
    print(is_subsequnce(str_1, str_2))
