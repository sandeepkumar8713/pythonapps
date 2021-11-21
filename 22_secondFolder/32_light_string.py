# https://leetcode.com/discuss/interview-question/342129/Google-or-Onsite-or-Light-String
# Question : Create a class LightString to manage a string of lights, each of which has a value 0 or 1
# indicating whether it is on or off.
#
# Example :
# LightString str = new LightString(5); // all lights are initially off
# str.isOn(0); // false
# str.isOn(1); // false
# str.isOn(2); // false
# str.toggle(0, 2);
# str.isOn(0); // true
# str.isOn(1); // true
# str.isOn(2); // true
# str.isOn(3); // false
# str.toggle(1, 3);
#
# Question Type : Generic
# Used : We used binary indexed tree. We add 1 to each index in given range for toggle.
#        To check if on or not we check if mod of 2 is even or not
#        Logic : class BIT:
#        def add(self, i):
#        i += 1
#        while i <= self.n:
#            self.l[i] += 1
#            i += i & -i
#        def query(self, i):
#        i += 1
#        ans = 0
#        while i:
#           ans += self.l[i]
#           i -= i & -i
#        return ans
#        class LightString:
#        def __init__(self, n):
#           self.tree = BIT(n)
#        def isOn(self, i):
#           return bool(self.tree.query(i) % 2)
#        def toggle(self, start, end):
#           self.tree.add(start)
#           self.tree.add(end + 1)
# Complexity : O(log n) both toggle and query


class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0] * (n + 1)

    def add(self, i):
        i += 1
        while i <= self.n:
            self.l[i] += 1
            i += i & -i

    def query(self, i):
        i += 1
        ans = 0
        while i:
            ans += self.l[i]
            i -= i & -i
        return ans


class LightString:
    def __init__(self, n):
        self.tree = BIT(n)

    def isOn(self, i):
        return bool(self.tree.query(i) % 2)

    def toggle(self, start, end):
        self.tree.add(start)
        self.tree.add(end + 1)


if __name__ == "__main__":
    s = LightString(5)
    assert not s.isOn(0)
    assert not s.isOn(1)
    assert not s.isOn(2)
    s.toggle(0, 2)
    assert s.isOn(0)
    assert s.isOn(1)
    assert s.isOn(2)
    assert not s.isOn(3)
    s.toggle(1, 3)
    assert not s.isOn(1)
    assert not s.isOn(2)
    assert s.isOn(3)
    s.toggle(0, 4)
    assert not s.isOn(0)
    assert s.isOn(1)
    assert s.isOn(2)
    assert not s.isOn(3)
    assert s.isOn(4)