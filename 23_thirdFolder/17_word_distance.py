# CTCI : Q17_11_Word_Distance
# Question : You have a large text file containing words. Given any two words find the
# shortest distance (in terms of number of words) between them in the file. If the
# operation will be repeated many times for the same file (but different pairs of words)
# can you optimize your solution?
#
# Question Type : Generic
# Used : Make a map of location list. Here key would be the word and value would be list of
#        its locations in the file.
#        From the map get 2 location lists for the given words.
#        Now loop through the two list to find best pair(minimum distance).
#        Logic :
#        i = 0, j = 0
#        bestPair = [locations1[0], locations2[0]]
#        while i < len(locations1) and j < len(locations2):
#           currentPair = [locations1[i], locations2[j]]
#           updateBest(bestPair, currentPair)
#           if currentPair[0] < currentPair[1]: i += 1
#           else: j += 1
#        return bestPair
#
#        def updateBest(bestPair, currentPair):
#        bestdiff = abs(bestPair[0] - bestPair[1])
#        currentDiff = abs(currentPair[0] - currentPair[1])
#        if currentDiff < bestdiff:
#           bestPair[0] = currentPair[0]
#           bestPair[1] = currentPair[1]
# Complexity : To make map: O(n) To find distance: O(A+B) where A and B are occurrence count of word a and b


def getLocationMap(words):
    locationMap = dict()
    for i in range(len(words)):
        word = words[i]
        if word in locationMap.keys():
            locationMap[word].append(i)
        else:
            locationMap[word] = [i]
    return locationMap


def updateBest(bestPair, currentPair):
    bestdiff = abs(bestPair[0] - bestPair[1])
    currentDiff = abs(currentPair[0] - currentPair[1])
    if currentDiff < bestdiff:
        bestPair[0] = currentPair[0]
        bestPair[1] = currentPair[1]


def findClosestDist(word1, word2, locationMap):
    if word1 not in locationMap.keys() or word2 not in locationMap.keys():
        return None

    locations1 = locationMap[word1]
    locations2 = locationMap[word2]
    i = 0
    j = 0

    print(locations1, locations2)
    bestPair = [locations1[0], locations2[0]]
    while i < len(locations1) and j < len(locations2):
        currentPair = [locations1[i], locations2[j]]
        updateBest(bestPair, currentPair)
        if currentPair[0] < currentPair[1]:
            i += 1
        else:
            j += 1
    return bestPair


if __name__ == "__main__":
    word1 = "river"
    word2 = "life"
    textFile = "As they rounded a bend in the path that ran beside the river Lara recognized the silhouette of a fig tree atop a nearby hill. The weather was hot and the days were long. The fig tree was in full leaf but not yet bearing fruit. " \
               "Soon Lara spotted other landmark an outcropping of limestone beside the path that had a silhouette like a man face a marshy spot beside the river where the waterfowl were easily startled a tall tree that looked like a man with his arms upraised. They were drawing near to the place where there was an island in the river. The island was a good spot to make camp. They would sleep on the island tonight. " \
               "Lara had been back and forth along the river path many times in her short life. Her people had not created the path it had always been there like the river but their deerskin-shod feet and the wooden wheels of their handcarts kept the path well worn. Laras people were salt traders and their livelihood took them on a continual journey."
    textFile = textFile.replace(",", "")
    textFile = textFile.replace(".", "")
    words = textFile.split(" ")
    locationMap = getLocationMap(words)
    print(findClosestDist(word1, word2, locationMap))
