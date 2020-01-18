# https://www.careercup.com/question?id=6266160824188928
# https://leetcode.com/discuss/interview-experience/297576/Google-or-L3-or-MTV-or-March-2019-Reject
# Question : Given a room with thief on left side of the room with finite number of sensors.
# He has to reach on right side missing the sensors. Each sensor is placed at any random point in the room and has
# its coverage in the radius r. Find out if the thief can reach to the right side without touching
# the range of any sensor.
# The third interviewers asked a question about flippy birds. Say in a 2d space. You are a flippy bird
# and you are facing some obstacles. How do you know if you can cross all the obstacles and reach the other end.
#
# Used : Yeah, this is percolation problem solvable using UnionFind.
#        https://www.coursera.org/lecture/algorithms-part1/union-find-applications-OLXM8
#        There are should be 2 disjoint set representing 2 walls.(left and right). Now start making union of sensors
#        with other sensor and walls. After this, if the 2 walls have same parent(not disjoint) it means that they
#        are connected, so thief can't pass through it. The two walls should be disjoint for a pass.
#        Logic : def canGoFromLeftToRight(roomHeight, sensors, r):
#        ids = range(len(sensors))
#        top = [], bottom = []
#        for i,[x,y] in enumerate(sensors):
#           if y+r >= roomHeight: # overlaps top side of the room
#               top += [i]
#           if y <= r: # overlaps bottom side of the room
#               bottom += [i]
#        if not top or not bottom: return True
#        for i,j in zip(top, top[1:]): union(j,i, ids)
#        for i,j in zip(bottom, bottom[1:]): union(i,j, ids)
#        for i,[x,y] in enumerate(sensors):
#           for I,[X,Y] in enumerate(sensors[i+1:],i+1):
#               if (X-x)*(X-x) + (Y-y)*(Y-y) <= 4*r*r:
#                   union(i,I, ids)
#        return find(top[0], ids) != find(bottom[0], ids)
# Complexity : O(n^2)


def union(i, j, ids):
    ids[find(i, ids)] = find(j, ids)


def find(i, ids):
    while (i != ids[i]):
        ids[i] = ids[ids[i]]
        i = ids[i]
    return i


# Assume all sensors are within a room, the actual width of the room does not matter.
def canGoFromLeftToRight(roomHeight, sensors, r):
    ids = range(len(sensors))

    top = []
    bottom = []
    for i,[x,y] in enumerate(sensors):
        if y+r >= roomHeight: # overlaps top side of the room
            top += [i]
        if y <= r: # overlaps bottom side of the room
            bottom += [i]

    if not top or not bottom:
        return True

    # unite all sensors overlapping the top
    for i,j in zip(top, top[1:]):
        union(j,i, ids)

    # unite all sensors overlapping the bottom
    for i,j in zip(bottom, bottom[1:]):
        union(i,j, ids)

    # unite all sensors overlapping each other
    for i,[x,y] in enumerate(sensors):
        for I,[X,Y] in enumerate(sensors[i+1:],i+1):
            if (X-x)*(X-x) + (Y-y)*(Y-y) <= 4*r*r:
                union(i,I, ids)

    return find(top[0], ids) != find(bottom[0], ids)


if __name__ == "__main__":
    print canGoFromLeftToRight(1, [(0,0),(0.5,0.2),(0.7,0.4),(0.6,0.6),(1,1)], 0.5) # False
    print canGoFromLeftToRight(1, [(0,0),(0.5,0.2),(0.7,0.4),(1,1)], 0.5) # True
