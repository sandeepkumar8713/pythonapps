# Redis, cache implementation validate for 1 min
# implement following function : set, get, ttl
# input : phone, output otp
# ttl : time to live
# How remove stale data:
# 1 solution may be to set another min heap with key as validity time and value as phone number.
# We keep on deleting items which are at the top of the heap.
# Question Type : Asked

def getRand():
    pass


class Cache:
    def __int__(self):
        self.myCache = {}
        self.stack = []

    def set(self, number, validity):
        self.myCache[number] = [getRand(), timestamp() + validity]
        # 10:00 > 10:01

    def get(self, number):
        otp, validity = self.myCache[number]
        if validity > current_time():
            del self.myCache[number]
            return None
        else:
            return otp

    def cleanup(self):
        # 10:02
        pass
