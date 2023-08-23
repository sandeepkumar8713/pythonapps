# https://www.geeksforgeeks.org/number-substrings-count-character-k/
# https://github.com/Zhouzhiling/leetcode/blob/master/MemDev%20Find%20Perfect%20Substring.md
# Question : Given a string and an integer k, find the number of substrings in which all the different
# characters occur exactly k times.
# A String S compromised of digits from 0 to 9, contains a perfect substring if all the elements within
# a substring occur exactly k times. Calculate the number of perfect strings in s.
#
# Examples: Input : s = "aabbcc", k = 2
# Output : 6
# The substrings are aa, bb, cc, aabb, bbcc and aabbcc.
#
# Examples: Input : s = "1102021222", k = 2
# Output : 6
# The substrings are 11, 11020, 102021, 0202, 22, 22
#
# Question Type : Asked
# Used : Count the number of distinct characters (distinct_count).
#        Now we will make all possible sliding window of (1 to distinct_count) * k
#        Run loop for each window and find substring which satisfies the condition and increment result count.
# Logic: distinct_count = len(set([i for i in inp_str]))
#        for unique_count in range(1, distinct_count + 1):
#           window_length = unique_count * k
#           freq = defaultdict(int)
#           left = 0, right = window_length - 1
#           for i in range(left, min(right + 1, len(inp_str))):
#               freq[inp_str[i]] += 1
#           while right < len(inp_str):
#               if have_same_frequency(freq, k):
#                   count += 1
#               freq[inp_str[left]] -= 1
#               left += 1, right += 1
#               if right < len(inp_str):
#                   freq[inp_str[right]] += 1
#        return count
# Complexity : O(n * d) where d is count of distinct

from collections import defaultdict


def have_same_frequency(freq, k):
    return all([freq[i] == k or freq[i] == 0 for i in freq])


def count_substrings(inp_str, k) -> int:
    count = 0

    distinct_count = len(set([i for i in inp_str]))
    for unique_count in range(1, distinct_count + 1):
        window_length = unique_count * k

        freq = defaultdict(int)
        left = 0
        right = window_length - 1
        for i in range(left, min(right + 1, len(inp_str))):
            freq[inp_str[i]] += 1

        while right < len(inp_str):
            if have_same_frequency(freq, k):
                count += 1
            freq[inp_str[left]] -= 1
            left += 1
            right += 1
            if right < len(inp_str):
                freq[inp_str[right]] += 1

    return count


if __name__ == '__main__':
    s = '1102021222'
    k = 2
    print(count_substrings(s, k))

    s = "aabbcc"
    k = 2
    print(count_substrings(s, k))

    s = "114565722"
    k = 2
    print(count_substrings(s, k))
