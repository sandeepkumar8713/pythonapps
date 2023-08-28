## Inheritance 

Link : https://realpython.com/python-super/

Link : https://realpython.com/lessons/multiple-inheritance-python/

## Super 
1. At a high level super() gives you access to **methods in a superclass** from the subclass that inherits from it.
2. super() alone returns a **temporary object of the superclass** that then allows you to call that superclass’s methods. 
3. The primary use case of this is to **extend the functionality** of the inherited method.

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
```

1. Here you have implemented two methods for the Cube class: .surface_area() and .volume(). Both of these calculations 
   **rely on calculating the area** of a single face, so rather than reimplementing the area calculation, you use
   super() to extend the area calculation.
2. Also notice that the Cube class definition **does not have an .__init__()**. Because Cube inherits from Square
   and .__init__() doesn’t really do anything differently for Cube than it already does for Square, you can **skip defining**
   it, and the .__init__() of the superclass (Square) will be called automatically. 

## Super deep dive
In Python 3, the **super(Square, self)** call is equivalent to the parameterless **super()** call. The first parameter refers to
the subclass Square, while the second parameter refers to a Square object which, in this case, is self.

```python
class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
```

1. In this example, you are setting **Square as the subclass argument to super(), instead of Cube**. This causes super() to start 
   searching for a matching method (in this case, .area()) **at one level above Square** in the instance hierarchy, in this
   case Rectangle.
2. In this specific example, the behavior doesn’t change. But imagine that **Square also implemented an .area()** function
   that you wanted to make sure **Cube did not use**. Calling super() in this way allows you to do that.
3. What about the second parameter? Remember, this is an **object that is an instance of the class** used as the first parameter.
   For an example, isinstance(Cube, Square) must return True.
4. By including an instantiated object, super() returns a **bound method**: a method that is bound to the object, which gives
  the method the object’s context such as any instance attributes. If this parameter is not included, the method returned
   is just a function, unassociated with an object’s context.
5. Technically, super() doesn’t return a method. It returns a **proxy object**. This is an object that delegates calls to the 
   correct class methods without making an **additional object** in order to do so. 

## Super in Multiple Inheritance
Python supports multiple inheritance, in which a subclass can inherit from multiple superclasses that don’t necessarily
inherit from each other (also known as **sibling classes**).

```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

```

The problem, though, is that both superclasses (Triangle and Square) define a .area(). In this case  Triangle.area() will be 
called as it was first in order of inheritance. But we will get error as **self.height** is not defined. This order of 
excution is defined by **Method Resolution Order**

## Method Resolution Order

The method resolution order (or MRO) tells Python how to search for **inherited methods**. This comes in handy when you’re
using super() because the MRO tells you exactly where Python will look for a method you’re calling with super()
and in what order.

```python
>>> RightPyramid.__mro__
(<class '__main__.RightPyramid'>, <class '__main__.Triangle'>, 
 <class '__main__.Square'>, <class '__main__.Rectangle'>, 
 <class 'object'>)
```

Just by changing the **signature of the RightPyramid class**, you can search in the order you want, and the methods will
resolve correctly.

```python
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

>>> pyramid = RightPyramid(2, 4)
>>> RightPyramid.__mro__
(<class '__main__.RightPyramid'>, <class '__main__.Square'>, 
<class '__main__.Rectangle'>, <class '__main__.Triangle'>, 
<class 'object'>)
>>> pyramid.area()
20.0
```

When you’re using super() with multiple inheritance, it’s imperative to design your classes to **cooperate**. Part of this is 
ensuring that your methods are **unique** so that they get resolved in the MRO, by making sure method signatures are 
unique—whether by using **method names or method parameters**.

Two fix Triangle object initiate we will need to do following.

```python
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
```

## Multiple Inheritance Alternatives
1. **Composition** : (https://realpython.com/inheritance-composition-python/)
2. **Mixin** : A mixin works as a kind of inheritance, but instead of defining an **“is-a”** relationship it may be more
   accurate to say that it defines an **“includes-a”** relationship. With a mix-in you can write a behavior that can be
   **directly included** in any number of other classes.

```python
class VolumeMixin:
    def volume(self):
        return self.area() * self.height

class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6
```

This mixin can be used the same way in any other class that has an area defined for it and for which the formula 
**area * height** returns the correct volume.

Read more about MRO overloading to change sequence of call: 
https://stackoverflow.com/questions/20822850/change-python-mro-at-runtime
https://pybites.blogspot.com/2009/01/mro-magic.html


-------------------------------------------------------------------

## Types of Inheritance 

1. **Single Inheritance** (A -> B)

```python
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
```

2. **Multiple Inheritance** (A,B -> C)

```python
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
```

3. **Multilevel Inheritance** (A -> B -> C)

4. **Hierarchical Inheritance** (A -> B,C,D)

```python
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
```

5. **Hybrid Inheritance** (all mixed Multilevel, Hierarchical, Multiple, Single)
