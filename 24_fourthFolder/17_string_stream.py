# http://shibaili.blogspot.com/2019/01/359-logger-rate-limiter.html
# https://massivealgorithms.blogspot.com/2016/06/leetcode-359-logger-rate-limiter.html
# https://leetcode.com/problems/logger-rate-limiter/
# Question :  Design a data structure for running stream of string. You have to print a word
# if it has not come within 10 second else ignore it.
#
# Example:
# Logger logger = new Logger();
# logger.shouldPrintMessage(1, "foo"); returns true;
# logger.shouldPrintMessage(2,"bar"); returns true;
# logger.shouldPrintMessage(3,"foo"); returns false;
# logger.shouldPrintMessage(8,"bar"); returns false;
# logger.shouldPrintMessage(10,"foo"); returns false;
# logger.shouldPrintMessage(11,"foo"); returns true;
#
# Question Type : Generic
# Used : Maintain a map of message : timestamp. When the function is called put if message
#        is not there and return True
#        If message is there and time difference is 10 or above, update timestamp and return
#        True. Else return False.
# Logic: def shouldPrint(self, timestamp, message):
#        if message not in self.map.keys():
#           self.map[message] = timestamp
#           return True
#        else:
#           if timestamp - self.map[message] >= 10:
#               self.map[message] = timestamp
#               return True
#           else:
#               return False
# Complexity : O(1)


class Logger:
    def __init__(self):
        self.map = dict()

    def shouldPrint(self, timestamp, message):
        if message not in self.map.keys():
            self.map[message] = timestamp
            return True
        else:
            if timestamp - self.map[message] >= 10:   # Update timestamp only when we are about to print
                self.map[message] = timestamp
                return True
            else:
                return False


if __name__ == "__main__":
    logger = Logger()
    print(logger.shouldPrint(1, "foo"))
    print(logger.shouldPrint(2, "bar"))
    print(logger.shouldPrint(3, "foo"))
    print(logger.shouldPrint(8, "bar"))
    print(logger.shouldPrint(10, "foo"))
    print(logger.shouldPrint(11, "foo"))
