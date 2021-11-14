# https://leetcode.com/discuss/interview-question/294744/Google-or-Onsite-or-Busy-Traffic
# Question : Given a list of cars traveling from point start to end with speed in the format [start,
# end, speed]. You need to return the list of smallest intervals (segments) and the average speed of
# vehicles in each of those intervals. Used for road color coding as per traffic prediction used in
# google maps or lately Uber.
#
# Example : Input: [[0, 14, 90], [3, 15, 80]]
# Output: [[0, 3, 90], [3, 14, 85], [14, 15, 80]]
# Explanation: car1: [0, 14, 90] car 1 travels from point 0 to 14 with speed 90
# car2: [3, 15, 80] car 2 travels from point 3 to 15 with speed 80
# Segments: [0, 3] with average speed 90
# [3, 14] speed is (90 + 80) / 2 = 85, where we take the average of all cars here
# [14, 15] with average speed is 80
#
# Question Type : Generic
# Used : Make a class Event : eventType(open or close), time, speed.
#        Make list of events from the given input intervals.
#        Sort the event list based on time. Now loop over the list, if it a open event,
#        increment the total else decrement the total.
#        If time is not equal to previous time, insert the timestamp along with average in result.
#        Logic : def intervalAverages(intervals):
#        events = []
#        for interval in intervals:
#           events.append(Event('open', interval[0], interval[2]))
#           events.append(Event('close', interval[1], interval[2]))
#        events.sort(key=lambda x: x.time)
#        previousEventTime = 0
#        if len(events) > 0: previousEventTime = events[0].time
#        total = 0, count = 0, result = []
#        for event in events:
#           if event.time != previousEventTime:
#               result.append([previousEventTime, event.time, total/count])
#               previousEventTime = event.time
#           if event.eventType == 'open':
#               total += event.speed
#               count += 1
#           else:
#               total -= event.speed
#               count -= 1
#        return result
# Complexity : O(n log n)


class Event:
    def __init__(self, eventType, time, speed):
        self.eventType = eventType
        self.time = time
        self.speed = speed

    def __str__(self):
        return self.eventType + " " + str(self.time) + " " + str(self.speed)


def intervalAverages(intervals):
    events = []
    for interval in intervals:
        events.append(Event('open', interval[0], interval[2]))
        events.append(Event('close', interval[1], interval[2]))

    # sort list of object based on a attribute
    events.sort(key=lambda x: x.time)
    # for event in events:
    #     print event

    previousEventTime = 0
    if len(events) > 0:
        previousEventTime = events[0].time
    total = 0
    count = 0
    result = []
    for event in events:
        if event.time != previousEventTime:
            result.append([previousEventTime, event.time, total/count])
            previousEventTime = event.time

        if event.eventType == 'open':
            total += event.speed
            count += 1
        else:
            total -= event.speed
            count -= 1

    return result


if __name__ == "__main__":
    intervals = [[0, 14, 90], [3, 15, 80]]
    print(intervalAverages(intervals))
