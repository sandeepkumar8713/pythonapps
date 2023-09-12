## Interview questions

Link : https://codesubmit.io/interview/python-interview-questions

The data types in Python are:
Numbers, String, List, Tuple, Set, Dictionary

```python
class Trie:
    def __init__(self):
        self.root = None
    
    def search(self):
        pass

# List all attributes and dunder menthods of the given object
t = Trie()
print (t.__dir__())
# ['root', '__module__', '__init__', 'insert', 'subStringSearch', 'search', '__dict__', '__weakref__', '__doc__', 
# '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', 
# '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__subclasshook__', 
# '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

print(dir(int))
```

Link : https://www.tutorialsteacher.com/python/magic-methods-in-python

Add triple quotes ''' to add multi line string

**Magic methods** or **Dunder methods** are not meant to be invoked directly by you, but the invocation happens internally from
the class on a certain action. For example, when you add two numbers using the + operator, internally, the __add__() method 
will be called. Use the **dir()** function to see the number of magic methods inherited by a class.

Magic methods are most frequently used to define **overloaded behaviours** of predefined operators in Python

```python
num=10
res = num.__add__(5) 
print(res) # 15
```

In Python the __new__() magic method is **implicitly called** before the __init__() method. The __new__() method returns a new object,
which is then **initialized** by __init__(). 

__str__() is overridden to return a printable **string representation** of any user defined class.

```python
def __str__(self):
    return 'name='+self.name+', salary=$'+str(self.salary)
```

The str() function internally calls the __str__() method defined in the above employee class.

__new__(cls, other) 	To get called in an object's instantiation.
__init__(self, other) 	To get called by the __new__ method.
__del__(self) 	Destructor method. 

__getattr__(self, name) 	Is called when the accessing attribute of a class that does not exist.
__setattr__(self, name, value) 	Is called when assigning a value to the attribute of a class.
__delattr__(self, name) 	Is called when deleting an attribute of a class. 

__str__(self) 	To get called by built-int str() method to return a string representation of a type.
__repr__(self) 	To get called by built-int repr() method to return a machine readable representation of a type.
__unicode__(self) 	To get called by built-int unicode() method to return an unicode string of a type.
__format__(self, formatstr) 	To get called by built-int string.format() method to return a new style of string.
__hash__(self) 	To get called by built-int hash() method to return an integer.
__nonzero__(self) 	To get called by built-int bool() method to return True or False.
__dir__(self) 	To get called by built-int dir() method to return a list of attributes of a class.
__sizeof__(self) 	To get called by built-int sys.getsizeof() method to return the size of an object. 

**Break and continue can be used together.** “Break” will stop the current loop from execution, while “continue” will cause 
the next iteration of the loop to run immediately.  

An **iterator has the whole sequence in memory** before it returns the first result. An iterator uses the "return". A generator 
**calculates each result at the moment** it is called for. The next result is unknown. A generator uses "yield".

Interpretor vs Compiler
A compiler translates code written in a **high-level programming language into a lower-level language** like assembly language, 
object code and machine code (binary 1 and 0 bits). It **converts the code ahead of time** before the program runs.

An interpreter **translates the code line-by-line** when the program is **running**.

**Difference**
1. A compiler takes in the entire program and requires a **lot of time to analyze** the source code. Whereas the interpreter takes a 
   **single line** of code and very little time to analyze it.
2. Compiled code runs faster, while **interpreted code runs slower**.
3. A compiler **displays all errors** after compilation. If your code has mistakes, it will not compile. But the interpreter
   displays **errors of each line one by one**.

**4 Types of Interpreters**
Bytecode interpreter, Threaded code interpreter, Abstract syntax tree interpreter, Justin-in-time compilation

**args and kargs**
In cases when we **don't know how many arguments** will be passed to a function, like when we want to pass a **list or a tuple**
of values, we use *args.

**kwargs takes **keyword arguments when we don't know** how many there will be.

The recommendation is to rely on **kwargs** only for methods that have a **reduced scope**. Private methods (and by **private** in a 
context of Python. Methods starting by _) which are used in few places in the class are good candidates.

Everything in Python is an **object** and all variables hold references to the objects. So python is **call by reference**.
You cannot change the value of the references. However, you **can change the objects** if it is mutable.

A **lambda function is an anonymous function** that’s used when an anonymous function is required for a short period of time. This 
function can **only have one statement**, but it can have **any number of parameters**.

```python
a = lambda x, y : x*y
print(a(7, 19))
```

An **immutable** type cannot be changed. Examples are **integers, floats, strings, tuples**. 
A **mutable** type can change. Examples are **lists, dictionaries, sets, classes**.

**Tabs vs spaces**
The most popular way of indenting is with **spaces** only and also part of the PEP-8 standard. 

**Pickling(serialization)** in Python: The process in which the pickle module accepts various Python objects and converts them into a string representation 
and dumps the file accordingly using the dump function is called pickling. 

**Unpickling** in Python: The process of retrieving actual Python objects from the stored string representation is called unpickling.

The **docstring** in Python is also called a documentation string, it provides a way to document the Python classes, functions, 
and modules.

We can access the module written in **Python from C** by using the following method.
```python
Module == PyImport_ImportModule("<modulename>");
```

1. **WSGI stands for Web Server Gateway Interface, and ASGI stands for Asynchronous Server Gateway interface.**
2. Django provides a **default wsgi server**.
3. The django server should be used for development. I personally use **nginx** and **gunicorn** to run my server.

PEP 8 is the Python **latest coding convention** and it is abbreviated as **Python Enhancement Proposal**. It is all about how to 
format your Python code for maximum readability.

The following are the benefits of using Python language:
    Object-Oriented Language
    High-Level Language
    Dynamically Typed language
    Extensive support Libraries
    Presence of third-party modules
    Open source and community development
    Portable and Interactive
    Portable across Operating systems

**Statically typed languages**: In this type of language, the data type of a variable is known at the compile time which means the 
programmer has to specify the data type of a variable at the time of its declaration. 

**Dynamically typed languages**: These are the languages that do not require any pre-defined data type for any variable as it is 
interpreted at runtime by the machine itself. In these languages, interpreters assign the data type to a variable at runtime depending 
on its value.

Python uses the **Tim Sort algorithm** for sorting. It’s a stable sorting whose worst case is O(N log N). It’s a hybrid sorting 
algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.

```python
string = "GeeksforGeeks"
string.swapcase() ---> "gEEKSFORgEEKS"

## debug
python -m pdb python-script.py
```

We can delete a file using Python by following approaches:
os.remove()
os.unlink()

**PIP** is an acronym for Python Installer Package which provides a seamless interface to install various Python modules. It is a 
command-line tool that can search for packages over the internet and install them without any user interaction.

**Function Annotation** is a feature that allows you to **add metadata to function parameters and return values**. This way you can 
specify the input type of the function parameters and the return type of the value the function returns.

Function annotations are arbitrary Python expressions that are associated with various parts of functions. These expressions are 
**evaluated at compile time** and have **no life in Python’s runtime environment**. Python does not attach any meaning to these 
annotations. They take life when interpreted by third-party libraries, for example, **mypy**.
