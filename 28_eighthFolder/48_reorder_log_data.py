# https://leetcode.com/problems/reorder-data-in-log-files
# Question : You are given an array of logs. Each log is a space-delimited string of words, where the first
# word is the identifier.
# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
#
# Reorder these logs so that:
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same,
# then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.
#
# Example : Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
#
# Question Type : Easy
# Used : Custom Sort
# Logic: def compare(a, b):
#        if not a.is_digit and not b.is_digit:
#           if a.content < b.content: return -1
#           elif a.content > b.content: return 1
#           else:
#               if a.id < b.id: return -1
#               elif a.id > b.id: return 1
#               else: return 0
#        if a.is_digit and not b.is_digit: return 1
#        if b.is_digit and not a.is_digit: return -1
#        return 0
# Complexity : O(n)

import functools


class Node:
    def __init__(self, value):
        self.value = value
        sub_str = value.split(" ")
        self.id = sub_str[0]
        self.content = " ".join(sub_str[1:])
        self.is_digit = False
        if sub_str[1].isdigit():
            self.is_digit = True


def compare(a, b):
    if not a.is_digit and not b.is_digit:
        if a.content < b.content:
            return -1
        elif a.content > b.content:
            return 1
        else:
            if a.id < b.id:
                return -1
            elif a.id > b.id:
                return 1
            else:
                return 0

    if a.is_digit and not b.is_digit:
        return 1

    if b.is_digit and not a.is_digit:
        return -1

    # To maintain relative order of digits
    return 0


def reorder(logs):
    node_list = []
    for log in logs:
        node_list.append(Node(log))

    node_list.sort(key=functools.cmp_to_key(compare))

    result = []
    for node in node_list:
        result.append(node.value)
    return result


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorder(logs))

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(reorder(logs))

    logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
    print(reorder(logs))

    logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    print(reorder(logs))
