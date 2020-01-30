# https://leetcode.com/problems/brace-expansion-ii/
# https://leetcode.com/problems/brace-expansion-ii/discuss/409894/Python-with-explanation-Stack-solution.
# Question : Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr)
# to denote the set of words the expression represents.
# Grammar can best be understood through simple examples:
# Single letters represent a singleton set containing that word.
# R("a") = {"a"}
# R("w") = {"w"}
# When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
# R("{a,b,c}") = {"a","b","c"}
# R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
# When we concatenate two expressions, we take the set of possible concatenations between two words where the first
# word comes from the first expression and the second word comes from the second expression.
# R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
# R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
# Formally, the 3 rules for our grammar:
# For every lowercase letter x, we have R(x) = {x}
# For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) U R(e_2) U ...
# For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) * R(e_2)}, where + denotes
# concatenation, and * denotes the cartesian product.
# Given an expression representing a set of words under the given grammar, return the sorted list of words
# that the expression represents.
#
# Example 1:
# Input: "{a,b}{c,{d,e}}"
# Output: ["ac","ad","ae","bc","bd","be"]
#
# Example 2:
# Input: "{{a,z},a{b,c},{ab,z}}"
# Output: ["a","ab","ac","z"]
# Explanation: Each distinct word is written only once in the final answer.
#
# Question Type : ShouldSee
# Used : We will use a stack here to parse the expression.
#        If a character is a {, append it to the stack and start a new set of characters and append that to
#        the stack as well.
#        If a character is a ,, start a new set of characters and append that to the stack.
#        If a character is a },
#        we take a union of all the sets that we have seen so far from the last opening brace and form a list of these.
#        we pop the opening brace out.
#        the group that is at the top of the stack should now become the product of that set and the union that
#        we have formed. So, for all elements in the top of the stack set, they are multiplied to the elements
#        of the union list.
#        If a character is an alphabet, we simply append it to all items in the current set.
#        Logic : def braceExpansionII(expression):
#        if not expression: return []
#        stack = [[""]]
#        for c in expression:
#           if c == '{':
#               stack.append(c)
#               stack.append([""])
#        elif c == ',':
#           stack.append([""])
#        elif c == '}':
#           union = []
#           while stack and stack[-1] != '{':
#                union += stack.pop()
#           stack.pop() # --> brace '{'
#           stack[-1] = [s+u for s in stack[-1] for u in union]
#        else:
#           stack[-1] = [x+c for x in stack[-1]]
#        res = set()
#        while stack:
#           ele = stack.pop()
#           for x in ele:
#               res.add(x)
#        return sorted(res)
# Complexity : O(n ^ 2)


def braceExpansionII(expression):
    if not expression:
        return []

    # Stack contains empty set first.
    stack = [[""]]

    for c in expression:
        if c == '{':
            stack.append(c)
            stack.append([""])

        elif c == ',':
            stack.append([""])

        # If c is a '}', collapse and take union of all sets till we hit a
        # '{'. Then pop the opening brace. Then, take product of the unionized
        # set with that at the stack top. Make the stack top to be this new
        # set.
        elif c == '}':
            union = []
            while stack and stack[-1] != '{':
                union += stack.pop()
            stack.pop() # --> brace '{'

            # Stack top is not the product.
            stack[-1] = [s+u for s in stack[-1] for u in union]

        # If c is a char, append it to all elements in the current set.
        else:
            stack[-1] = [x+c for x in stack[-1]]

    res = set()
    while stack:
        ele = stack.pop()
        for x in ele:
            res.add(x)
    return sorted(res)


if __name__ == "__main__":
    expression = "{a,b}{c,{d,e}}"
    print(braceExpansionII(expression))
