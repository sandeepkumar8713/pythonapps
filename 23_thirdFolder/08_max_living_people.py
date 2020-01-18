# CTCI : Q16_10_Living_People
# Question : Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of people alive. You may assume that all people were born
# between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
# be included in that year's count. For example, Person (birth= 1908, death= 1909) is included in the
# counts for both 1908 and 1909.
#
# Used : We can create an array of the years, where the value at delta[year] indicates how the population
# changed in that year. To create this array, we walk through the list of people and increment when they're
# born and decrement when they die. Once we have this array(delta), we can walk through each of the years,
# tracking the current population as we go (adding the value at array[year] each time). While keeping track
# of highest population reached.
# Complexity : O(n + m) n : people count m : year range

import random


class Person:
    def __init__(self, birthYear, deathYear):
        self.birthYear = birthYear
        self.deathYear = deathYear


def maxLiveYear(people, min, max):
    deltaPopulation = [0] * (max - min + 2)
    for person in people:
        birth = person.birthYear - min
        deltaPopulation[birth] += 1

        death = person.deathYear - min
        deltaPopulation[death + 1] -= 1

    maxAliveYear = 0
    maxAlive = 0
    currentlyAlive = 0

    for i in range(len(deltaPopulation)):
        currentlyAlive += deltaPopulation[i]
        if currentlyAlive > maxAlive:
            maxAlive = currentlyAlive
            maxAliveYear = min + i
    return maxAliveYear, maxAlive


if __name__ == "__main__":
    n = 100
    first = 1900
    last = 2000
    people = []
    for i in range(n):
        birthYear = first + random.randint(0, last-first)
        deathYear = birthYear + random.randint(0, last - birthYear)
        person = Person(birthYear, deathYear)
        people.append(person)
        #print (person.birthYear, person.deathYear)
    print (maxLiveYear(people, first, last))
