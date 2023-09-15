Total number of possible Binary Search Trees with n different keys
Catalan number Cn = (2n)!/(n+1)!*n! : 2nCn / (n + 1)

Triangle area
area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

arc angle
math.degrees(math.atan2(p[1] - loc[1], p[0] - loc[0])))

find median from sorted list (odd and even)
medianList.append((sortedList[(k - 1) // 2] + sortedList[k // 2]) / 2)

When we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit

For a given array, if we create all possible subarray. Number at i-th index will have (i + 1) * (N - i) frequency.

i += i & (-i); Add 1 to last set bit of i
i -= i & (-i); Subtract 1 from last set bit of i

Let Points be A and B. So line can be represent by : c1 = a1*A.x + b1*A.y
where a1 = B.y - A.y; b1 = A.x - B.x
Now find determinant b/w lines
determinant = float(a1*b2 - a2*b1)
To find intersecting points :
if determinant == 0: print ("Given lines are parallel")
else: x = (b2*c1 - b1*c2) / determinant; y = (a1*c2 - a2*c1) / determinant

Recall the quadratic formula:
x = [-b +- sqrt(b^2 - 4ac)] / 2a

for interval in intervals:
    events.append(Event('open', interval[0], interval[2]))
    events.append(Event('close', interval[1], interval[2]))
events.sort(key=lambda x: x.time)

quicksort
partition(arr, left, right, pivotLeft, pivotRight):
i = (left - 1) # index of smaller element
pivot = arr[right] # pivot
for j in range(left, right):
    if arr[j] <= pivot:
    i = i + 1
    arr[i], arr[j] = arr[j], arr[i]
arr[i + 1], arr[right] = arr[right], arr[i + 1]
pivotPosition = i + 1
pivot = arr[i + 1]

josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
josephus(1, k) = 1

# BFS
while queue:
    cost, node = queue.pop(0)
    nodeIndex = node[0]
    visitedNodes = node[1]
    if visitedNodes == targetVisit:
        return cost

c = a ^ b

# multiply without operator
res = 0
while b > 0:
if b & 1: res = res + a
    a <<= 1
    b >>= 1
return res

INT_BIT = sys.getsizeof(int())

---------------------------------------------------------------------------------
**AP Formula** : Sn = n/2(2a + (n-1)d)

```python
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = ''

def build_trie(words):
    trie = TrieNode()
    for word in words:
        temp = trie
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
        temp.word = word
    return trie
```

**Merge sort**
1. Uses Auxiliary space
2. Better for large data structure

**Quick Sort**
1. Worst case is O(n^2) for already sorted
2. Locality of reference

**Parent union**
**We cannot use union-find to detect cycles in a directed graph.**

```python
def union(i, j, ids):
    ids[find(i, ids)] = find(j, ids)

def find(i, ids):
    while i != ids[i]:
        ids[i] = ids[ids[i]] # Set grandparent to parent
        i = ids[i]
    return i

# To be called after all unions to find grandfather as well.
for i in range(len(ids)):
    find(i, ids)

# complexity : O(e log v) where e is the number of edges in the graph and v is the number of vertices.
```

**Eulerian Path** is a path in graph that visits every edge exactly once. Eulerian
Circuit is an Eulerian Path which starts and ends on the same vertex.
For that these two conditions must be met:
1) All vertices with nonzero degree belong to a single strongly connected component.
2) In degree and out degree of every vertex is same

for node in route:
    graph[node] = graph.get(node, []) + [i]

**Sort in decreasing order based on area.**
allBoxList.sort(key=lambda x: x.getArea(), reverse=True)

**Use the sorted func with key as second element i.e. score**
result = sorted(inpArr, key=lambda x: x[1])

```python
import functools
def comparator(a, b):
    return a-b
print(sorted(A1, key=functools.cmp_to_key(comparator)))
```

1. For a matrix, diff of indices are same for **diagonal** (left to right)
2. sum of indices are same for diagonal (right to left)


1. A set of n can have 2^n subsets. (**power subset**)


1. To get **sorted key** in dict, loop from **min(keys) to max(keys)**.
2. We can get a sorted list by looping through it. Remember to increment while ele not found.


1. It is known for a string of length n, there are a total of n*(n+1)/2 number of **substrings**.
2. n items make n*(n-1)/2 **pairs**

**Heapq**
import heapq
heapq.heapify(pool)
heapq.heappush(pool, q) # Min heap
heapq.heappush(pool, -q) # Max heap
sumq += heapq.heappop(pool)

```python
def charToIndex(ch):
    return ord(ch) - ord('a')

def indexToChar(i):
    return chr(i + ord('a'))

def indexToChar2(i, start):
    return chr(i + ord(start))

char_set = set()
for i in range(0,26):
    char_set.add(indexToChar2(i, 'a'))

import sys
min_res = sys.maxsize

## Binary search
left = 0
right = 10 - 1
while left < right:
    mid = left + (right - left) // 2

## Pattern search using regex
import re
regexp_1 = re.compile(r'^\*/([1-9]|[0-5][0-9])$') ## matches */45
regexp = re.compile(r'inet [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
regexp = re.compile(r'^0?[0-9]$') ## 0-9, 00-09
atom_reg_exp='(0?[1-9]|[12][0-9]|[3][0-1])' # 0-9, 00-31
atom_reg_exp='(0?[1-9]|[0-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]|)' # 0-9, 00-255
matched_1 = regexp.search('07')
if matched_1:
    sub_string = matched_1.group() ## Gets whole matching string
    sub_string_2 = matched_1.group(1) ## Gets matching string from first bracket
```

# who are the logged in user in linux : $who
# last logged in user : $last
# ls -R : check subdirectories
# find, sed

**To make all possible pairs without index**
for item_1,item_2 in zip(top, top[1:]):

**To make all possible pairs with index**
for i,[x,y] in enumerate(sensors):
    for I,[X,Y] in enumerate(sensors[i+1:],i+1):

**binary representation**
print (bin(covered_skill))

**math library example**
```python
import math
dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

class KStacks:
    def __init__(self, k, n):
        self.k = k  # Number of stacks.
        self.n = n  # Total size of array holding all the 'k' stacks.

if __name__ == "__main__":
    pass
```

**Return a list as a string with no delimiter**
return "".join(digits)

**round upto D digits**
return round(mid, D)
return abs(-12)

**Fetch row using SQLAlchemy**
```
    query = select(document).where(document.c.document_id == document_id)
    res = db_session.execute(query)
    return res.one_or_none()
```

1. LRU implementation https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/
2. **OrderedDict** is implemented using double linked list.
```python
from collections import OrderedDict
cache = OrderedDict()
cache[key] = value
cache.move_to_end(key)     # Move recently used item to end.
cache.popitem(last=False)  # Remove least recently used item from front.
```

**Datetime**
```python
from datetime import datetime, timedelta
past = datetime.now() - timedelta(days=1)
present = datetime.now()
past < present   # True
datetime(3000, 1, 1) < present # False
present - datetime(2000, 4, 4) # datetime.timedelta(days=8515, seconds=56256, microseconds=871972)
```

return "".join(str(digits) for digits in reversed(answer))

**Find index** of element from list
index = animals.index('dog')
print(index)

**error**
ValueError: 'dog' is not in list

**Remove** ele from list
prime_numbers.remove(9)

```
    a=[1,2,3,4,5,6,7]
    a[:2] : [1, 2] ## first two elements
    a[2:] : [3, 4, 5, 6, 7] ## Print all elements from index 2
    a[2] : [1, 2] ## Second element
    
    1. For minus, assume index from right as -1, -2, -3, -4
    a[-2] : 6 ## Second last element
    a[-2:] : [6, 7] ## last two elements
    a[:-2] : [1, 2, 3, 4, 5] ## Print all elements except last two
    
    a[:-2] + a[-2:] : [1, 2, 3, 4, 5, 6, 7] ## Partition the array at last 2
    
    a[::-1] : [7, 6, 5, 4, 3, 2, 1] ## Reverse the given array
    
    a[::] : [1,2,3,4,5,6,7] ## Copy of given array
    a[0:2] : [1, 2] ## end index is not included in the range.
    
    class Graph:
        def __init__(self, n):
            # key : list
            self.graph = dict()
            for i in range(n):
                self.graph[i] = []
```

**Replace** will return new string
replaced = filePathName.replace("./", "")

To make a set as in key in dict. Convert it as **frozenset**.
frozenset({1,2,3})
Or you can use bit vector

For DP with DFS, Try to keep DFS definition within the function.
So less number of arguments will be passed. So less **context switching**.

1. Add custom sort for Node class
2. Note that it is **comparison**
setattr(Node, "__lt__", lambda self, other: self.data <= other.data)

**Traversing** through all the nodes. A way to mark visited nodes in adjacency list.
```python
for i in range(len(graph[u])):
    v = graph[u].pop(i)
    rt = dfs(v, current_route + [v], current_num_tickets + 1)
    graph[u].insert(i, v)
```

Check if string consists only of **digits**
if sub_str[1].isdigit():
    self.is_digit = True

**Delete last element in min heap**
def delete_last_element(heap):
    if len(heap) >= 2:
        if heap[-1] < heap[-2]:
            heap.pop(-2)
            return
    heap.pop(-1)


**level order**
class Node:
    def __init__(self, data):
        self.data = data
        self.hd = sys.maxsize
        self.left = None
        self.right = None

**dict sorted on keys**
for key in sorted(map.keys()):
    print(map[key], end=" ")

**remove ele from dict**
for ch in remove:
    del charSet[ch]

f = open(file_name, 'w+')
f.write("Hello\n")
f.close()

using **generator** to create a output list
item_list = [1, 2, 4, 10]
x = [item for item in item_list if item > 5]
y = [item if item > 5 else -1 for item in item_list]

---------------------------------------------------------------

**Rest call Example**

```python
import requests

# Fetch data from the API
url = "https://jsonmock.hackerrank.com/api/articles?page=2"
response = requests.get(url)
data = response.json()

# Filter out items with null titles and story titles
filtered_data = [item for item in data["data"] if item["title"] or item["story_title"]]

# Use story title if title is missing, and vice-versa
for item in filtered_data:
    if not item["title"]:
        item["title"] = item["story_title"]
    if not item["story_title"]:
        item["story_title"] = item["title"]

# Sort the data based on multiple item attributes
sorted_data = sorted(filtered_data, key=lambda x: (x["title"], x["num_comments"]))
```

---------------------------------------------------------------

**Asynchronous Server Gateway interface**
Web Server : Uvicorn(ASGI), Tomcat
Rest Framework : FastAPI, Flask, Django
**Memory management** in Python
data frame? in pandas
python 3.11
Python celery
Async and await in Python
generators (yield)

## Remaining
1. Compare reactiveness in Java and Python

---------------------------------------------------------------
