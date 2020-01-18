# https://leetcode.com/discuss/interview-experience/389969/Google-or-L3-or-Seattle-or-Sep-2019-No-Offer
# http://www.petertheobald.com/tech/ghost-solver---in-which-we-ruin-a-great-game/
# Question : Ghost game, its a game played in N players, game begins with empty string. There are 2 rules:
# You can only add such char to the string so that it doesnt becomes a complete valid english word, but it
# should always be a substring of a valid english word.
# If you cant add a char, then you loose. Game ends when a player looses
#
# Game state is: ""
# You cannot add 'a' , as 'a' is a valid english word, but you can add 'c' because its a valid substring of
# [cat, cable, car ....]
# Game state is : "ca"
# You loose, because now if you add 'b' thinking its a valid substring of "cable", but this already becomes
# a valid english word "cab"
#
# After my initail probing of questions, I suggested we can use Trie, in which we keep the dictionary of valid
# english words. As we cant have a subtree after having a valid smaller word, the trie should be sufficiently
# small. In trie node we also keep if this child is at the end of the terminal word (valid word), then the Idea
# was fairly simple try appending any such char to the current state which is not a terminal word.
#
# Game state is: "ca"
# In order to not loose, i would append "f", such that "caf" is still a valid subtring of "cafe"
# Interviewer was satisfied with this approach ran several test cases, coded it!
#
# Follow-up: Now we have to append such char which gurantee that we should win if there is atleast one way
# in which we will not loose on our turn. I tried to give approaches where either the game finishes in N-1 turns
#  such that I don't get to play next turn, or we could color the trie & see if there a path in which the leaf
#  node is not colored by my color then choose it. Interviewer wanted a probablistic approach, I tried couting
# of terminal nodes from the current state in all the paths & then returning the chance terminal / Nontermianl
#  but it didn't added up. I believe this is a conditional probablity problem, with some Math wizardy. We ran out
#  of time, I think it was average I did solved the primary problem but the extension was tough.
#
# TODO :: add code



