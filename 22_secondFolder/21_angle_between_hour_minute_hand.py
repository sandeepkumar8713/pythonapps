# https://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/
# Question : This problem is know as Clock angle problem where we need to find angle between hands of an
# analog clock at a given time.
#
# Input:  h = 12:00, m = 30.00
# Output: 165 degree
#
# Question Type : ShouldSee
# Used : Calculate the angles moved by hour and minute hands with reference to 12:00
#        hour_angle = 0.5 * (h * 60 + m)
#        minute_angle = 6 * m
#        To calculate angle subtract the above two.
#        angle = abs(hour_angle - minute_angle)
#        Return the smaller angle of two possible angles
# Complexity : O(1)


def calcAngle(h, m):
    if h < 0 or m < 0 or h > 12 or m > 60:
        print('Wrong input')

    if h == 12:
        h = 0
    if m == 60:
        m = 0

    # Calculate the angles moved by hour and minute hands with reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)

    return angle


if __name__ == "__main__":
    h = 9
    m = 60
    print('Angle ', calcAngle(h, m))
