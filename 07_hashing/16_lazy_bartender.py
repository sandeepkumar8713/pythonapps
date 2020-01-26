# https://practice.geeksforgeeks.org/problems/lazy-bartender-amazon-question
# Question : There are N number of possible drinks.(n1,n2..)
# Has C number of fixed customers.
# Every customer has fixed favourite set of drinks.
# Bartender has to create least possible number of drinks
# to suffice need of all the customers
#
# Cust1: n3,n7,n5,n2,n9
# Cust2: n5
# Cust3: n2,n3
# Cust4: n4
# Cust5: n3,n4,n5,n7,n4
#
# Output: 3(n3,n4,n5)
#
# Question Type : Easy
# Used : For the given input matrix make a map drinkCustMap : key (drink) : value (list of customer who like it)
#        Run a loop till this map is empty. Find the drink which is most fav to all, serve it.
#           Remove that drink from map. Remove those customers from the map who are already served.
#           break if maxFavdrink is not found.
# Complexity : O(n * m)


def findMaxFavDrink(drinkCustMap):
    maxCustCount = 0
    maxFavDrink = -1
    for drink, custList in drinkCustMap.items():
        if len(custList) > maxCustCount:
            maxCustCount = len(custList)
            maxFavDrink = drink

    return maxFavDrink


def removeCustServed(drinkCustMap, custServedList):
    for drink, custList in drinkCustMap.items():
        for custServed in custServedList:
            if custServed in custList:
                custList.remove(custServed)


def serveDrink(custChoices):
    custCount = len(custChoices)
    drinkCustMap = dict()

    custIndex = 0
    for custChoice in custChoices:
        for drink in custChoice:
            if drink in drinkCustMap.keys():
                drinkCustMap[drink].append(custIndex)
            else:
                drinkCustMap[drink] = [custIndex]
        custIndex += 1

    while len(drinkCustMap.keys()) != 0:
        drinkToBeServed = findMaxFavDrink(drinkCustMap)
        if drinkToBeServed == -1:
            break
        print(drinkToBeServed)
        custServedList = drinkCustMap[drinkToBeServed]
        del drinkCustMap[drinkToBeServed]
        removeCustServed(drinkCustMap, custServedList)


if __name__ == "__main__":
    custChoices = [[3, 7, 5, 2, 9],
                   [5],
                   [2, 3],
                   [4],
                   [3, 4, 5, 7]]
    serveDrink(custChoices)
