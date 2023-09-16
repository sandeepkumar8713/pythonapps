# https://leetcode.com/problems/longest-happy-string/
# https://leetcode.com/discuss/interview-question/3740816/Microsoft-or-OA
# Question : A string s is called happy if it satisfies the following conditions:
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple
# longest happy strings, return any of them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.
#
# Example : Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
#
# TODO :: add used

import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
    max_heap = []
    if a != 0:
        heapq.heappush(max_heap, (-a, 'a'))
    if b != 0:
        heapq.heappush(max_heap, (-b, 'b'))
    if c != 0:
        heapq.heappush(max_heap, (-c, 'c'))
    res = []

    while max_heap:
        first, char1 = heapq.heappop(max_heap)  # char with most rest numbers
        if len(res) >= 2 and res[-1] == res[-2] == char1:  # check whether this char is the same with previous two
            if not max_heap:  # if there is no other choice, just return
                return ''.join(res)
            second, char2 = heapq.heappop(max_heap)  # char with second most rest numbers
            res.append(char2)
            second += 1  # count minus one, because the second here is negative, thus add 1
            if second != 0:  # only if there is rest number count, add it back to heap
                heapq.heappush(max_heap, (second, char2))
            heapq.heappush(max_heap, (first, char1))  # also need to put this part back to heap
            continue

        #  situation that this char can be directly added to answer
        res.append(char1)
        first += 1
        if first != 0:
            heapq.heappush(max_heap, (first, char1))
    return ''.join(res)


if __name__ == "__main__":
    a = 1
    b = 1
    c = 7
    print(longestDiverseString(a, b, c))

    a = 7
    b = 1
    c = 0
    print(longestDiverseString(a, b, c))
