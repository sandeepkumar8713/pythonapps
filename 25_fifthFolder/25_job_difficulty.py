# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/934601/Python-96
# Question : You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job,
# you have to finish all the jobs j where 0 <= j < i). You have to finish at least one task every day. The
# difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day
# is the maximum difficulty of a job done in that day. Given an array of integers jobDifficulty and an integer d.
# The difficulty of the i-th job is jobDifficulty[i]. Return the minimum difficulty of a job schedule. If you
# cannot find a schedule for the jobs return -1.
#
# Example : Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7.
#
# Question Type : OddOne
# Used : We will use 2 dp, 1 for current day, other of next day. Run a loop for each day.
#        For that day make a stack.
#        Run another loop, over all the jobs starting from current day. Initialize tempDp with
#        jobDifficulty of the current job. Now keep popping job from the stack, if its difficulty
#        is less than current job. Now update current tempDp if (after removing popped job difficulty
#        from and adding current job difficulty is less).
#        If stack is still not empty, update current tempDp if top job in stack is choosen
#        and its tempDp value is less.
#        At the end append current job index in stack.
#        When the current day jobs loop gets over update dp with tempDp and reset tempDp.
#        After the outer loop, return dp[-1]
#        minDifficulty(jobDifficulty, d):
#        for day in range(d):
#           stack = []
#           for i in range(day, n):
#               if i:
#                   tempDp[i] = dp[i - 1] + jobDifficulty[i]
#               else:
#                   tempDp[i] = jobDifficulty[i]
#               while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
#                   job = stack.pop()
#                   tempDp[i] = min(tempDp[i], tempDp[job] - jobDifficulty[job] + jobDifficulty[i])
#               if stack:
#                   tempDp[i] = min(tempDp[i], tempDp[stack[-1]])
#               stack.append(i)
#           dp = tempDp
#           tempDp = [0] * n
#        return dp[-1]
# Complexity : O(d * n * n) where n is size of jobDifficulty array

import sys


def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d:
        return -1
    dp = [sys.maxsize] * n
    tempDp = [0] * n

    for day in range(d):
        stack = []
        for i in range(day, n):
            if i:
                tempDp[i] = dp[i - 1] + jobDifficulty[i]
            else:
                tempDp[i] = jobDifficulty[i]
            while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                job = stack.pop()
                tempDp[i] = min(tempDp[i], tempDp[job] - jobDifficulty[job] + jobDifficulty[i])
            if stack:
                tempDp[i] = min(tempDp[i], tempDp[stack[-1]])
            stack.append(i)
        dp = tempDp
        tempDp = [0] * n

    return dp[-1]


if __name__ == "__main__":
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    print(minDifficulty(jobDifficulty, d))

    jobDifficulty = [9, 9, 9]
    d = 4
    print(minDifficulty(jobDifficulty, d))

    jobDifficulty = [7, 1, 7, 1, 7, 1]
    d = 3
    print(minDifficulty(jobDifficulty, d))

    jobDifficulty = [1, 1, 1]
    d = 3
    print(minDifficulty(jobDifficulty, d))

    jobDifficulty = [11, 111, 22, 222, 33, 333, 44, 444]
    d = 6
    print(minDifficulty(jobDifficulty, d))
