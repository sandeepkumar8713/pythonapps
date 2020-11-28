# https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/
# Question : Design a data structure that supports following operations in 0(1) time.
# insert(x): Inserts an item x to the data structure if not already present.
# remove(x): Removes an item x from the data structure if present.
# search(x): Searches an item x in the data structure.
# getRandom(): Returns a random element from current set of elements
#
# Question Type : ShouldSee
# Used : Its better to use map only.
#        insert(x) :
#        Check if x is already present by doing a hash map lookup.
#        If not present, then insert it at the end of the array.
#        Add in hash table also, x is added as key and last array index as index.
#        remove(x) :
#        Check if x is present by doing a hash map lookup.
#        If present, then find its index and remove it from hash map.
#        Swap the last element with this element in array and remove the last element.
#        Swapping is done because the last element can be removed in O(1) time.
#        Update index of last element in hash map.
#        getRandom() :
#        Generate a random number from 0 to last index.
#        Return the array element at the randomly generated index.
#        search(x) :
#        Do a lookup for x in hash map and get its index.
#        Use this index to get value from array.
# Complexity : O(n) (searching data in dict)

import random


class MyStruct:
    def __init__(self):
        self.arr = []
        self.hashMap = dict()

    def insert(self, data):
        if data in self.hashMap.keys():
            return
        index = len(self.arr)
        self.arr.append(data)
        self.hashMap[data] = index

    def remove(self, data):
        if data not in self.hashMap.keys():
            return
        index = self.hashMap[data]
        del self.hashMap[data]
        lastIndex = len(self.arr) - 1
        self.arr[index], self.arr[lastIndex] = self.arr[lastIndex], self.arr[index]
        self.arr.pop()
        self.hashMap[self.arr[index]] = index

    def search(self, data):
        if data in self.hashMap.keys():
            return self.arr[self.hashMap[data]]
        return -1

    def random(self):
        randomIndex = random.randint(0, len(self.arr))
        return self.arr[randomIndex]


if __name__ == "__main__":
    myStruct = MyStruct()
    myStruct.insert(10)
    myStruct.insert(20)
    myStruct.insert(30)
    myStruct.insert(40)
    print(myStruct.search(30))
    myStruct.remove(20)
    myStruct.insert(50)
    print(myStruct.search(50))
    print(myStruct.random())
