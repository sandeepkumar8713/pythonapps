# https://leetcode.com/problems/my-calendar-iii/
# Similar : https://leetcode.com/problems/my-calendar-i/
# Similar : 01_array/06_minimum_platform
# Question : Implement a MyCalendarThree class to store your events. A new event can always be added.
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half
# open interval [start, end), the range of real numbers x such that start <= x < end. A K-booking happens when K
# events have some non-empty intersection (ie., there is some time that is common to all K events.)
# For each call to the method MyCalendar.book, return an integer K representing the largest integer such that
# there exists a K-booking in the calendar. Your class will be called like this: MyCalendarThree
# cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
# This concept can be used in beggars problem and bus stand problem.
#
# Example : MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3
#
# Question Type : Generic
# Used : Make one dict of timeLine,
#        Add 1 at start of time in timeline and subtract 1 at end of time in timeline.
#        Now loop through the map, keep adding the values, return max total.
# Logic: class MyCalendar:
#        def __init__(self): self.timeLine = dict()
#        def book(self, start, end):
#           if start in self.timeLine:
#               self.timeLine[start] += 1
#           else:
#               self.timeLine[start] = 1
#           if end in self.timeLine:
#               self.timeLine[end] -= 1
#           else:
#               self.timeLine[end] = -1
#           active = ans = 0
#           for time in sorted(self.timeLine):
#               active += self.timeLine[time]
#               ans = max(ans, active)
#           return ans
# Complexity : O(n log n)


class MyCalendar:
    def __init__(self):
        self.timeLine = dict()

    def book(self, start, end):
        if start in self.timeLine:
            self.timeLine[start] += 1
        else:
            self.timeLine[start] = 1
        if end in self.timeLine:
            self.timeLine[end] -= 1
        else:
            self.timeLine[end] = -1

        active = ans = 0
        for time in sorted(self.timeLine):
            active += self.timeLine[time]
            ans = max(ans, active)

        return ans


if __name__ == "__main__":
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(50, 60))
    print(myCalendar.book(10, 40))
    print(myCalendar.book(5, 15))
    print(myCalendar.book(5, 10))
    print(myCalendar.book(25, 55))
