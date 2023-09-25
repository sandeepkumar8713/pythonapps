# https://leetcode.com/problems/permutation-in-string/
# Question : Given two strings s1 and s2, write a function to return true if s2 contains the
# permutation of s1. In other words, one of the first string's permutations is the substring
# of the second string.
#
# Example : Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Question Type : ShouldSee
# Used : Anagram and permutation of a string are same.
#        To do so, we maintain a count variable, which stores the number of characters(out of the 26 alphabets),
#        which have the same frequency of occurence in s1s1 and the current window in s2s2. When we slide the window,
#        if the deduction of the last element and the addition of the new element leads to a new frequency match of
#        any of the characters, we increment the count by 1. If not, we keep the count intact. But, if a
#        character whose frequency was the same earlier(prior to addition and removal) is added, it now leads to a
#        frequency mismatch which is taken into account by decrementing the same count variable. If, after
#        the shifting of the window, the count evaluates to 26, it means all the characters match in frequency
#        totally. So, we return a True in that case immediately.
# Logic: def checkInclusion(s1, s2):
#        if len(s1) > len(s2): return False
#        s1Freq = [0] * 26, s2Freq = [0] * 26
#        for i in range(len(s1)):
#           s1Freq[charToIndex(s1[i])] += 1
#           s2Freq[charToIndex(s2[i])] += 1
#        count = 0
#        for i in range(len(s1Freq)):
#           if s1Freq[i] == s2Freq[i]:
#               count += 1
#        for i in range(0, len(s2) - len(s1)):
#           left = charToIndex(s2[i])
#           right = charToIndex(s2[i + len(s1)])
#           if count == 26: return True
#
#           s2Freq[right] += 1
#           if s2Freq[right] == s1Freq[right]: count += 1
#           elif s2Freq[right] == s1Freq[right] + 1: count -= 1
#
#           s2Freq[left] -= 1
#           if s2Freq[left] == s1Freq[left]: count += 1
#           elif s2Freq[left] == s1Freq[left] - 1: count -= 1
#        return count == 26
# Complexity : O(l1 + l2 - l1)


def charToIndex(ch):
    return ord(ch) - ord('a')


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Freq = [0] * 26
    s2Freq = [0] * 26

    for i in range(len(s1)):
        s1Freq[charToIndex(s1[i])] += 1
        s2Freq[charToIndex(s2[i])] += 1

    count = 0
    for i in range(len(s1Freq)):
        if s1Freq[i] == s2Freq[i]:
            count += 1

    # Sliding window
    for i in range(0, len(s2) - len(s1)):
        left = charToIndex(s2[i])
        right = charToIndex(s2[i + len(s1)])

        if count == 26:
            return True

        s2Freq[right] += 1
        if s2Freq[right] == s1Freq[right]:
            count += 1
        elif s2Freq[right] == s1Freq[right] + 1:
            count -= 1

        s2Freq[left] -= 1
        if s2Freq[left] == s1Freq[left]:
            count += 1
        elif s2Freq[left] == s1Freq[left] - 1:
            count -= 1

    return count == 26


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))
