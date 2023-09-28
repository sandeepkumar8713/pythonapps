# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Question : You are given an array of strings arr. A string s is formed by the concatenation of a subsequence
# of arr that has unique characters. Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some or no elements without
# changing the order of the remaining elements.
#
# Example : Input: arr = ["un","iq","ue"]
# Output: 4
# - "uniq" ("un" + "iq") OR
# - "ique" ("iq" + "ue")
#
# TODO :: add used
# Used : Run DP with DFS for both include and exclude.
#        Return max of include and exclude.
#        For memory save dict of dp, key being temp string

def is_unique(str_1, str_2):
    hash_set_1 = set()

    for ch in str_1:
        hash_set_1.add(ch)

    if len(str_1) != len(hash_set_1):
        return False

    hash_set_2 = set()
    for ch in str_2:
        if ch in hash_set_1:
            return False
        hash_set_2.add(ch)

    if len(str_2) != len(hash_set_2):
        return False

    return True


def find_max_len(inp_arr):
    temp = ""
    n = len(inp_arr)
    dp = {}

    def dfs(index, temp):
        if index >= n:
            return len(temp)

        if temp in dp.keys():
            return dp[temp]

        include = 0
        exclude = dfs(index + 1, temp)
        if is_unique(inp_arr[index], temp):
            new_temp = temp + inp_arr[index]
            include = dfs(index + 1, new_temp)

        dp[temp] = max(include, exclude)
        return dp[temp]

    return dfs(0, temp)


if __name__ == "__main__":
    inp_arr = ["un", "iq", "ue"]
    print(find_max_len(inp_arr))

    inp_arr = ["cha", "r", "act", "ers"]
    print(find_max_len(inp_arr))

    inp_arr = ["abcdefghijklmnopqrstuvwxyz"]
    print(find_max_len(inp_arr))

    inp_arr = ["aa", "bb"]
    print(find_max_len(inp_arr))

