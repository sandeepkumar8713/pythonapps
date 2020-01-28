# Question : Given (x, y) coordinates, create a function such that each coordinate is uniquely mapped
# to an integer. Also make sure that given an integer, you should be able to find (x, y) coordinates.
# So F(x, y) = z and also that inverse F(z) = (x, y)
#
# Question Type : ShouldSee
# Used : Make use of hash map. This solution is similar to open addressing. For given x,y calculate distance from
#        origin i.e. z= sqrt(x^2 + y^2). Now check if z is present in map, and its x,y pair matches.
#        If exists, add 0.0001 to z and try again. If not exist, insert z with x,y in map.
# Complexity : O(n) insert O(1) search

import math


class DataStructure:
    def __init__(self):
        self.map = dict()

    def insert(self, x, y):
        z = math.sqrt(x*x + y*y)
        while z in self.map.keys():
            if self.map[z][0] == x and self.map[z][1] == y:
                return z
            z += 0.0001
        self.map[z] = [x, y]
        return z

    def get(self, z):
        if z in self.map.keys():
            return self.map[z]
        return None


if __name__ == "__main__":
    dataStructure = DataStructure()
    z = dataStructure.insert(3, 4)
    print ("%s %s" % (z, dataStructure.get(z)))
    z = dataStructure.insert(3, 4)
    print ("%s %s" % (z, dataStructure.get(z)))
    z = dataStructure.insert(3, -4)
    print ("%s %s" % (z, dataStructure.get(z)))
    z = dataStructure.insert(-3, 4)
    print ("%s %s" % (z, dataStructure.get(z)))
    z = dataStructure.insert(-3, -4)
    print ("%s %s" % (z, dataStructure.get(z)))
