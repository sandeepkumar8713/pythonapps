## Metaclass

The term **metaprogramming** refers to the potential for a program to have **knowledge of** or manipulate itself.
Python supports a form of metaprogramming for classes called **metaclasses**.

## New ways
New-style classes unify the concepts of class and type. If obj is an instance of a new-style class, type(obj) is 
the same as obj.__class__:


```python
>>> class Foo:
        pass
>>> obj = Foo()
>>> obj.__class__
<class '__main__.Foo'>
>>> type(obj)
<class '__main__.Foo'>
>>> obj.__class__ is type(obj)
True

>>> n = 5
>>> d = { 'x' : 1, 'y' : 2 }

>>> class Foo:
        pass

>>> x = Foo()

>>> for obj in (n, d, x):
     print(type(obj) is obj.__class__)

True
True
True
```

In Python 3, all classes are new-style classes. Thus, in Python 3 it is reasonable to refer to an object’s type and
its class interchangeably.

Remember that, in Python, **everything is an object**. Classes are objects as well. As a result, a class must have a type. 
**What is the type of a class**?

```python
class Foo:
    pass
>>> type(Foo)
<class 'type'>

>>> for t in int, float, dict, list, tuple:
     print(type(t))

<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>

>>> type(type)
<class 'type'>
```

In general, **the type of any new-style class is type**. The type of the built-in classes you are familiar with is also type.

**type is a metaclass, of which classes are instances.**

## Defining a Class Dynamically
You can also call type() with three arguments—type(<name>, <bases>, <dct>):
<name> specifies the class name. This becomes the __name__ attribute of the class.
<bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
<dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the 
class.
Calling type() in this manner creates a **new instance of the type metaclass**. In other words, it dynamically
creates a new class.

## Example 1

In this first example, the <bases> and <dct> arguments passed to type() are both empty. **No inheritance** from any parent
class is specified, and **nothing is initially placed** in the namespace dictionary. 

```python
Foo = type('Foo', (), {})
x = Foo()

class Foo:   # Equivalent to this class definition
    pass
```

## Example 2
Here, <bases> is a tuple with a single element Foo, specifying the parent class that Bar inherits from. An attribute, attr, is initially placed into the namespace dictionary.

```python
Bar = type('Bar', (Foo,), dict(attr=100))
>>> x = Bar()
>>> x.attr
100
>>> x.__class__
<class '__main__.Bar'>
>>> x.__class__.__bases__
(<class '__main__.Foo'>,)

class Bar(Foo):  # Equivalent to this class definition
    attr = 100
```

## Example 3 

```python
Foo = type(
     'Foo',
     (),
     {
         'attr': 100,
         'attr_val': lambda x : x.attr
     }
)

class Foo:  # Equivalent to this class definition
    attr = 100
    def attr_val(self):
        return self.attr
```

## Example 4 
To define complex method we use following example

```python
def f(obj):
    print('attr =', obj.attr)

Foo = type(
     'Foo',
     (),
     {
         'attr': 100,
         'attr_val': f
     }
)

def f(obj):
    print('attr =', obj.attr)

class Foo:  # Equivalent to this class definition
    attr = 100
    attr_val = f
```

## Custom Metaclass

```python
class Foo:
    pass

f = Foo()
```

The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:
1. The __call__() method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class
   is the **type metaclass**, so type’s __call__() method is invoked.
2. That __call__() method in turn invokes the following:
    __new__()
    __init__()

If Foo does not define __new__() and __init__(), default methods are **inherited from Foo’s ancestry**. But if Foo does
define these methods, they **override** those from the ancestry, which allows for customized behavior when instantiating Foo.

```python
def new(cls):
     x = object.__new__(cls)
     x.attr = 100
     return x

Foo.__new__ = new
f = Foo()
f.attr   # 100
```

class Foo: each time an instance of Foo is created, by default it is **initialized with an attribute called attr**, which has a 
value of 100. (Code like this would more usually appear in the __init__() method and not typically in __new__(). 
This example is contrived for demonstration purposes.)

**You can’t reassign the __new__() method of the type metaclass**. Python doesn’t allow it.

One possible solution is a custom metaclass. Essentially, instead of mucking around with the type metaclass, you can 
define your own metaclass, which derives from type, and then you can muck around with that instead.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class Foo(metaclass=Meta):
     pass

Foo.attr   # 100
```

The definition header class Meta(type): specifies that Meta derives from type. Since type is a metaclass, 
that makes **Meta a metaclass as well**.

In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template
for the creation of classes. Metaclasses are sometimes referred to as **class factories**.

## Alternative 
**Decorator** We are extending the class using decorator


```python
def decorator(cls):
     class NewClass(cls):
        attr = 100
     return NewClass

@decorator
class X:
    pass

X.attr # 100
```
