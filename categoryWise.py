# Question : List all category wise question

questionMap = {}

questionMap['arrayCreation'] = {'26_sixthFolder/48_min_inc_to_reach_target'}

questionMap['hashing'] = {'26_sixthFolder/46_good_split_count'}


def getSelectedFilename():
    overallSet = []
    for key, value in questionMap.items():
        overallSet.extend(list(value))
    return overallSet
