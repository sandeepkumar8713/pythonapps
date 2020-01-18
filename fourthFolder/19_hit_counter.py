# https://www.geeksforgeeks.org/design-a-hit-counter/
# Question : Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Used : Here we try to keep hit count at each timestamp
#        Make 2 arrays of size 0. times and hit.
#        On hit call, update hit count and timestamp in times at timestamp % 300. Overwrite old timestamp
#        on getHit call, sum the hit count where timestamp - times[i] < 300
# Complexity : O(1)


times = [0] * 300
hits = [0] * 300


def hit(timestamp):
    idx = timestamp % 300
    if times[idx] != timestamp:
        times[idx] = timestamp
        hits[idx] = 1
    else:
        hits[idx] += 1


def getHits(timestamp):
    res = 0
    for i in range(300):
        if timestamp - times[i] < 300:
            res += hits[i]
    return res


if __name__ == "__main__":
    hit(0)
    hit(1)
    hit(2)
    hit(3)
    print getHits(4)
    print hits
    print getHits(300)
    print getHits(301)
