# https://leetcode.com/problems/race-car/
# Question : Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative
# positions.) Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
# When you get an instruction "A", your car does the following: position += speed, speed *= 2.
# When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 ,
# otherwise speed = 1.  (Your position stays the same.) For example, after commands "AAR", your car goes to positions
# 0->1->3->3, and your speed goes to 1->2->4->-1. Now for some target position, say the length of the shortest
# sequence of instructions to get there.
#
# Example : Input: target = 3
# Output: 2
# Explanation: The shortest instruction sequence is "AA". Your position goes from 0->1->3.
#
# Question Type : Generic
# Used : Will do bfs. At each step will to move in 2 directions : fwd and backward. Loop will run until we hit the
#        target. Through BFS we will get shortest path.
#        Logic :
#        while len(queue) != 0:
#        size = len(queue)
#        while size != 0:
#            currPair = queue.pop(0)
#            pos = currPair[0]
#            speed = currPair[1]
#
#            pos1 = pos + speed
#            speed1 = speed * 2
#            newPair1 = (pos1, speed1)
#            if pos1 == target:
#               return result + 1
#            queue.append(newPair1)
#
#            if speed > 0: speed2 = -1
#            else: speed2 = 1
#            newPair2 = (pos, speed2)
#            key2 = str(pos) + "_" + str(speed2)
#            if key2 not in visitedSpots:
#                queue.append(newPair2)
#                visitedSpots.add(key2)
#            size -= 1
#        result += 1
# Complexity : O(E+V)


def raceCar(target):
    queue = []
    pair = (0, 1)  # position is 0, speed is 1
    queue.append(pair)
    visitedSpots = set()
    visitedSpots.add("0_1")
    result = 0

    while len(queue) != 0:
        size = len(queue)
        while size != 0:
            currPair = queue.pop(0)
            pos = currPair[0]
            speed = currPair[1]

            # Increase speed
            pos1 = pos + speed
            speed1 = speed * 2
            newPair1 = (pos1, speed1)
            if pos1 == target:
                return result + 1

            queue.append(newPair1)

            # Decrease speed
            if speed > 0:
                speed2 = -1
            else:
                speed2 = 1

            newPair2 = (pos, speed2)
            key2 = str(pos) + "_" + str(speed2)
            if key2 not in visitedSpots:
                queue.append(newPair2)
                visitedSpots.add(key2)
            size -= 1
        result += 1

    return -1


if __name__ == "__main__":
    target = 3
    print(raceCar(target))
