# CTCI : Q16_25_LRU_Cache (similar)
# Question : Given a sequence of pages and memory capacity, your task is to find the number of page faults using
# Least Recently Used (LRU) Algorithm.
#
# Used : Make a class LRU cache, whose attributes are: cacheList, capacity. Keep a count of page faults.
#        Loop over the input pages. If the page is not in cache list increment the page fault. If the cache is not
#           filled completely, append the page in cache list. If the cache is full, remove the first page from cache
#           list and append the page in cache list.
#           If page is there in cache list, remove that page and append it in the end.
#        return pageFaultCount
# Complexity : O(n)


class LRUCache:
    def __init__(self, size):
        self.cacheList = []
        self.capacity = size

    def pageFaultCount(self, pages):
        pageFault = 0
        for page in pages:
            if page not in self.cacheList:
                pageFault += 1

                # Cache still empty
                if len(self.cacheList) < self.capacity:
                    self.cacheList.append(page)
                else:  # Cache full
                    self.cacheList.pop(0)
                    self.cacheList.append(page)
            else:
                self.cacheList.remove(page)
                self.cacheList.append(page)

        return pageFault


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 4
    lru = LRUCache(capacity)
    print ("Page fault count: %s" % lru.pageFaultCount(pages))
