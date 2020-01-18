# https://massivealgorithms.blogspot.com/2019/06/leetcode-1044-longest-duplicate.html
# https://leetcode.com/problems/longest-duplicate-substring/
# Question : Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more
# times. (The occurrences may overlap.)
#
# Example :
# Input: "banana"
# Output: "ana"
#
# Used : We will use Rabin-Karp algorithm to search the pattern. It uses hashing to find an exact match of a
#        pattern string in a text. It uses a rolling hash to quickly filter out positions of the text that cannot
#        match the pattern, and then checks for a match at the remaining positions.
#        Binary search the length of longest duplicate substring and call the help function search(mid).
#        search(mid) slide a window of length mid, rolling hash the string in this window, record the seen string
#        in a hash set, and try to find duplicated string.
#        def search(mid, a, modulus, n, nums):
#           h = 0
#           for i in range(mid):
#               h = (h * a + nums[i]) % modulus
#           seen = set(), seen.add(h)
#           aL = 1
#           for i in range(1, mid+1):
#               aL = (aL * a) % modulus
#           for start in range(1, n-mid+1):
#               h = (h * a - nums[start - 1] * aL % modulus + modulus) % modulus
#               h = (h + nums[start + mid - 1]) % modulus
#               if h in seen: return start
#               seen.add(h)
#           return -1
# Complexity : O(n log n)


def search(mid, a, modulus, n, nums):
    h = 0
    for i in range(mid):
        h = (h * a + nums[i]) % modulus

    seen = set()
    seen.add(h)

    aL = 1
    for i in range(1, mid+1):
        aL = (aL * a) % modulus

    for start in range(1, n-mid+1):
        h = (h * a - nums[start - 1] * aL % modulus + modulus) % modulus
        h = (h + nums[start + mid - 1]) % modulus
        if h in seen:
            return start
        seen.add(h)

    return -1


def longestDupSubstring(inpStr):
    n = len(inpStr)
    nums = []
    for char in inpStr:
        nums.append(ord(char) - ord('a'))

    a = 26
    modulus = 2**32

    result = 0
    low, high = 0, n
    while low < high:
        mid = (low + high + 1) / 2
        pos = search(mid, a, modulus, n, nums)
        if pos != -1:
            low = mid
            result = pos
        else:
            high = mid - 1

    return inpStr[result:result + low]


if __name__ == "__main__":
    inpStr = "banana"
    print longestDupSubstring(inpStr)
