# https://leetcode.com/discuss/interview-question/862600/
# Question : Amazon parses logs of user transactions/activity to flag fraudulent activity. The log file is
# represented as an Array of arrays. The arrays consist of the following data:
# [<userid1> <userid2> <# of transactions>]
# Write a function to parse the log data to find distinct users that meet or cross a certain threshold.
# Output should be an array of user-ids that are sorted. If same userid appears in the transaction as userid1
# and userid2, it should count as one occurrence, not two.
#
# Question Type : Easy
# Used : Make a dict of given transactions with uid as key and value as occurrence count. Loop over the dict and
#        append the ids whose count is equal or more than threshold.
# Complexity : O(n)


def updateDict(mydict, key):
    try:
        mydict[key] += 1
    except:
        mydict[key] = 1


def detectFraud(transactions, threshold):
    mydict = dict()
    for log in transactions:
        content = log[0].split(" ")
        idFrom = content[0]
        idTo = content[1]

        updateDict(mydict, idFrom)
        if idFrom != idTo:
            updateDict(mydict, idTo)

    result = []
    for key, count in mydict.items():
        if count >= threshold:
            result.append(key)

    resultInteger = []
    for userId in result:
        resultInteger.append(int(userId))
    sortedIndex = sorted(range(len(resultInteger)), key=resultInteger.__getitem__)
    sortedResult = []
    for index in sortedIndex:
        sortedResult.append(result[index])
    return sortedResult


if __name__ == "__main__":
    transactions = [["345366 89921 45"],
                    ["029323 38239 23"],
                    ["38239 345366 15"],
                    ["029323 38239 77"],
                    ["345366 38239 23"],
                    ["029323 345366 13"],
                    ["38239 38239 23"]]
    threshold = 3
    print(detectFraud(transactions, threshold))
