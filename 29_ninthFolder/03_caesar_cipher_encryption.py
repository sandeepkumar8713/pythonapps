# https://leetcode.com/discuss/interview-question/395045/Facebook-or-Phone-Screen-or-Caesar-Cipher
# Question : You are given a list of string, group them if they are same after using Ceaser Cipher Encrpytion.
# Definition of "same", "abc" can right shift 1, get "bcd", here you can shift as many time as you want,
# the string will be considered as same.
#
# Example: Input: ["abc", "bcd", "acd", "dfg"]
# Output: [["abc", "bcd"], ["acd", "dfg"]]
#
# Question Type : Easy
# Used : Note that diff b/w the characters is same for "same" words.
#        We will use this diff as key in map to group the words.
# Logic: for word in words:
#           n = len(word), diff_list = []
#           for i in range(1, n):
#               diff_list.append(str(ord(word[i]) - ord(word[0])))
#           diff = "".join(diff_list)
#           record[diff].append(word)
#        return list(record.values())
# Complexity : O(n * m) n is word count, m is length of longest word.

from collections import defaultdict


def caesar_encryption(words):
    record = defaultdict(list)
    for word in words:
        n = len(word)
        diff_list = []
        for i in range(1, n):
            diff_list.append(str(ord(word[i]) - ord(word[0])))

        diff = "".join(diff_list)
        record[diff].append(word)

    return list(record.values())


if __name__ == "__main__":
    inp_arr = ["abc", "bcd", "acd", "dfg"]
    print(caesar_encryption(inp_arr))
