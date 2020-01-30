# https://algorithm-notes-allinone.blogspot.com/2019/08/leetcode-1055-shortest-way-to-form.html
# https://leetcode.com/discuss/interview-question/451456/Google-or-Phone-or-Shortest-Way-to-Form-String/
# Question : From any string, we can form a subsequence of that string by deleting some number of characters
# (possibly no deletions). Given two strings source and target, return the minimum number of subsequences of
# source such that their concatenation equals target. If the task is impossible, return -1.
#
# Example: Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
#
# Question Type : Generic
# Used : Make a function find() which match target with source as much as possible.
#        After that call find() again from next index (to match remaining with source)
#        Logic : def find(j, source, target):
#        i = 0
#        while i < len(source) and j < len(target):
#           if source[i] == target[j]: j += 1
#           i += 1
#        return j
#        def minways(source, target):
#        j = 0, count = 0
#        while j < len(target):
#           ret = find(j, source, target)
#           if ret == j: return -1
#           j = ret, count += 1
#        return count


def find(j, source, target):
    i = 0
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            j += 1
        i += 1
    return j


def minways(source, target):
    j = 0
    count = 0
    while j < len(target):
        ret = find(j, source, target)
        if ret == j:
            return -1
        j = ret
        count += 1
    return count


if __name__ == "__main__":
    source = "abc"
    target = "abcbc"
    print(minways(source, target))
