# CTCI : Q6_10_Test_Strips
# Question : You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which
# can be used to detect poison. A single drop of poison will turn the test strip positive permanently.
# You can put any number of drops on a test strip at once and you can reuse a test strip as many times
# as you'd like (as long as the results are negative). However, you can only run tests once per day and
# it takes seven days to return a result. How would you figure out the poisoned bottle in as few days
# as possible? Write code to simulate your approach.
#
# Question Type : ShouldSee
# Used : We can take each bottle number and look at its binary representation. If there's a 1
#        in the ith digit, then we will add a drop of this bottle's contents to test strip i.
#        We wait seven days, and then read the results.
#        If test strip i is positive, then set bit i of the result value. So each the strips
#        would set 1 or 0 in the result to some up with the id of bottle which is poisoned.
#        Observe that 2^10 is 1024, so 10 test strips will be enough to handle up to 1024 bottles.
# Complexity : O(n * m) or O(n lon n)


class Bottle:
    def __init__(self, id):
        self.id = id
        self.poisoned = False

    def setPoisoned(self, poisoned):
        self.poisoned = poisoned


class TestStrip:
    def __init__(self, id):
        self.id = id
        self.bottlesToTested = []

    def addBottle(self, bottle):
        self.bottlesToTested.append(bottle)


def runTest(bottles, testStrips):
    for bottle in bottles:
        bottleId = bottle.id

        bitIndex = 0
        while bottleId != 0:
            if bottleId & 1 == 1:
                testStrip = testStrips[bitIndex]
                testStrip.addBottle(bottle)
            bottleId >>= 1
            bitIndex += 1


def getResult(testStrips):
    poisonedBottleId = 0
    for testStrip in testStrips:
        bottlesToTested = testStrip.bottlesToTested
        for bottle in bottlesToTested:
            if bottle.poisoned:
                testStripId = testStrip.id
                poisonedBottleId |= 1 << testStripId
    return poisonedBottleId


def initializeInput(bottles, bottleCount, testStrips, stripCount):
    for i in range(0, bottleCount):
        bottle = Bottle(i)
        bottles.append(bottle)
    for i in range(0, stripCount):
        testStrip = TestStrip(i)
        testStrips.append(testStrip)


if __name__ == "__main__":
    bottleCount = 1000
    stripCount = 10
    poisonedBottleId = 18

    bottles = []
    testStrips = []
    print ("Given poisonedBottleId : " + str(poisonedBottleId))

    initializeInput(bottles, bottleCount, testStrips, stripCount)

    poisonedBottle = bottles[poisonedBottleId - 1]
    poisonedBottle.setPoisoned(True)

    runTest(bottles, testStrips)
    foundId = getResult(testStrips) + 1
    print ("Found poisonedBottleId : " + str(foundId))
