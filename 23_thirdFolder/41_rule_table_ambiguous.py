# https://www.careercup.com/question?id=5651823193489408
# Question : You have a table :
# Rule1 Rule2 Rule3 Value
# A1 B2 C3 40
# A1 B1 C1 20
# A2 B2 C2 10
# A1 B1 C1 40
# * B1 * 20
# A5 B2 * 10
# Now if I have a condition A1 && B2 && C3 i will get output as 40.
# If I input A1 && B1 && C1 I will get two results 40 and 20 here there the rule is ambiguous.
# "-" in table means any rule, 5th row matches with any row with B1 as rule2, so there is also ambiguity in result.
# Now given that table as input (m * n) where n is number of available rules combination (here its 6) and m rules
# (3 in this case) , output if the table is ambiguous i.e it will output two different result for same query.
#
# Question Type : OddOne
# Used :
# Complexity :
#
# TODO :: add code

