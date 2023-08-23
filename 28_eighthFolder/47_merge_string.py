# https://stackoverflow.com/questions/74820955/how-to-do-this-lexicography-lc-problem-the-right-way
# Question : Merge 2 strings based of freq of characters in respective strings
# For `s1 = "dce"` and `s2 = "cccbd"`, the output should be `mergeStrings(s1, s2) = "dcecccbd"`.
# All symbols from `s1` goes first, because all of them have only `1` occurrence in `s1` and `c`
# has `3` occurrences in `s2`.
#
# Question Type : Easy
# Used : Freq dict of characters. Do merge.
# Logic: while i < m and j < n:
#           ch_1 = str_1[i]
#           ch_2 = str_2[j]
#        if freq_dict_1[ch_1] < freq_dict_2[ch_2]:
#           res += ch_1
#           i += 1
#        elif freq_dict_1[ch_1] > freq_dict_2[ch_2]:
#           res += ch_2
#           j += 1
#        else:
#           if ch_1 <= ch_2:
#               res += ch_1
#               i += 1
#           else:
#               res += ch_2
#               j += 1
#     while i < m:
#         ch_1 = str_1[i]
#         res += ch_1
#         i += 1
#     while j < n:
#         ch_2 = str_2[j]
#         res += ch_2
#         j += 1
#     return res
# Complexity : O(m+n)

from collections import defaultdict


def merge_strings(str_1, str_2):
    freq_dict_1 = defaultdict(int)
    freq_dict_2 = defaultdict(int)

    for ch in str_1:
        freq_dict_1[ch] += 1

    for ch in str_2:
        freq_dict_2[ch] += 1

    i = 0
    j = 0
    m = len(str_1)
    n = len(str_2)
    res = ''
    while i < m and j < n:
        ch_1 = str_1[i]
        ch_2 = str_2[j]
        if freq_dict_1[ch_1] < freq_dict_2[ch_2]:
            res += ch_1
            i += 1
        elif freq_dict_1[ch_1] > freq_dict_2[ch_2]:
            res += ch_2
            j += 1
        else:
            if ch_1 <= ch_2:
                res += ch_1
                i += 1
            else:
                res += ch_2
                j += 1

    while i < m:
        ch_1 = str_1[i]
        res += ch_1
        i += 1

    while j < n:
        ch_2 = str_2[j]
        res += ch_2
        j += 1

    return res


if __name__ == "__main__":
    str_1 = "dce"
    str_2 = "cccbd"
    print(merge_strings(str_1, str_2))
