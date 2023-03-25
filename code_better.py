# Raymond Hettinger : https://www.youtube.com/watch?v=OSGv2VnC0go&t=207s

import urllib
import os
from collections import defaultdict
from collections import ChainMap, namedtuple, deque
from decimal import Decimal, localcontext, Context
import threading
import contextlib
# Higher order function
from functools import lru_cache

# In python3, range is producing item one by one. Not all a time
for i in range(6):
    print(i ** 2)

colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)

for i, color in enumerate(colors):
    print(i, color)

names = ['raymond', 'rachel', 'matthew']
for name, color in zip(names, colors):
    print(name, color)

print(sorted(colors, key=len))


def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# It will print key only
for k in d:
    print(k)

# Deleting values while iterating over it
less_d = {k: d[k] for k in d if not k.startswith('r')}
print(less_d)

# Make dict from 2 lists
const_d = dict(zip(names, colors))
print(const_d)

# Make dict from list with key as index of list
const_d = dict(enumerate(names))
print(const_d)

# Counting frequency
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

d = defaultdict(int)
for color in colors:
    d[color] += 1

# Making dict with values as list
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

while d:
    key, value = d.popitem()
    print(key, value)

# Python contains a container called “ChainMap” which encapsulates many
# dictionaries into one unit. ChainMap is member of module “collections“.
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
# Defining the chainmap
c = ChainMap(d1, d2, d3)

# It is better to return named tuples as it specify the field name
t = namedtuple('TestResults', ['failed', 'attempted'])
t.failed = 0
t.attempted = 4
print(t.failed, t.attempted)

# Unpacking list in a single line
details = 'Raymond', 'Hettinger', 0x30, 'python@exp.com'
fname, lname, age, email = details


# updating multiple state variable
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


print(', '.join(names))

# Using deque we can update list efficiently
d_names = deque(names)
del d_names[0]
d_names.popleft()
d_names.appendleft('mark')


@lru_cache
def web_lookup(url):
    return urllib.urlopen(url).read()


# Changing the context locally only for the 1 division
with localcontext(Context(prec=50)):
    print(Decimal(355) / Decimal(113))

# with open('data.txt') as f:
#     data = f.read()

# Locks will be released after the context is over
lock = threading.Lock()
with lock:
    print('Critical Section1')


@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


with ignored(OSError):
    os.remove('somefile.txt')

with open('help.txt', 'w') as f:
    with contextlib.redirect_stdout(f):
        help(pow)

# Using generator
print(sum(i ** 2 for i in range(10)))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a: a + 10
print(x(5))


# The power of lambda is better shown when you use them as an
# anonymous function inside another function.
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
