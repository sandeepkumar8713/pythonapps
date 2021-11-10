# Similar : https://leetcode.com/problems/time-based-key-value-store/
# Question : Implement the version control map system which takes the snapshot of the
# versions of data. Implement the following functions:
# put(key, value) -> puts the value again the key in the latest version of the map
# get(key) -> get the value of the key for the latest version of the data
# snapshot() -> take a snapshot and increment the version
# getValVersion(version id, key) -> return value of the key of the particular version
# Implement a SnapshotArray that supports the following interface:
#
# SnapshotArray(int length) initializes an array-like data structure with the given length.
# Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id:
#   the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index,
#   at the time we took the snapshot with the given snap_id
#
# Question Type : ShouldSee
# Used : Use dict here. Key/index should be used once. It should have list of values
#        along with version for each key.
#        This is for second question. key : index, value : [snapId, value]
#        Logic : class SnapshotArray:
#        def __init__(self, length):
#        self.record = [[[0, 0]] for i in range(length)]
#        self.snap_ind = 0
#        def set(self, index, val):
#        if self.record[index][-1][0] == self.snap_ind:
#           self.record[index][-1][1] = val
#        else:
#            self.record[index].append([self.snap_ind, val])
#        def snap(self):
#        self.snap_ind += 1
#        return self.snap_ind - 1
#        def get(self, index, snap_id):
#        pos = bisect.bisect_right(self.record[index], [snap_id, float('inf')])
#        return self.record[index][pos - 1][1]
# Complexity : O(1)

import copy
import bisect


class Repo():
    def __init__(self):
        self.latestVersion = 0
        self.map = dict()
        self.map[self.latestVersion] = dict()

    def put(self,key,value):
        dataMap = self.map[self.latestVersion]
        dataMap[key] = value

    def get(self, key):
        return self.map[self.latestVersion][key]

    def getValVersion(self, version, key):
         return self.map[version][key]

    def snapshot(self):
        self.map[self.latestVersion + 1] = copy.deepcopy(self.map[self.latestVersion])
        self.latestVersion += 1


class SnapshotArray:
    def __init__(self, length):
        self.record = [[[0, 0]] for i in range(length)]
        self.snap_ind = 0

    def set(self, index, val):
        if self.record[index][-1][0] == self.snap_ind:
            self.record[index][-1][1] = val
        else:
            self.record[index].append([self.snap_ind, val])

    def snap(self):
        self.snap_ind += 1
        return self.snap_ind - 1

    def get(self, index, snap_id):
        pos = bisect.bisect_right(self.record[index], [snap_id, float('inf')])
        return self.record[index][pos - 1][1]


if __name__ == "__main__":
    repo = Repo()
    repo.put(10,10)
    print(repo.get(10))
    repo.snapshot()
    repo.put(10, 100)
    print(repo.get(10))

    print(repo.getValVersion(0, 10))
    print(repo.getValVersion(1, 10))
