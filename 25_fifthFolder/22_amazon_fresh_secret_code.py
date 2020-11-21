# https://leetcode.com/discuss/interview-question/932920/
# Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits.
# The combination will change each day, and the team running the promotion wants to use a code list to make it easy
# to change the combination. The code list contains groups of fruits. Both the order of the groups within the code
# list and the order of the fruits within the groups matter. However, between the groups of fruits, any number,
# and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in
# that location within the group. Write an algorithm to output 1 if the customer is a winner else output 0.
#
# Example: secret code list: [[apple, apple], [banana, anything, banana]]
# Based on the above secret code list, a customer who made either of the following purchases would win the prize:
# orange, apple, apple, banana, orange, banana
# apple, apple, orange, orange, banana, apple, banana, banana
#
# Question Type : Generic
# Used : We use the concept of sliding window here. Keep increasing the window size as long as it match. At the end
#        check if window size is equal to secret code size. If a group matches partially, we move the index of shopping
#        cart back to the previously matched index and reset the codeWordIndex to 0.
#        isWinner(codeList, shoppingCart):
#        lastMatchedindex = 0, codeIndex = 0, codeWordIndex = 0
#        shopCartIndex = lastMatchedindex
#        while codeIndex < len(codeList) and shopCartIndex < len(shoppingCart):
#           if isMatched(shoppingCart[shopCartIndex], codeList[codeIndex][codeWordIndex]):
#               shopCartIndex += 1, codeWordIndex += 1
#               if codeWordIndex == len(codeList[codeIndex]):
#                   codeIndex += 1, codeWordIndex = 0
#                   lastMatchedindex = shopCartIndex
#           else:
#               lastMatchedindex += 1
#               shopCartIndex = lastMatchedindex
#               codeWordIndex = 0
#        return 1 if codeIndex == len(codeList):
# Complexity : O(n)


def isMatched(source, target):
    return "anything" == target or target == source


def isWinner(codeList, shoppingCart):
    lastMatchedindex = 0
    codeIndex = 0
    shopCartIndex = lastMatchedindex
    codeWordIndex = 0
    while codeIndex < len(codeList) and shopCartIndex < len(shoppingCart):
        if isMatched(shoppingCart[shopCartIndex], codeList[codeIndex][codeWordIndex]):
            shopCartIndex += 1
            codeWordIndex += 1
            if codeWordIndex == len(codeList[codeIndex]):
                codeIndex += 1
                lastMatchedindex = shopCartIndex
                codeWordIndex = 0
        else:
            lastMatchedindex += 1
            shopCartIndex = lastMatchedindex
            codeWordIndex = 0

    if codeIndex == len(codeList):
        return 1
    else:
        return 0


if __name__ == "__main__":
    codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]
    print(isWinner(codeList, shoppingCart))

    codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart = ["banana", "orange", "banana", "apple", "apple"]
    print(isWinner(codeList, shoppingCart))

    codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart = ["apple", "banana", "apple", "banana", "orange", "banana"]
    print(isWinner(codeList, shoppingCart))

    codeList = [["apple", "apple"], ["apple", "apple", "banana"]]
    shoppingCart = ["apple", "apple", "apple", "banana"]
    print(isWinner(codeList, shoppingCart))

    codeList = [["apple", "banana"]]
    shoppingCart = ["apple", "apple", "banana"]
    print(isWinner(codeList, shoppingCart))
