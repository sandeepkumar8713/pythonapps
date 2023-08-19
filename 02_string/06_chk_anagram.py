# https://leetcode.com/problems/valid-anagram/
# Question : Python program to check if two strings are anagrams of each other.
#
# Question Type : Asked
# Used : Make two list of 256 len, update count of each character in str1 and str2, now compare the two list
# Complexity : O(n)


NO_OF_CHARS = 256


def areAnagram(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    if len(str1) != len(str2):
        return 0

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1


if __name__ == "__main__":
    str1 = "geeksforgeeks"
    str2 = "forgeeksgeeks"
    if areAnagram(str1, str2):
        print("The two strings are anagram of each other")
    else:
        print("The two strings are not anagram of each other")
