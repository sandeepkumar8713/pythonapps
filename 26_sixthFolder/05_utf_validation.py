# https://leetcode.com/problems/utf-8-validation/
# Question : Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
# For a 1-byte character, the first bit is a 0, followed by its Unicode code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes
# with the most significant 2 bits being 10.
#
# Example : Input: data = [197,130,1]
# Output: true
# Explanation: data represents the octet sequence: 11000101 10000010 00000001.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
#
# Question Type : ShouldSee
# Used :
# Complexity :
#
# TODO ::