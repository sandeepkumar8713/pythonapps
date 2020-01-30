# https://leetcode.com/discuss/interview-experience/337083/Google-or-Test-Engineer-or-Bangalore-or-Spring-2019-Reject
# Question : Given a log file of following format, lines can be in any order or mixed up:
#
# Login 1: John Smith
# Login Success: 2
# Login 3: User123
# Login Failed: 3
# Login 2: Adam Apple
# Login Failed: 1
# Print out list of successful and failed logins:
#
# Success:
# Adam Apple
# Failed:
# User123
# John Smith
#
# Question Type : Easy
# Used : We can use set to store id only. loop 2 twice to print success and failure name.
# Complexity :
# TODO :: add code
