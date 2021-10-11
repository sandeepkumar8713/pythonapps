# https://leetcode.com/problems/student-attendance-record-ii/
# Question : n attendance record for a student can be represented as a string where each character
# signifies whether the student was absent, late, or present on that day. The record only contains
# the following three characters: 'A': Absent, 'L': Late and 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a
# student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
#
# Example : Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
#
# Question Type : ShouldSee
# Used :
# Complexity :
#
# TODO ::
#
