# https://www.geeksforgeeks.org/count-number-of-substrings-of-a-string-consisting-of-same-characters/
# Question : Given a string. The task is to find out the numbers of substrings consisting of the same characters.
#
# Examples:
#
# Input: abba
# Output: 5
# The desired substrings are {a}, {b}, {b}, {a}, {bb}
#
# Used : It is known for a string of length n, there are a total of n*(n+1)/2 number of substrings.
#        Let's initialize the result to 0. Traverse the string and find the number of consecutive element
#        (let's say count) of same characters. Whenever we find another character, increment the result by
#        count*(count+1)/2, set count to 1 and from that index, repeat the above process.
# Complexity : O(n)


def findNumbers(inpStr):
    n = len(inpStr)
    count = 1
    result = 0
    left = 0
    right = 1
    while right < n:
        if inpStr[left] == inpStr[right]:
            count += 1
        else:
            result += count * (count + 1)/2
            left = right
            count = 1
        right += 1

    result += count * (count + 1) / 2
    return result


if __name__ == "__main__":
    inpStr = "bbbcbb"
    print findNumbers(inpStr)
