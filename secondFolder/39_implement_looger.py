# https://leetcode.com/discuss/interview-question/340230
# Question : Implement a logger class, It should have start(time, pid), end(time, pid) and print() function.
# Prints the logs of this system sorted by the start time of processes in the below format.
#
# Example :
# Logger log = new MyLogger();
# log.start("1", 100);
# log.start("2", 101);
# log.end("2", 102);
# log.start("3", 103);
# log.end("1", 104);
# log.end("3", 105);
# log.print();
#
# Output:
# 1 started at 100 and ended at 104
# 2 started at 101 and ended at 102
# 3 started at 103 and ended at 105
#
# Used : We create a hashMap to store the start time of a pid. When we call end, we get the start time of the pid
#        from the hashMap and append it into the heap.
#        Logic : def start(self, pid, ts):
#        if pid not in self.store:
#           self.store[pid] = ts
#        def end(self, pid, ts):
#           if pid in self.store:
#               heapq.heappush(self.heap, (self.store[pid], ts, pid))
#               del self.store[pid]
#        def show(self):
#           tmp = self.heap[:]
#           while len(tmp) > 0:
#               start, end, pid = heapq.heappop(tmp)
#               print('{} started at {} and ended at {}'.format(pid, start, end))
# Complexity : O(n log n) space O(n)

import heapq


class Logger:
    def __init__(self):
        self.store = dict()
        self.heap = []

    def start(self, pid, ts):
        if pid not in self.store:
            self.store[pid] = ts

    def end(self, pid, ts):
        if pid in self.store:
            heapq.heappush(self.heap, (self.store[pid], ts, pid))
            del self.store[pid]

    def show(self):
        tmp = self.heap[:]
        while len(tmp) > 0:
            start, end, pid = heapq.heappop(tmp)
            print('{} started at {} and ended at {}'.format(pid, start, end))


if __name__ == "__main__":
    log = Logger()
    log.start("1", 100)
    log.start("2", 101)
    log.end("2", 102)
    log.start("3", 103)
    log.end("1", 104)
    log.end("3", 105)
    log.show()
