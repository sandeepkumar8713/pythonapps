## Decorators

Link : https://realpython.com/primer-on-python-decorators/

Decorators provide a simple syntax for calling **higher-order functions**.

By definition, a decorator is a function that takes **another function and extends the behavior** of the latter function
without **explicitly modifying** it.

## First-Class Objects
In Python, **functions are first-class objects**. This means that functions can be passed around and used as **arguments**, 
just like any other object (string, int, float, list, and so on).

```python
def say_hello(name):
    return f"Hello {name}"

def greet_bob(greeter_func):
    return greeter_func("Bob")

greet_bob(say_hello)
```

The say_hello function is named without parentheses. This means that only a **reference to the function** is passed. 
The function is **not executed**. The greet_bob() function, on the other hand, is written with parentheses, so it will
be called as usual.

## Inner Function
It’s possible to define functions inside other functions. Such functions are called **inner functions**.

```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

The inner functions are not defined until the parent function is called. They are locally scoped to parent(): they only exist 
inside the parent() function as **local variables**. 

## Returning Functions From Functions
Python also allows you to use functions as return values. The following example returns one of the inner functions from
the outer parent() function:

```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
first() # 'Hi, I am Emma'
```

Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference
to the function first_child.

## Simple decorators 

Put simply: **decorators wrap a function, modifying its behavior.**
It takes function refrence as input and return another function reference, which has modified the way
original function is called. 

```python
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
```

## Syntactic Sugar
Python allows you to use decorators in a simpler way with the **@** symbol, sometimes called the **“pie”** syntax. The 
following example does the exact same thing as the first decorator example:

```python
@my_decorator
def say_whee():
    print("Whee!")
```

So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). 

## Reusing Decorators
Let’s move the decorator to its **own module** that can be used in many other functions.

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
```

## Decorating Functions With Arguments
The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an 
**arbitrary number of positional and keyword arguments**.

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

say_whee() # Both the call works
greet("World") 
```

## Returning Values From Decorated Functions
You need to make sure the **wrapper function returns the return value of the decorated function**.

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

## Who are you?
A great convenience when working with Python, especially in the **interactive shell**, is its powerful **introspection ability**. 
Introspection is the ability of an object to know about its **own attributes** at runtime. 

```python
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    <full help message>

>>> say_whee
<function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>
```

However, after being decorated, say_whee() has gotten very **confused** about its identity. It now reports being the 
wrapper_do_twice() inner function inside the do_twice() decorator. Although technically true, 
this is **not very useful** information.

To fix this, decorators should use the **@functools.wraps decorator**, which will preserve information about the
original function. Update decorators.py again:

```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

>>> say_whee
<function say_whee at 0x7ff79a60f2f0>
```

Technical Detail: The @functools.wraps decorator uses the function functools.update_wrapper() to update **special attributes** \
like __name__ and __doc__ that are used in the introspection.

# Real world example : https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples
1. Make a timer decorator: to print time spent in execution
2. Debugging code: printing the input and output of the function
3. Slow down code: you want to rate-limit a function that continuously checks whether a resource—like a web page—has changed. The 
   @slow_down decorator will sleep one second before it calls the decorated function.
4. Registering Plugins, They can also simply register(update entry in map) that a function exists and return it unwrapped. 
   This can be used, for instance, to create a light-weight plug-in architecture. (This is how globls() work)
5. Check if user is logged in.
6. Adding Information About Units.
7. Validating Jsons.

```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```

## Decorating classes : 
There are two different ways you can use decorators on classes. The first one is very close to what you have already done with
functions: you can **decorate the methods** of a class. 

Some commonly used decorators that are even built-ins in Python are **@classmethod, @staticmethod, and @property**. 
The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not 
connected to a particular instance of that class. The @property decorator is used to customize getters and setters
for class attributes. 

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

c = Circle(5)
c.radius # 5
c.area # 78.56
c.radius = 2
c = Circle.unit_circle()
c.pi() # 3.14
Circle.pi() # 3.14
```

.radius is a mutable property: it can be set to a different value. However, by defining a setter method, we can do some error 
testing to make sure it’s not set to a nonsensical negative number. **Properties are accessed as attributes without parentheses**.

.unit_circle() is a class method. It’s not bound to one particular instance of Circle. Class methods are often used as 
**factory methods** that can create specific instances of the class.

.pi() is a static method. It’s not really dependent on the Circle class, except that it is part of its namespace. Static methods 
can be called on either **an instance or the class**.

A common use of class decorators is to be a **simpler alternative** to some use-cases of metaclasses. In both cases, 
you are changing the definition of a class dynamically.

## Creating Singletons

A singleton is a class with only one instance. There are several singletons in Python that you use frequently, including
**None, True, and False**. It is the fact that None is a singleton that allows you to compare for None using the **is keyword**,
Using is returns True only for objects that are the exact same instance.

The only difference is that we are using cls instead of func as the parameter name to indicate that it is meant to be a 
**class decorator**.

```python
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

>>> first_one = TheOne()
>>> another_one = TheOne()
>>> id(first_one)  # 140094218762280
>>> id(another_one) # 140094218762280 same memory address
```

Singleton classes are not really used as often in Python as in other languages. The effect of a singleton is usually
better implemented as a **global variable** in a module.

## Caching result

```python
import functools
from decorators import count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
```

## Explaination : func(*args, **kwargs)
args converts input to a **list**
kwargs converts input to a **dict** with key and values

```python
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result
print(my_sum(1, 2, 3))


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

## Unpacking * and **

```python
my_list = [1, 2, 3]
print(my_list) [1, 2, 3]
print(*my_list) # 1 2 3

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4}
```

