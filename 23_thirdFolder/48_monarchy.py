# https://leetcode.com/discuss/interview-question/302164/Google-or-Phone-Screen-or-Monarchy
# Question : Given a list of births and death. Return a list of order of succession of the monarchy.
# It is pre-order in n-ary tree.
#
# Question Type : Easy
# Used : When a birth function is called, we maintain a map of nodes and also make a n-ary
#        tree of the nodes.
#        Monarch map(name: node) is used make n-ary tree(ro attach child to its parent). For
#        death we simply mark them as not alive. After the birth calls.
#        We travel the n-ary in pre-order for order of succession. If a monarch
#        is marked as dead, we don't print it while doing pre-order.
#        Logic : def birth(self, child, parent):
#        monarch = Monarch()
#        monarch.name = child
#        if parent is None and self.firstMonarch is None:
#           self.firstMonarch = monarch
#        else:
#           if not (parent in self.monarchMap):
#                print "Parent not found"
#                return
#           self.monarchMap[parent].children.append(monarch)
#        self.monarchMap[child] = monarch
#        def death(self, name):
#        self.monarchMap[name].isAlive = False
# Complexity : O(n)


class Monarch(object):
    def __init__(self):
        self.name = None
        self.children = []
        self.isAlive = True


class Monarchy(object):
    def __init__(self):
        self.firstMonarch = None
        self.monarchMap = {}

    def birth(self, child, parent):
        # create monarch
        monarch = Monarch()
        monarch.name = child
        # If it's the first monarch
        if parent is None and self.firstMonarch is None:
            self.firstMonarch = monarch
        else:
            # find parent and add child
            if not (parent in self.monarchMap):
                print("Parent not found")
                return
            self.monarchMap[parent].children.append(monarch)
        # Add the monarch to hash table
        self.monarchMap[child] = monarch

    def death(self, name):
        self.monarchMap[name].isAlive = False

    def preOrder(self, node):
        if node:
            if node.isAlive is True:
                # don't print dead people :'(
                print(node.name)
            for child in node.children:
                self.preOrder(child)

    def getOrderOfSuccession(self):
        self.preOrder(self.firstMonarch)


if __name__ == "__main__":
    monarchy = Monarchy()
    monarchy.birth("king", None)
    monarchy.birth("Andy", "king")
    monarchy.birth("Bob", "king")
    monarchy.birth("Catherine", "king")
    monarchy.birth("Matthew", "Andy")
    monarchy.birth("Alex ", "Bob")
    monarchy.birth("Asha ", "Bob")
    monarchy.getOrderOfSuccession()

    print("")
    monarchy.death("Andy")
    monarchy.getOrderOfSuccession()
