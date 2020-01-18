# Question : You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
# '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example
# we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the
# lock will stop turning and you will be unable to open it. Given a target representing the value of the wheels
# that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it
# is impossible.
#
# Example : Input: deadEnds = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
#
# Used : We are going to do a bi-directional BFS. One from source, other from target. While doing BFS we will maintain
#        2 queue. We will loop through q1 and append new values in q2. Next we will loop over q2 and append in q1.
#        Put dead end nodes in visited list.
#        Logic : def openLock(start, target, deadEnds):
#        queue1 = [start]
#        queue2 = [target]
#        count = 1, visited = set()
#        for deadEnd in deadEnds: visited.add(deadEnd)
#        if start in visited: return -1
#        if target in visited: return -1
#        while len(queue1) != 0 and len(queue2) != 0:
#           temp = []
#           for num in queue1:
#               visited.add(num)
#               chars = list(num)
#               for j in range(4):
#                   nextStr1, nextStr2 = getTwoPossibility(chars, j)
#                   if checkIfPresent(queue2, temp, visited, nextStr1):
#                       return count
#                   if checkIfPresent(queue2, temp, visited, nextStr2):
#                       return count
#           queue1 = queue2
#           queue2 = temp
#           count += 1
#        return -1
#        def checkIfPresent(otherQueue, temp, visited, nextStr):
#        if nextStr not in visited:
#           if nextStr in otherQueue:
#               return True
#           temp.append(nextStr)
#        return False
# Complexity : O(n) n is the number of possibilities (here 10000)


def charToDigit(ch):
    return ord(ch) - ord('0')


def digitToChar(i):
    return unichr(i + ord('0'))


def getTwoPossibility(chars, j):
    oldChar = chars[j]
    digit = charToDigit(oldChar)
    inc = (digit + 1) % 10
    dec = (digit - 1) % 10

    chars[j] = digitToChar(inc)
    str1 = ""
    str1 = str1.join(chars)

    chars[j] = digitToChar(dec)
    str2 = ""
    str2 = str2.join(chars)

    chars[j] = oldChar

    return str1, str2


def checkIfPresent(otherQueue, temp, visited, nextStr):
    if nextStr not in visited:
        if nextStr in otherQueue:
            return True
        temp.append(nextStr)
    return False


def openLock(start, target, deadEnds):
    queue1 = [start]
    queue2 = [target]
    count = 1
    visited = set()
    for deadEnd in deadEnds:
        visited.add(deadEnd)

    if start in visited:
        return -1
    if target in visited:
        return -1

    while len(queue1) != 0 and len(queue2) != 0:
        temp = []
        for num in queue1:
            visited.add(num)
            chars = list(num)
            for j in range(4):
                nextStr1, nextStr2 = getTwoPossibility(chars, j)
                if checkIfPresent(queue2, temp, visited, nextStr1):
                    return count
                if checkIfPresent(queue2, temp, visited, nextStr2):
                    return count
        queue1 = queue2
        queue2 = temp
        count += 1

    return -1


if __name__ == "__main__":
    source = "0000"
    target = "0202"
    deadEnds = ["0201", "0101", "0102", "1212", "2002"]
    print openLock(source, target, deadEnds)
