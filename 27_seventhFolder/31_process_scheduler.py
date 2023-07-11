# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# Questions : A service is responsible for running tasks, and we're interested in the order
# those tasks will run. A task is defined by its:
#   s earliest start time
#   d total duration of execution
#   p priority of execution
# The service is greedy in running tasks, such that it will start a runnable task if idle.
# At most one task can be run at any time, and all tasks will be run exactly once.
# The service will not start a task before its earliest start times however the task may
# be run any time thereafter. Once started, no other tasks may be scheduled for the duration
# d while the task runs to completion.
# If two or more tasks are available to be run, then the next task is selected in order
# of the following criteria:
#   Highest priority p
#   Earliest start time s
#   Lowest duration of execution d
#   Lowest index in the input
#
# Example : Input :
# s : [0, 2, 2]
# d : [1, 1, 1]
# p : [0, 0, 1]
# Output : [0, 2, 1]
#
# Question Type : Asked
# Used : Make an object for each task.
#        Make a custom sort function based of above listed 4 conditions
#        We need to do step by step scheduling,
#           In step 1 choose all the tasks whose start time is ready and then sort them
#           In Step 2 find the time spent by tasks in step 1 and accordingly choose
#           tasks whose start time is ready and sort them.
# Logic: get_task_sequence(start_times, durations, priorities):
#        tasks = {}, n = len(start_times)
#        for i in range(n):
#           task = Task(start_times[i], durations[i], priorities[i], i)
#           if start_times[i] in tasks:
#               tasks[start_times[i]].append(task)
#           else:
#               tasks[start_times[i]] = [task]
#        result = []
#        left = min(start_times), right = left
#        while len(tasks.keys()) != 0:
#           this_list = []
#           while left <= right:
#               if left in tasks:
#                   this_list.extend(tasks.get(left))
#                   del tasks[left]
#               left += 1
#           this_result = sorted(this_list, key=functools.cmp_to_key(comparator))
#           exc_time = 0
#           for task in this_result:
#               result.append(task.index)
#               exc_time += task.duration
#           right += exc_time
#           if right < left: right = left
#        return result
# Complexity : O(n log n)

import functools


class Task:
    def __init__(self, start_time, duration, priority, index):
        self.start_time = start_time
        self.duration = duration
        self.priority = priority
        self.index = index


def comparator(task_a, task_b):
    priority_diff = task_a.priority - task_b.priority
    start_time_diff = task_a.start_time - task_b.start_time
    duration_diff = task_a.duration - task_b.duration
    index_diff = task_a.index - task_b.index

    if priority_diff != 0:
        return -priority_diff
    if start_time_diff != 0:
        return start_time_diff
    if duration_diff != 0:
        return duration_diff
    return index_diff


def get_task_sequence(start_times, durations, priorities):
    tasks = {}
    n = len(start_times)
    for i in range(n):
        task = Task(start_times[i], durations[i], priorities[i], i)
        if start_times[i] in tasks:
            tasks[start_times[i]].append(task)
        else:
            tasks[start_times[i]] = [task]

    result = []
    left = min(start_times)
    right = left
    while len(tasks.keys()) != 0:
        this_list = []
        # Pick all the tasks whose start time is ready to execute
        while left <= right:
            if left in tasks:
                this_list.extend(tasks.get(left))
                del tasks[left]
            left += 1

        this_result = sorted(this_list, key=functools.cmp_to_key(comparator))
        exc_time = 0
        for task in this_result:
            result.append(task.index)
            exc_time += task.duration
        right += exc_time

        if right < left:
            right = left

    return result


if __name__ == "__main__":
    s = [1, 1, 1, 1]
    d = [2, 2, 2, 2]
    p = [0, 1, 2, 3]
    print(get_task_sequence(s, d, p))

    s = [0, 2, 2]
    d = [1, 1, 1]
    p = [0, 0, 1]
    print(get_task_sequence(s, d, p))

    s = [0, 1, 2]
    d = [3, 1, 1]
    p = [0, 0, 1]
    print(get_task_sequence(s, d, p))

    s = [0, 1, 9]
    d = [3, 1, 1]
    p = [0, 0, 1]
    print(get_task_sequence(s, d, p))
