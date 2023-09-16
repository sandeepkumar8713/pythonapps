# https://leetcode.com/discuss/interview-question/3819090/MICROSOFT-OA
# Question : There is a string S of length N consisting of lowercase English letters (the letters are
# numbered from 1 to N). We are going to insert M '$' characters into the string in the order described by
# the contents of array C. The K-th '$' character (for K from 0 to M-1) is inserted after the CIK-th letter
# in S. (the 's' character is not considered a letter). For example, given S = "aabcba" and C = [1, 3, 2],
# we will insert three's characters into S, thus obtaining following strings: "a$abcba"-> "a$ab$cba" -> "a$a$b$cba".
# What is the minimum number of steps after which we can stop, such that there is at least one's character
# between every two occurrences of the same letter?
# In the example above, after the first insertion there are no '$' characters between the two letters 'b'
# (3rd and 5th letters in S), but after the second insertion there is a 's' between every two occurrences of
# every letter, so the answer is 2.
#
# Binary search
# TODO :: add used


def find_min_insertion(inp_str, pos):
    n = len(inp_str)
    left = 0
    right = len(pos) - 1
    while left <= right:
        mid = left + (right - left) // 2
        all = set(pos[:mid])
        have = [-1] * 26
        mark = True
        i = 0
        temp = -1
        while mark and i < n:
            p = ord(inp_str[i]) - ord('a')
            if have[p] > temp:
                mark = False

            have[p] = i
            if (i + 1) in all:
                temp = i

            i += 1

        if mark:
            right = mid - 1
        else:
            left = mid + 1

    right += 1
    if right > len(pos):
        return -1
    return right


if __name__ == "__main__":
    inp_str = "aabcba"
    pos = [1, 3, 2]
    print(find_min_insertion(inp_str, pos))
