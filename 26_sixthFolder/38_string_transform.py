# https://wentao-shao.gitbook.io/leetcode/string/1153.string-transforms-into-another-string
# https://leetcode.com/problems/string-transforms-into-another-string/
# Question : Given two strings str1 and str2 of the same length, determine whether you can
# transform str1 into str2 by doing zero or more conversions. In one conversion you can
# convert all occurrences of one character in str1 to any other lowercase English character.
# Return true if and only if you can transform str1 into str2.
#
# Example : Input: str1 = "aabcc", str2 = "ccdee"
# Output: true
# Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order
# of conversions matter.
#
# Example : Input: str1 = "leetcode", str2 = "codeleet"
# Output: false
# Explanation: There is no way to transform str1 to str2.
#
# Question Type : Generic
# Used : Make a dict, key char from first str and value from second str
#        Now loop over the two array simultaneously. While doing so see char1 is there in dict.
#        If no, insert char1 as key and char2 as value
#        If yes, check if char2 in dict is same as char2 in str2. If yes continue else return False
#        After loop, return True.
# Complexity : O(n)
#
# TODO :: check if similar added
#