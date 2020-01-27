# Question : Multi -level cache system design with different storage in each level.
# a. Read Operation : Minimum time to read a particular key from cache system. This should be followed by writing the
# key in all levels above it. Eg. if "key" is found at level 'i', add this key to cache present at 1 to i-1 level.
# b. Write Operation: - Any write Operation should write  in cache of all levels.
#
# You can choose any algorithm for cache management like LRU, MRU.
#
# BONUS POINTS:-
# a. Show the current usage of each level cache.(Number of elements vs total Capacity of cache)
# b. Average read time and average write time.
#
# Question Type : OddOne
# Used : TODO :: add used
# Complexity :

from threading import Thread
import time


class LRUCache:
    notFoundLevelCount = 0
    
    def __init__(self, size):
        self.cacheList = []
        self.capacity = size
        self.nextCache = None

    def read(self, key):
        if key in self.cacheList:
            self.cacheList.remove(key)
            self.cacheList.append(key)
            return self.cacheList[-1]
        else:
            LRUCache.notFoundLevelCount += 1
            if self.nextCache is not None:
                value = self.nextCache.read(key)
                # this should be after write
                # self.writeInThisLevel(key)
                thread = Thread(target=self.writeInThisLevel, args=(key,))
                thread.start()
                # thread.join()
                return value

    def writeInThisLevel(self, key):
        if key in self.cacheList:
            self.cacheList.remove(key)

        if len(self.cacheList) == self.capacity:
            del self.cacheList[0]

        self.cacheList.append(key)

    def write(self, key):
        # self.writeInThisLevel(key)
        thread = Thread(target=self.writeInThisLevel, args=(key,))
        thread.start()
        self.nextLevelWrite(key)

    def nextLevelWrite(self, key):
        if self.nextCache is not None:
            self.nextCache.write(key)

    def display(self):
        print(self.cacheList,end=" ")
        if self.nextCache is not None:
            self.nextCache.display(),
        else:
            print('')
            
    def getNextCache(self):
        return self.nextCache

    def setNextCache(self, nextCache):
        self.nextCache = nextCache

    def usage(self):
        print(len(self.cacheList), '/', self.capacity, '|',end=" ")
        if self.nextCache is not None:
            self.nextCache.usage(),
        else:
            print('')


def insertCache(rootCache, cacheCapacity):

    newCache = LRUCache(cacheCapacity)
    if rootCache is None:
         return newCache
    nextCache = rootCache

    while nextCache.getNextCache() is not None:
        nextCache = nextCache.getNextCache()

    nextCache.setNextCache(newCache)

    return rootCache


class LRUCacheManager:
    def __init__(self, cacheCapacityList):
        self.rootCache = None

        for cacheCapacity in cacheCapacityList:
            self.rootCache = insertCache(self.rootCache, cacheCapacity)

        self.totalWriteTime = 0
        self.totalReadTime = 0
        self.totalWriteCount = 0
        self.totalReadCount = 0

    def write(self, key):
        startTime = time.time()
        self.rootCache.write(key)
        self.totalWriteTime = time.time() - startTime
        self.totalWriteCount += 1

    def read(self, key):
        startTime = time.time()
        result = self.rootCache.read(key)
        self.totalReadTime = time.time() - startTime
        self.totalReadCount += 1
        return result

    def usage(self):
        self.rootCache.usage()

    def display(self):
        self.rootCache.display()

    def getAvgWriteTime(self):
        return self.totalWriteTime / self.totalWriteCount

    def getAvgReadTime(self):
        return self.totalReadTime / self.totalReadCount


if __name__ == "__main__":
    cacheCapacityList = [4, 5, 6, 7, 8]

    lruManager = LRUCacheManager(cacheCapacityList)

    lruManager.write(1)
    lruManager.write(2)
    lruManager.write(3)
    lruManager.write(4)
    lruManager.write(5)
    print("Usage :"),
    lruManager.usage()
    lruManager.write(6)
    lruManager.write(7)
    lruManager.write(8)
    lruManager.write(9)
    lruManager.display()
    print(lruManager.read(3))
    print(lruManager.read(2))
    lruManager.display()
    print("Usage :"),
    lruManager.usage()
    # print LRUCache.notFoundLevelCount
    print("Average Write Time: %s"% lruManager.getAvgWriteTime())
    print("Average Read Time: %s" % lruManager.getAvgReadTime())
