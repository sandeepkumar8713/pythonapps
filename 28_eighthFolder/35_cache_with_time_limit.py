# https://leetcode.com/problems/cache-with-time-limit/
# Write a class that allows getting and setting key-value pairs, however a time until expiration is
# associated with each key.
# The class has three public methods:
# set(key, value, duration): accepts an integer key, an integer value, and a duration in milliseconds.
# Once the duration has elapsed, the key should be inaccessible. The method should return true if the
# same un-expired key already exists and false otherwise. Both the value and duration should be
# overwritten if the key already exists.
# get(key): if an un-expired key exists, it should return the associated value. Otherwise it should
# return -1.
# count(): returns the count of un-expired keys.
#
# Question Type : Asked
# Used : Dict with priority queue
# Logic: def set(self, key, value, duration):
#        setattr(Node, "__lt__", lambda self, other: self.expiry <= other.expiry)
#        exists = False
#        if key in self.map.keys():
#           old_node = self.map[key]
#           if datetime.now() <= old_node.expiry:
#               exists = True
#           old_node.expiry = datetime(year=1, month=1, day=1)
#           del self.map[key]
#        new_node = Node(key, value, datetime.now() + timedelta(milliseconds=duration))
#        self.map[key] = new_node
#        heapq.heappush(self.pq, new_node)
#        return exists
#
#        def get(self, key):
#        if key in self.map.keys():
#           node = self.map[key]
#               if datetime.now() <= node.expiry:
#                   return node.data
#        return -1
#
#        def count(self):
#        heapq.heapify(self.pq)
#        while len(self.pq) > 0 and self.pq[0].expiry < datetime.now():
#           old_node = heapq.heappop(self.pq)
#           if old_node.expiry != datetime(year=1, month=1, day=1):
#               del self.map[old_node.key]
#        return len(self.pq)
# Complexity : get : O(1) set : O(1) + O(log n), count : O(n) + O(log n)

from datetime import datetime, timedelta
import heapq
import time


class Node:
    def __init__(self, key, data, expiry):
        self.key = key
        self.data = data
        self.expiry = expiry


class CacheTime:
    def __init__(self):
        self.map = dict()
        self.pq = []

    def set(self, key, value, duration):
        setattr(Node, "__lt__", lambda self, other: self.expiry <= other.expiry)

        exists = False
        if key in self.map.keys():
            old_node = self.map[key]
            if datetime.now() <= old_node.expiry:
                exists = True
            old_node.expiry = datetime(year=1, month=1, day=1)
            del self.map[key]

        new_node = Node(key, value, datetime.now() + timedelta(milliseconds=duration))
        self.map[key] = new_node
        heapq.heappush(self.pq, new_node)

        return exists

    def get(self, key):
        if key in self.map.keys():
            node = self.map[key]
            if datetime.now() <= node.expiry:
                return node.data

        return -1

    def count(self):
        heapq.heapify(self.pq)
        while len(self.pq) > 0 and self.pq[0].expiry < datetime.now():
            old_node = heapq.heappop(self.pq)
            if old_node.expiry != datetime(year=1, month=1, day=1):
                del self.map[old_node.key]
        return len(self.pq)


if __name__ == "__main__":
    ct_1 = CacheTime()
    print(ct_1.set(1, 42, 100))
    time.sleep(50 / 1000)  # After 50 milliseconds
    print(ct_1.get(1))
    time.sleep(100 / 1000)  # After 100 milliseconds
    print(ct_1.get(1))

    print("")

    ct_2 = CacheTime()
    print(ct_2.set(1, 42, 50))
    time.sleep(40 / 1000)  # After 40 milliseconds
    print(ct_2.set(1, 50, 100))
    time.sleep(10 / 1000)  # After 50 milliseconds
    print(ct_2.get(1))
    time.sleep(70 / 1000)  # After 120 milliseconds
    print(ct_2.get(1))
    time.sleep(80 / 1000)  # After 200 milliseconds
    print(ct_2.get(1))
    time.sleep(50 / 1000)  # After 250 milliseconds
    print(ct_2.count())
