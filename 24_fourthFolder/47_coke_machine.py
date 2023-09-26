# https://leetcode.com/discuss/interview-question/307252
# Question : Given a coke machine with a series of buttons. If you press a button it will get you a
# certain range of coke. Find out if it's possible to get the target range of coke. You can press
# buttons any number of times.
#
# Example : Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [100, 110]
# Output: false
# Explanation: if we press first button it might give us 120 volume of coke, not in the target range.
#
# Question Type : ShouldSee
# Used : We do dfs, we pick each button, press it, then call dfs again, recursively until we hit target.
# Logic : def coke_machine(buttons, target, cur_sum=None, memo=None):
#        if memo is None: memo = set()
#        if cur_sum is None: cur_sum = (0, 0)
#        if cur_sum in memo: return False
#        if cur_sum[0] >= target[0] and cur_sum[1] <= target[1]: return True
#        if cur_sum[1] > target[1]:
#           memo.add(cur_sum)
#           return False
#        for button in buttons:
#           if coke_machine(buttons, target, (cur_sum[0] + button[0], cur_sum[1] + button[1])):
#               return True
#        memo.add(cur_sum)
#        return False
# Complexity : O(n) where n is distance between source and target


def cokeMachine(buttons, target, cur_sum=None, memo=None):
    if memo is None:
        memo = set()

    if cur_sum is None:
        cur_sum = (0, 0)

    if cur_sum in memo:
        return False

    if cur_sum[0] >= target[0] and cur_sum[1] <= target[1]:
        return True

    if cur_sum[1] > target[1]:
        memo.add(cur_sum)
        return False

    for button in buttons:
        if cokeMachine(buttons, target, (cur_sum[0] + button[0],
                                          cur_sum[1] + button[1]), memo):
            return True

    memo.add(cur_sum)
    return False


if __name__ == "__main__":
    buttons = [[100, 120], [200, 240], [400, 410]]
    target = [100, 110]
    print(cokeMachine(buttons, target))

    buttons = [[100, 120], [200, 240], [400, 410]]
    target = [90, 120]
    print(cokeMachine(buttons, target))

    buttons = [[100, 120], [200, 240], [400, 410]]
    target = [300, 360]
    print(cokeMachine(buttons, target))

    buttons = [[100, 120], [200, 240], [400, 410]]
    target = [310, 360]
    print(cokeMachine(buttons, target))
