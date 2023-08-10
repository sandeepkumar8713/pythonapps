# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# https://www.geeksforgeeks.org/weighted-job-scheduling/
# Similar : https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Questions : We have n jobs, where every job is scheduled to be done from startTime[i]
# to endTime[i], obtaining a profit of profit[i].
# You're given the startTime, endTime and profit arrays, return the maximum profit
# you can take such that there are no two jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
#
# Question Type : Generic
# Used : Like Box stacking.
#        Since input is sorted, we will use Binary search to find the previous j.
#        Run a loop from 1 to n:
#           Assume this task is included, the call binary search to find out the previous feasible task
#           if this task is included. Let us call it j.
#           Add dp[j] to icluded task's profit.
#           Then compare with profit value if this task is not selected.
# Logic: job = sorted(job, key=lambda j: j.finish)
#        table = [0 for _ in range(n)]
#        table[0] = job[0].profit
#        for i in range(1, n):
#           inclProf = job[i].profit
#           j = binarySearch(job, i)
#           if j != -1:
#               inclProf += table[j]
#           table[i] = max(inclProf, table[i - 1])
#        return table[n - 1]
#
#        def binarySearch(job, start_index):
#        lo = 0, hi = start_index - 1
#        while lo <= hi:
#           mid = (lo + hi) // 2
#           if job[mid].finish <= job[start_index].start:
#               if job[mid + 1].finish <= job[start_index].start:
#                   lo = mid + 1
#               else:
#                   return mid
#           else:
#               hi = mid - 1
#        return -1
# Complexity : O(n log n)

# Class to represent a job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


# A Binary Search based function to find the latest job (before current job) that doesn't conflict with current
# job.  "index" is index of the current job.  This function returns -1 if all jobs before index conflict with it.
# The array jobs[] is sorted in increasing order of finish time.
def binarySearch(job, start_index):
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1

    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


# The main function that returns the maximum possible, profit from given array of jobs
def schedule(job):
    # Sort jobs according to finish time
    job = sorted(job, key=lambda j: j.finish)

    # Create an array to store solutions of subproblems. table[i] stores
    # the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]
    table[0] = job[0].profit

    for i in range(1, n):
        # Find profit including the current job
        inclProf = job[i].profit
        j = binarySearch(job, i)
        if j != -1:
            inclProf += table[j]

        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])

    return table[n - 1]


if __name__ == "__main__":
    job = [Job(1, 2, 50), Job(3, 5, 20),
           Job(6, 19, 100), Job(2, 100, 200)]
    print("Optimal profit is"),
    print (schedule(job))
