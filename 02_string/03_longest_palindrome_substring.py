# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
# Question : Given a string, find the longest substring which is palindrome. For example, if the given string is
# "forgeeksskeegfor" the output should be "geeksskeeg"
#
# Question Type : Generic
# Used : The idea is to generate all even length and odd length palindromes and keep track of the
#        longest palindrome seen so far. One by one consider every character as center point of even
#        and length palindromes.
#        Run a loop for i: 1 to n-1.
#           low = i - 1, high = i (for odd)
#           keep looping while low >= 0 and high < length and string[low] == string[high]:
#                low -= 1, high += 1  (update maxLen if required)
#        Similarly do for even
# Complexity : O(n^2)


def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    # One by one consider every character as center point of even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome substring is:",end=" ")
    print(string[start:start + maxLength])

    return maxLength


if __name__ == "__main__":
    string = "forgeeksskeegfor"
    print("Length is: " + str(longestPalSubstr(string)))
