# https://careercup.com/question?id=5078647835197440
# Question : Given n number of persons in a park. One of them is having a virus. But we don't know whom. Also, the
#            position of all persons is given. A contaminated person can spread it up to d distance. When the best
#            case (Spread is minimum) and the worst case(Spread is maximum) would occur?
#
# Question Type : ShouldSee
# Used : Try to make islands of people who are within the given distance d. Now the islands with max and min people
#        are answers.
#        islands = [], first = position[0], count = 1
#        for i in range(1, len(position)):
#           second = position[i]
#           if abs(second-first) <= d: count += 1
#           else: islands.append(count), count = 1
#           if i == len(position)-1: islands.append(count)
#           first = second
# Complexity : O(n)


def spread(d, position):
    if len(position) <= 2:
        return len(position), len(position)

    islands = []
    first = position[0]
    count = 1

    for i in range(1, len(position)):
        second = position[i]
        if abs(second-first) <= d:
            count += 1
        else:
            islands.append(count)
            count = 1
        if i == len(position)-1:
            islands.append(count)
        first = second

    return min(islands), max(islands)


if __name__ == "__main__":
    position = [1, 3, 5, 9, 14]
    d = 5
    print(spread(d, position))

    position = [1, 3, 5, 9, 14, 21]
    d = 5
    print(spread(d, position))

    position = [1, 3, 5, 14, 19]
    d = 5
    print(spread(d, position))
