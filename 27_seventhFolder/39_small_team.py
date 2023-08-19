# https://leetcode.com/problems/smallest-sufficient-team/
# Question : In a project, you have a list of required skills req_skills, and a list of people.
# The ith person people[i] contains a list of skills that the person has.
# Consider a sufficient team: a set of people such that for every required skill in req_skills,
# there is at least one person in the team who has that skill. We can represent these teams by the
# index of each person.
# For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person.
# You may return the answer in any order.
# It is guaranteed an answer exists.
#
# Question Type : ShouldSee
# Used : It is like box stacking. Please note that we use bit masking to reach the required team
#        which is having lesser size.
# TODO :: add explanation


def find_small_team(req_skills, people):
    skill_map = {}
    for i, skill in enumerate(req_skills):
        skill_map[skill] = i

    covered_skill = 0
    for skill in req_skills:
        i = skill_map[skill]
        covered_skill |= 1 << i

    print("Required", bin(covered_skill))

    n = len(people)
    l = (covered_skill + 1)
    min_team = [None] * l
    for i in range(n):
        person_skill = 0
        person = people[i]
        for skill in person:
            index = skill_map[skill]
            person_skill |= 1 << index
        print(i, bin(person_skill))
        min_team[person_skill] = [i]

    for i in range(l):
        for j in range(0, i):
            if min_team[i] is None or min_team[j] is None:
                continue
            current_skill = i
            previous_skill = j
            new_skill = current_skill | previous_skill
            new_team = min_team[i] + min_team[j]
            if min_team[new_skill] is None or len(min_team[new_skill]) > len(new_team):
                min_team[new_skill] = new_team

    print("Small Team :", min_team[covered_skill])


if __name__ == "__main__":
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    find_small_team(req_skills, people)

    print("")
    req_skills = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    people = [["algorithms", "math", "java"],
              ["algorithms", "math", "reactjs"],
              ["java", "csharp", "aws"],
              ["reactjs", "csharp"],
              ["csharp", "math"],
              ["aws", "java"]]
    find_small_team(req_skills, people)
