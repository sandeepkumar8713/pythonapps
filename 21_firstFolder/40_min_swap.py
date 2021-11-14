# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# Question : You are given two strings s1 and s2 of equal length consisting of letters "x" and
# "y" only. Your task is to make these two strings equal to each other. You can swap any two
# characters that belong to different strings, which means: swap s1[i] and s2[j]. Return the
# minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible
# to do so.
#
# Example : Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
#
# Question Type : ShouldSee
# Used : 1. seq is char in s1 + char in s2 when unmatched for some index i.
#        2. for seq "xy": (char 'x' in s1 and char 'y' in s2) - add to set seen. If another similar sequence is
#           encountered, increment swaps by 1 because s1 = "xx" and s2="yy" need 1 swap.
#        3. In the end, check if we are left with both of the seq types, eg "xy" and "yx", it would take 2 swaps more,
#           hence return swaps+2, ...else if only 1 swap is left, we cannot achieve equal strings: return -1.
#        4. if the set is empty at last, strings are made equal, return swaps.
#        Logic : def minimumSwap(s1, s2):
#        seen = set(), swaps = 0
#        for i in range(len(s1)):
#           if s1[i] != s2[i]:
#               seq = s1[i] + s2[i]
#               if seq in seen:
#                   seen.remove(seq)
#                   swaps += 1
#               else:
#                   seen.add(seq)
#        if len(seen) == 1: return -1
#        elif len(seen) == 2: return swaps + 2
#        else: return swaps
# Complexity : O(n)


def minimumSwap(s1, s2):
    seen = set()
    swaps = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            seq = s1[i] + s2[i]

            if seq in seen:
                seen.remove(seq)
                swaps += 1
            else:
                seen.add(seq)

    if len(seen) == 1:
        return -1
    elif len(seen) == 2:
        return swaps + 2
    else:
        return swaps


if __name__ == "__main__":
    s1 = "xy"
    s2 = "yx"
    print(minimumSwap(s1, s2))

    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    print(minimumSwap(s1, s2))

    s1 = "xx"
    s2 = "xy"
    print(minimumSwap(s1, s2))
